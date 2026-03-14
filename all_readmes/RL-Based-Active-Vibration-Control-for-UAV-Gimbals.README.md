name:	nusRying/RL-Based-Active-Vibration-Control-for-UAV-Gimbals
description:	
--
# RL-Based Active Vibration Control for UAV Gimbals

This repository is a full scaffold for training and deploying RL controllers
for 3-DOF gimbal active vibration control (AVC), with mathematically explicit
state/action/reward design and a practical sim-to-real path.

It is built around:
- A digital twin environment (`Gymnasium`) with injected 100-400 Hz disturbances.
- Continuous-action RL algorithms (`SAC`, `DDPG`) for torque-level control.
- Optional hybrid mode (classical PID baseline + RL delta correction).
- Export to ONNX and a deployment runtime stub for MAVLink/embedded integration.

## 1) Problem Statement

Goal: minimize payload jitter and pointing error under high-frequency disturbances
while keeping actuation smooth enough to avoid thermal and mechanical stress.

Control target in this codebase:
- Stabilize 3 axes around `target_angles_rad` (default zero).
- Reject harmonic disturbance torques in the propeller vibration band.
- Learn a policy robust to payload and mount variability.

Why RL instead of only PID/LQR:
- Disturbance spectrum is non-stationary in real UAS operation.
- Gimbal dynamics can become nonlinear as payload/inertia changes.
- RL can learn a direct state-to-action mapping without re-deriving linear models
  for each payload/mount configuration.

## 2) End-to-End Pipeline

1. Define environment + digital twin parameters in `configs/env.yaml`.
2. Select algorithm/hyperparameters in `configs/sac.yaml` or `configs/ddpg.yaml`.
3. Train with vectorized simulation (`scripts/train.py`).
4. Evaluate with deterministic policy rollouts (`scripts/eval.py`).
5. Export actor network to ONNX (`scripts/export_onnx.py`).
6. Run inference loop on onboard computer and wire telemetry/actuation transport
   (`src/rl_avc_gimbal/deployment/mavlink_runtime_stub.py`).
7. Optionally merge rollout logs into a reusable dataset (`scripts/build_dataset.py`).
8. Compose a hardware-specific env config (`scripts/compose_env.py`).

This maps directly to:
- Phase 1 (modeling): `src/rl_avc_gimbal/sim/digital_twin.py`
- Phase 2 (RL MDP): `src/rl_avc_gimbal/envs/gimbal_avc_env.py`
- Phase 3 (sim-to-real): hybrid mode + randomization in `configs/env.yaml`
- Phase 4 (deployment): `src/rl_avc_gimbal/deployment/*.py`

## 3) Mathematical Formulation

### 3.1 State and Observation

Per step, the environment frame is:
\[
f_t = [\theta_t,\ \dot{\theta}_t,\ a_t] \in \mathbb{R}^{9}
\]
where:
- \(\theta_t \in \mathbb{R}^3\): roll/pitch/yaw angles
- \(\dot{\theta}_t \in \mathbb{R}^3\): angular rates
- \(a_t \in \mathbb{R}^3\): payload IMU linear acceleration proxy

To expose periodic structure to a feed-forward policy, the environment stacks
history of length \(H\):
\[
s_t = [f_{t-H+1},\dots,f_t] \in \mathbb{R}^{9H}
\]

Default \(H=8\), so observation dimension is \(72\).

Why this choice:
- Vibration suppression depends on short-time temporal context.
- History stacking avoids immediate need for recurrent policies.
- 8 frames at \(dt=5\) ms gives 40 ms context, enough to expose phase trends.

### 3.2 Action

The policy outputs normalized action:
\[
u_t \in [-1,1]^3
\]

Non-hybrid mode:
\[
\tau_t = u_t \odot \tau_{\max}
\]

Hybrid PID + RL-delta mode:
\[
e_t = \theta^\* - \theta_t
\]
\[
\tau_{\text{pid},t} = K_p e_t + K_i \int e_t dt + K_d \frac{de_t}{dt}
\]
\[
\tau_{\Delta,t} = u_t \odot \tau_{\max} \odot s_{\Delta}
\]
\[
\tau_t = \text{clip}(\tau_{\text{pid},t} + \tau_{\Delta,t},-\tau_{\max},\tau_{\max})
\]

Where \(\odot\) is elementwise multiplication.

Why normalized actions:
- Stable, algorithm-agnostic interface for SAC and DDPG.
- Physical limits are applied inside environment, preventing unbounded torques.

Why hybrid option:
- Safer early sim-to-real transfer.
- PID handles low-frequency setpoint stabilization; RL learns residual cancellation.

### 3.3 Digital Twin Dynamics

Per axis \(i\), implemented in `SimpleGimbalTwin.step`:
\[
I_i \ddot{\theta}_i =
\tau_{i} + \tau_{d,i} - c_i \dot{\theta}_i - k_i (\theta_i - \theta_i^\*)
\]

In vector form:
\[
\ddot{\theta}_t = \frac{ \tau_t + \tau_{d,t} - c \odot \dot{\theta}_t - k \odot (\theta_t-\theta^\*) }{I}
\]

Explicit Euler integration:
\[
\dot{\theta}_{t+1} = \dot{\theta}_t + \ddot{\theta}_t \, dt
\]
\[
\theta_{t+1} = \theta_t + \dot{\theta}_{t+1} \, dt
\]

IMU proxy:
\[
a_t = r \, \ddot{\theta}_t + \eta_t,\ \eta_t \sim \mathcal{N}(0,\sigma_{\text{imu}}^2)
\]

Why this model:
- Intentionally lightweight for fast RL iteration and parallel env rollouts.
- Captures the dominant damping/stiffness/inertia tradeoffs required for AVC.
- Explicitly exposes disturbance torque channel for vibration robustness training.

Limitations to know:
- No full 3-axis cross-coupling matrix or actuator electrical dynamics yet.
- No sensor delay/filter pipeline yet.
- These are suitable next upgrades after policy sanity is confirmed.

### 3.4 Disturbance Injection

For each axis:
\[
\tau_{d,i}(t) = A_i \sin(2\pi f_i t + \phi_i) + \epsilon_i
\]
with:
- \(f_i \sim \mathcal{U}(100,400)\) Hz
- \(\phi_i \sim \mathcal{U}(0,2\pi)\)
- \(\epsilon_i \sim \mathcal{N}(0,\sigma_d^2)\)

Why 100-400 Hz:
- Matches common multirotor motor/prop harmonic region that causes camera jitter.

Why harmonic + Gaussian:
- Harmonic term models dominant periodic vibration.
- Gaussian term models broadband residuals and unmodeled excitations.

### 3.5 Reward Function

Implemented as:
\[
r_t = -\Big(
w_a \cdot \frac{1}{3}\|a_t\|_2^2
+ w_p \cdot \frac{1}{3}\|\theta_t-\theta^\*\|_2^2
+ w_c \cdot \frac{1}{3}\|\tau_t-\tau_{t-1}\|_2^2
\Big)
\]

Default weights:
- \(w_a = 1.0\)
- \(w_p = 0.25\)
- \(w_c = 0.01\)

Why this decomposition:
- `accel` term directly penalizes image-jitter-causing vibration.
- `position` term prevents drift from optical pointing target.
- `chatter` term suppresses aggressive switching that overheats or wears motors.

### 3.6 Episode Boundaries

Termination:
\[
\max_i |\theta_i| > \theta_{\max}
\]
with default \(\theta_{\max}=1.2\) rad.

Truncation:
\[
t \ge T_{\text{episode}}
\]
with \(T_{\text{episode}}=20\) s and \(dt=0.005\) s, so 4000 steps/episode.

Why:
- Termination protects simulation from irrecoverable unstable states.
- Fixed horizon produces consistent training return statistics.

## 4) Domain Randomization Math

At every reset:
- Payload mass \(m \sim \mathcal{U}(0.25,0.75)\) kg
- Reference mass \(m_{\text{ref}}=0.5\) kg
- Payload scale:
\[
s_m = \max(0.2,\ m/m_{\text{ref}})
\]
- Mount stiffness scale \(s_k \sim \mathcal{U}(0.8,1.2)\)
- Damping scale \(s_c \sim \mathcal{U}(0.9,1.1)\)

Applied as:
\[
I = s_m I_0,\quad k=s_k k_0,\quad c=s_c c_0
\]

Why:
- Teaches invariances to camera swaps and mount variability.
- Reduces overfitting to one nominal dynamic profile.

## 5) SAC and DDPG: Why Both

Both are designed for continuous control.

SAC advantages:
- Stochastic policy with entropy regularization.
- Typically more robust to noisy dynamics and disturbance-rich environments.
- Better default first choice for this project.

DDPG advantages:
- Deterministic actor can be simpler to reason about and lighter in some setups.
- Useful comparison baseline and can be easier to deploy in constrained settings.

### 5.1 SAC Objective (conceptual)
\[
J_Q(\phi)=\mathbb{E}\Big[\big(Q_\phi(s,a)-y\big)^2\Big]
\]
\[
y=r+\gamma \mathbb{E}_{a'\sim\pi}\left[
Q_{\bar{\phi}}(s',a')-\alpha \log \pi(a'|s')
\right]
\]
\[
J_\pi(\theta)=\mathbb{E}_{s\sim\mathcal{D},a\sim\pi_\theta}
\left[\alpha \log \pi_\theta(a|s)-Q_\phi(s,a)\right]
\]

### 5.2 DDPG Objective (conceptual)
\[
y=r+\gamma Q_{\phi'}(s',\mu_{\theta'}(s'))
\]
\[
J_Q(\phi)=\mathbb{E}\Big[(Q_\phi(s,a)-y)^2\Big]
\]
\[
\nabla_\theta J \approx
\mathbb{E}\left[
\nabla_a Q_\phi(s,a)\vert_{a=\mu_\theta(s)}
\nabla_\theta \mu_\theta(s)
\right]
\]

The training implementation uses Stable-Baselines3 in
`src/rl_avc_gimbal/training/train.py`.

## 6) Hyperparameter Choices and Rationale

From `configs/sac.yaml` and `configs/ddpg.yaml`:

- `n_envs=4`: balances throughput vs CPU usage for most workstations.
- `learning_rate=3e-4`: stable default for MLP actor-critic methods.
- `buffer_size=500000`: enough diversity for randomization + disturbance phases.
- `learning_starts=10000`: collects initial varied rollouts before updates.
- `batch_size=512`: reduces gradient noise in disturbance-heavy tasks.
- `gamma=0.99`: preserves long-horizon stabilization objective.
- `tau=0.005`: conservative Polyak averaging for stable targets.
- `train_freq=[1, step]`: online update cadence aligned to control steps.
- `net_arch=[256,256]`: enough capacity without over-parameterizing.
- `action_noise_sigma=0.10` (DDPG): explicit exploration in deterministic policy.

Callbacks:
- `CheckpointCallback`: saves periodic snapshots.
- `EvalCallback`: tracks deterministic performance and best model.

### 6.1 Environment Parameter-by-Parameter Rationale

From `configs/env.yaml`:

- `seed: 42`
  - Reason: deterministic reproducibility for debugging and regression checks.
- `dt: 0.005` s
  - Reason: 200 Hz control update is a practical minimum for AVC and aligns with
    embedded real-time rates.
- `episode_seconds: 20`
  - Reason: enough trajectory length to see low-frequency drift + many high-frequency cycles.
- `history_length: 8`
  - Reason: 40 ms short memory at 200 Hz gives phase context for periodic disturbances.
- `termination_max_angle_rad: 1.2`
  - Reason: marks unrecoverable attitude excursions before learning destabilizes.
- `imu_noise_std: 0.01`
  - Reason: prevents overfitting to noise-free acceleration signals.
- `torque_limit_nm: [0.60, 0.60, 0.40]`
  - Reason: enforces actuator realism and keeps RL inside feasible motor envelope.
- `inertia_kgm2: [0.012, 0.012, 0.008]`
  - Reason: representative starting point for compact 3-axis payload assemblies.
- `damping: [0.090, 0.090, 0.070]`
  - Reason: baseline dissipation to avoid unrealistically persistent oscillation.
- `stiffness: [0.800, 0.800, 0.500]`
  - Reason: captures restoring behavior toward setpoint per axis.
- `target_angles_rad: [0.0, 0.0, 0.0]`
  - Reason: zero-hold stabilization benchmark; easy to compare policies.
- `lever_arm_m: 0.08`
  - Reason: converts angular acceleration to linear acceleration proxy near payload sensor.

Reward weights:
- `weights.accel: 1.0`
  - Reason: primary objective is vibration suppression at payload.
- `weights.position: 0.25`
  - Reason: secondary objective; enough to prevent drift without over-constraining RL.
- `weights.chatter: 0.01`
  - Reason: small but persistent smoothness regularizer for thermal/mechanical safety.

Disturbance:
- `disturbance.enabled: true`
  - Reason: training without disturbance defeats AVC objective.
- `disturbance.frequency_hz: [100, 400]`
  - Reason: targets dominant multirotor vibration/harmonic region.
- `disturbance.amplitude: [0.20, 0.20, 0.15]`
  - Reason: forces nontrivial suppression effort while remaining recoverable.
- `disturbance.gaussian_std: 0.02`
  - Reason: injects non-periodic uncertainty to improve robustness.

Domain randomization:
- `payload_mass_kg: [0.25, 0.75]`
  - Reason: covers wide camera/payload swap envelope.
- `mount_stiffness_scale: [0.80, 1.20]`
  - Reason: models mount aging, temperature variation, and build tolerances.
- `damping_scale: [0.90, 1.10]`
  - Reason: introduces realistic dissipation variability without destabilizing all rollouts.

Hybrid control defaults:
- `hybrid_control.enabled: false`
  - Reason: pure RL baseline first, then staged enable for transfer safety.
- `pid_kp: [4.0, 4.0, 3.0]`
  - Reason: moderate proportional centering; yaw often gets slightly lower gain.
- `pid_ki: [0.2, 0.2, 0.2]`
  - Reason: slow bias rejection without strong windup pressure.
- `pid_kd: [0.10, 0.10, 0.08]`
  - Reason: damping boost to reduce overshoot and residual ringing.
- `integral_limit: [0.40, 0.40, 0.30]`
  - Reason: anti-windup bound aligned with axis torque authority.
- `rl_delta_scale: [0.25, 0.25, 0.25]`
  - Reason: caps RL residual authority so baseline PID remains dominant early on.

### 6.2 Algorithm Config Parameter Rationale

From `configs/sac.yaml` / `configs/ddpg.yaml`:

- `total_timesteps: 300000 (SAC), 350000 (DDPG)`
  - Reason: DDPG often needs longer training to match SAC robustness in noisy tasks.
- `policy: MlpPolicy`
  - Reason: sufficient for stacked-state vector input without image encoder overhead.
- `gradient_steps: 1`
  - Reason: stable update-to-data ratio for on-policy-like environment drift.
- `verbose: 1`
  - Reason: useful diagnostics without excessive logging overhead.
- `device: auto`
  - Reason: portable default across CPU-only and CUDA setups.
- `log_interval: 10`
  - Reason: regular visibility into training curve with low console noise.
- `checkpoint_freq: 50000`
  - Reason: captures recoverable milestones without over-fragmenting storage.
- `eval_freq: 25000`
  - Reason: enough cadence to detect regressions before wasting full runs.

## 7) File-Level Architecture

Core modules:
- Environment: `src/rl_avc_gimbal/envs/gimbal_avc_env.py`
- Disturbance model: `src/rl_avc_gimbal/envs/disturbance.py`
- Dynamics model: `src/rl_avc_gimbal/sim/digital_twin.py`
- PID controller: `src/rl_avc_gimbal/controllers/pid.py`
- Training pipeline: `src/rl_avc_gimbal/training/train.py`
- Evaluation pipeline: `src/rl_avc_gimbal/training/evaluate.py`
- ONNX export: `src/rl_avc_gimbal/deployment/export_onnx.py`
- Runtime stub: `src/rl_avc_gimbal/deployment/mavlink_runtime_stub.py`

Configs:
- Environment: `configs/env.yaml`
- SAC hyperparameters: `configs/sac.yaml`
- DDPG hyperparameters: `configs/ddpg.yaml`

CLI wrappers:
- `scripts/train.py`
- `scripts/eval.py`
- `scripts/export_onnx.py`
- `scripts/analyze_frequency.py`
- `scripts/build_dataset.py`
- `scripts/compose_env.py`
- `scripts/check_env.py`
- `scripts/probe_env.py`

## 8) Training, Evaluation, and Export Commands

Use your existing Conda environment:

```powershell
conda activate comp_vision
pip install -r requirements.txt
pip install -e .
```

Train SAC:

```powershell
python scripts/train.py `
  --algo sac `
  --env-config configs/env.yaml `
  --algo-config configs/sac.yaml `
  --run-dir runs/sac_baseline
```

Train DDPG:

```powershell
python scripts/train.py `
  --algo ddpg `
  --env-config configs/env.yaml `
  --algo-config configs/ddpg.yaml `
  --run-dir runs/ddpg_baseline
```

Evaluate:

```powershell
python scripts/eval.py `
  --algo sac `
  --model-path runs/sac_baseline/final_model `
  --env-config configs/env.yaml `
  --episodes 10 `
  --save-json runs/sac_baseline/eval_summary.json `
  --record-first-episode runs/sac_baseline/rollout_ep0.npz
```

Export ONNX:

```powershell
python scripts/export_onnx.py `
  --algo sac `
  --model-path runs/sac_baseline/final_model `
  --env-config configs/env.yaml `
  --output models/sac_policy.onnx
```

Analyze frequency response:

```powershell
python scripts/analyze_frequency.py `
  --rollout-npz runs/sac_baseline/rollout_ep0.npz `
  --band-min-hz 10 `
  --band-max-hz 90 `
  --save-json runs/sac_baseline/frequency_summary.json `
  --save-csv runs/sac_baseline/frequency_trace.csv
```

Sampling note:
- Frequency analysis is limited by Nyquist (`f_N = 1/(2*dt)`).
- With default `dt=0.005`, `f_N=100 Hz`, so `100-400 Hz` is not fully observable.
- Use `10-90 Hz` at current `dt`, or reduce `dt` (increase sample rate) for higher bands.

Build merged dataset (optional):

```powershell
python scripts/build_dataset.py `
  --glob "runs/*/rollout_ep0.npz" `
  --output datasets/avc_merged.npz `
  --save-report-json datasets/avc_merged_report.json
```

Compose hardware env config:

```powershell
python scripts/compose_env.py `
  --base configs/env.yaml `
  --profile configs/env_hw_profile.yaml `
  --output configs/env_hw_merged.yaml
```

Check `comp_vision` environment health:

```powershell
python scripts/check_env.py --save-json runs/env_report.json
```

Probe episode completion (useful before RLlib/PPO runs):

```powershell
python scripts/probe_env.py `
  --env-config configs/env_hw_merged.yaml `
  --episodes 5 `
  --policy random
```

## 9) Evaluation Metrics

The evaluation script reports:
- Episode return mean/std:
\[
G=\sum_t r_t
\]
- Acceleration RMS mean/std:
\[
\text{RMS}_a = \sqrt{\frac{1}{T}\sum_t \text{accel\_term}_t}
\]
- Number of early terminations vs horizon truncations.

Interpretation:
- Lower (more negative) return can still happen if chatter penalty is too high.
- Prioritize low `Accel RMS` first for vibration suppression.
- Track early terminations; they indicate unstable policies or too-hard randomization.

## 10) Deployment Path (Jetson/Pixhawk/MCU)

Current runtime architecture:
1. Policy exported to ONNX actor network.
2. `onnxruntime` session loads model.
3. Telemetry frames build stacked observation identical to training format.
4. Inference returns action; command is sent to low-level actuator loop.

In `mavlink_runtime_stub.py`, you must implement:
- `read_telemetry()`
- `send_torque()`

Control-rate math:
- For 200 Hz runtime, control period is 5 ms.
- Total loop time (read + preprocess + inference + write) must stay < 5 ms.
- Targeting < 2-3 ms for inference provides margin for I/O jitter.

Why ONNX:
- Framework-independent runtime.
- Easier path to TensorRT or hardware-specific acceleration later.

## 11) Sim-to-Real Strategy in This Repo

Recommended sequence:
1. Train in pure simulation until reward and RMS stabilize.
2. Enable hybrid mode for safer residual learning:
   - `hybrid_control.enabled: true`
3. Expand randomization ranges gradually.
4. Replace stub bridge with ROS2/Gazebo or Isaac connection.
5. Move to HIL before free-flight validation.

Why staged transfer:
- Avoid unsafe random exploration on hardware.
- Preserve baseline stability while RL learns high-frequency correction.

## 12) Safety and Practical Notes

- Torque saturation is always enforced in twin dynamics.
- PID integral has configurable clamping to reduce windup.
- Chatter penalty is essential for thermal reliability.
- Keep per-axis sign conventions consistent from simulator to hardware.
- Verify axis ordering (`roll, pitch, yaw`) end-to-end before flight tests.

## 13) Known Simplifications and Next Technical Upgrades

Current model simplifications:
- Decoupled per-axis second-order dynamics.
- No explicit motor electrical model/current loop.
- No modeled transport delay or quantization.

High-impact upgrades:
- Add axis coupling matrix and gyroscopic cross-terms.
- Add motor torque-current saturation and deadzone/hysteresis.
- Add sensor/actuator delay and low-pass filtering in environment.
- Add frequency-domain reward term (e.g., PSD in known vibration bands).
- Add constrained RL or safety shield around torque commands.

## 14) Quick Project Tree

```text
configs/
  env.yaml
  sac.yaml
  ddpg.yaml
  env_hw_profile.example.yaml
  env_hw_profile.yaml
  env_hw_merged.yaml
  env_hw_debug_120.yaml
docs/
  frequency_response_appendix.md
  tuning_playbook.md
  dataset_collection.md
  hardware_kickoff_checklist.md
  comp_vision_env_notes.md
  rllib_debug_next_steps.md
  sac_hw_short_baseline.md
scripts/
  train.py
  eval.py
  export_onnx.py
  analyze_frequency.py
  build_dataset.py
  compose_env.py
  check_env.py
  probe_env.py
src/rl_avc_gimbal/
  controllers/
  deployment/
  envs/
  sim/
  training/
tests/
  test_env_smoke.py
```

## 15) Additional Technical Docs

- Frequency-domain interpretation and Bode-style analysis:
  `docs/frequency_response_appendix.md`
- Strict log-driven tuning procedure:
  `docs/tuning_playbook.md`
- Optional rollout dataset workflow:
  `docs/dataset_collection.md`
- Hardware kickoff and calibration checklist:
  `docs/hardware_kickoff_checklist.md`
- `comp_vision` dependency troubleshooting:
  `docs/comp_vision_env_notes.md`
- RLlib-specific debug flow for zero reward/length:
  `docs/rllib_debug_next_steps.md`
- Recorded baseline metrics from first SAC hardware-profile run:
  `docs/sac_hw_short_baseline.md`


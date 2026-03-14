name:	nusRying/Deep_Features_PhD_Research
description:	
--
# Project Architecture: 7 Standalone Experimental Phases

The entire research pipeline has been refactored into 7 fully modular, reproducible phases. Each phase is housed in its own directory with isolated dependencies and a self-contained execution script (`main.py`).

## ≡ƒôé Directory Structure

```plaintext
project_root/
Γö£ΓöÇΓöÇ data/                               # Place raw input datasets here
Γö£ΓöÇΓöÇ phase_v1_baseline/                  # Standard ExSTraCS model with PCA
Γö£ΓöÇΓöÇ phase_v2_safety/                    # Adds Sensitivity-optimized threshold tuning
Γö£ΓöÇΓöÇ phase_v3_ensemble/                  # Multi-seed probability averaging (variance reduction)
Γö£ΓöÇΓöÇ phase_v4_stacking/                  # Stacking ensemble with SMOTE and LogReg meta-committee
Γö£ΓöÇΓöÇ phase_v5_universal_balance/         # Advanced SMOTE-ENN cleaning + Out-of-Fold (OOF) features
Γö£ΓöÇΓöÇ phase_v6_global_peak/               # 3-Tier Stacking + LCS Feature Pruning (Theoretical Limit)
ΓööΓöÇΓöÇ phase_v7_knowledge_discovery/       # MASTER: All above + Clinical Rule Extraction
```

## ΓÜÖ∩╕Å Prerequisites & Setup

**Python Version**: Python 3.9+

**Dependencies**: Each phase contains its own `requirements.txt`. Before running a phase, install its specific environment:

```bash
cd phase_v7_knowledge_discovery
pip install -r requirements.txt
```

## ≡ƒÜÇ How to Execute

To run the full pipeline for any specific phase, navigate to its directory and execute the main script.

Example (Running Phase 7):

```bash
cd phase_v7_knowledge_discovery
python main.py
```

_(Note: Full execution of advanced phases like v6 and v7 may take approximately 12 hours using an RTX 4060 Ti / 16GB RAM.)_

## ≡ƒº¬ Verification (Smoke Tests)

For the heavier models (Phases v6 and v7), you can run a rapid validation pipeline to verify environment setup and code execution without waiting for full model convergence (~15 mins):

```bash
python main.py --smoke-test
```

## ≡ƒôè Outputs & Artifacts

Upon completion, each phase automatically generates the following artifacts within its respective directory:

- **Models**: Serialized model weights are saved in the `models/` subdirectory.
- **Metrics**: Comprehensive performance results are exported as JSON files in the `results/` subdirectory.
- **Knowledge Discovery**: For Phase v7, the extracted Clinical Rule reports are generated at: `phase_v7_knowledge_discovery/results/clinical_consensus_report.txt`.


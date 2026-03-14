name:	nusRying/SATCOM-DVBS2X
description:	
--
# DVBS2X ΓÇö DVBΓÇæS2/X TXΓåöRX Loopback Suite

Lightweight DVBΓÇæS2/X transmitterΓåÆreceiver loopback testbench for development and experimentation.

Quickstart
1. Create venv and install:
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
2. Run a loopback:
   python tests/test_tx_rx_loopback.py --max-frames 1 --esn0-db 10
3. Run tests:
   pytest -q

Repository layout
- tx/, rx/, common/ ΓÇö signal chain modules
- tests/ ΓÇö loopback driver and integration tests
- config/, data/ ΓÇö matrices and sample inputs
- docs/, examples/, results/

Contributing, CI and usage examples are in the repo. License: MIT.

# Wi‑Fi Firmware OTA QA (Public‑safe)

Template for validating **over‑the‑air firmware updates** for Wi‑Fi routers/mesh nodes.

## What it shows
- Version check + semantic version validation
- Update/rollback state machine (simulated)
- Negative tests: power loss, network loss (simulated)
- Test plan & KPIs for OTA safety

## Quick start
```bash
pip install -r requirements.txt
python scripts/ota_sim.py --target 2.3.1
pytest -q
```

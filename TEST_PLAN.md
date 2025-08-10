# OTA Test Plan (Generic)

- Pre‑checks: battery/AC, connectivity, storage free
- Update: download, verify checksum/signature, apply
- Reboot & health: boot success, services up, version reported
- Rollback: if health check fails within T seconds
- KPIs: success rate ≥ 99.5%, rollback success 100%, mean update time X±Y

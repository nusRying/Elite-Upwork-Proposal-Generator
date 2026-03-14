name:	nusRying/Snakey-Android
description:	
--
# Snakey Android

Modern Snake.io-style multiplayer game for Android.

## Repo layout

- `client/` ΓÇö Unity 2D project (Android target)
- `server/` ΓÇö Node.js (TypeScript) authoritative server (HTTP + WebSocket)
- `shared/` ΓÇö protocol docs + test vectors
- `docs/` ΓÇö architecture, roadmap, runbooks
- `infra/` ΓÇö local/dev infrastructure (Postgres, server Dockerfile)

## Quick start (server)

1) Start Postgres:

```powershell
docker compose -f infra/docker-compose.yml up -d
```

2) Run the server:

```powershell
cd server
npm install
npm run dev
```

3) Verify health:

```powershell
curl http://localhost:3000/health
```

## Client (Unity)

Unity project scaffolding lives in `client/`. See `docs/RUNBOOK.md` for the pinned Unity version and setup steps.



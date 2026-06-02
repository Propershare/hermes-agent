# Seshat Gateway Bootstrap Contract

Purpose: any agent/LLM entering through the Seshat gateway should be able to discover the lab map, memory locations, governance rules, and reporting protocol without guessing.

Seshat is the project name. Maat Governance is the constitutional/governance layer.

Canonical OpenClaw bootstrap file:

- `C:\Users\imhotepjr\.openclaw\workspace\MAAT-GATEWAY-BOOTSTRAP.md`

## First Files To Read

When an agent enters this machine through OpenClaw or another gateway, read these files first if accessible:

1. `C:\Users\imhotepjr\.openclaw\workspace\AGENTS.md`
2. `C:\Users\imhotepjr\.openclaw\workspace\MEMORY.md`
3. `C:\Users\imhotepjr\.openclaw\workspace\MAAT-LAB-INDEX.md`
4. `C:\Users\imhotepjr\.openclaw\workspace\MAAT-GATEWAY-BOOTSTRAP.md`

## Lab Roots

OpenClaw control root:

- `C:\Users\imhotepjr\.openclaw\workspace`

Maat ecosystem / memory repo:

- `C:\Users\imhotepjr\.openclaw\workspace\maat-ecosystem`
- Remote: `https://github.com/Propershare/maat-ecosystem.git`

Hermes/Maat governance fork:

- `C:\Users\imhotepjr\Projects\maat-governance\hermes-agent`
- Origin: `https://github.com/Propershare/hermes-agent.git`
- Upstream: `https://github.com/NousResearch/hermes-agent.git`
- Active branch: `maat-governance-foundation`

## Memory Rule

Do not assume memory is live just because files exist.

Before reporting live memory/gitMaat capability, verify:

1. Maat memory repo exists.
2. Current memory service/API or CLI entrypoint exists.
3. DB/service connection works without exposing secrets.
4. Read/write test succeeds or fails with a named blocker.

## Status Reporting Rule

Before answering status questions about Maat/Hermes/gitMaat, run live checks when tools are available:

```powershell
git -C C:\Users\imhotepjr\.openclaw\workspace\maat-ecosystem status --short --branch
git -C C:\Users\imhotepjr\.openclaw\workspace\maat-ecosystem remote -v
git -C C:\Users\imhotepjr\Projects\maat-governance\hermes-agent status --short --branch
git -C C:\Users\imhotepjr\Projects\maat-governance\hermes-agent remote -v
```

## Governance Rule

High-risk actions require explicit human permission:

- deleting data
- changing security settings
- exposing secrets
- publishing externally
- spending money
- sending messages as the user
- changing gateway/channel config

## Local Model Rule

Default local model target for Hermes/Maat testing:

- Base URL: `http://127.0.0.1:11434/v1`
- Model: `gemma4:e2b`

One-shot Hermes test:

```powershell
C:\Users\imhotepjr\Projects\maat-governance\run-hermes-gemma4-e2b-once.ps1 "Reply exactly: MAAT_OK"
```

## Expected Agent Behavior

An entering agent should:

1. Read the bootstrap/index files.
2. Verify live paths before claiming access.
3. Use OpenClaw as control plane, not as the only code root.
4. Keep external project roots clean.
5. Report blockers explicitly.
6. Preserve Maat principles: truth, order, balance, justice, reciprocity, self-reflection.

# Maat Desktop Long-Term Memory Quickstart

This guide is for anyone who downloads the Hermes/Maat fork and wants to run a local agent with long-term memory on their own desktop.

The goal: a person should be able to clone the fork, point it at a local model, choose a local memory folder/database, and start building a durable personal/scholar memory without using cloud memory by default.

## What This Provides

A Maat-governed desktop agent should have:

- a local model connection
- a local memory root
- human-readable project notes
- structured long-term memory
- audit logs for important actions
- clear rules for what gets remembered
- clear rules for what must never be stored

## Recommended Desktop Layout

Create a local lab folder outside the repo:

### Windows

```text
C:\Users\YOUR_NAME\MaatLab
C:\Users\YOUR_NAME\MaatLab\memory
C:\Users\YOUR_NAME\MaatLab\memory\semantic
C:\Users\YOUR_NAME\MaatLab\memory\episodic
C:\Users\YOUR_NAME\MaatLab\memory\audit
C:\Users\YOUR_NAME\MaatLab\models
C:\Users\YOUR_NAME\MaatLab\projects
```

### macOS / Linux

```text
~/MaatLab
~/MaatLab/memory
~/MaatLab/memory/semantic
~/MaatLab/memory/episodic
~/MaatLab/memory/audit
~/MaatLab/models
~/MaatLab/projects
```

Keep the repo separate from the memory root. The repo is code. The memory root belongs to the human.

## Step 1 — Clone This Fork

```bash
git clone https://github.com/Propershare/hermes-agent.git
cd hermes-agent
git switch maat-governance-foundation
```

## Step 2 — Install Runtime Dependencies

Hermes uses Python and `uv`.

```bash
uv run python cli.py --help
```

If `uv` is not installed, install it from:

```text
https://docs.astral.sh/uv/getting-started/installation/
```

## Step 3 — Run A Local Model

Recommended first path: Ollama.

Install Ollama:

```text
https://ollama.com/download
```

Pull a small model:

```bash
ollama pull llama3.2:3b
```

Or use another local model you already have.

Ollama exposes an OpenAI-compatible endpoint at:

```text
http://127.0.0.1:11434/v1
```

## Step 4 — Test Hermes Against The Local Model

Example:

```bash
uv run python cli.py \
  --query "Reply exactly: MAAT_OK" \
  --ignore_user_config \
  --max_turns 1 \
  --quiet \
  --model "llama3.2:3b" \
  --provider "custom" \
  --base_url "http://127.0.0.1:11434/v1" \
  --api_key "ollama-local"
```

If it replies `MAAT_OK`, your local model loop works.

## Step 5 — Create A Maat Memory Config

Copy the template:

```bash
cp maat_governance/templates/maat-memory.local.example.yaml maat-memory.local.yaml
```

Edit `maat-memory.local.yaml` and set your own memory root.

Example Windows memory root:

```yaml
memory_root: "C:\\Users\\YOUR_NAME\\MaatLab\\memory"
```

Example macOS/Linux memory root:

```yaml
memory_root: "~/MaatLab/memory"
```

Do not commit your personal memory config if it contains private paths, secrets, or database URLs.

## Step 6 — Memory Types

Maat uses memory classes so agents do not mix everything together.

### Semantic Memory

Durable facts, concepts, user preferences, project knowledge.

Examples:

- preferred local model
- current project root
- trusted source list
- recurring workflow

### Episodic Memory

Session history and summaries.

Examples:

- what happened today
- decisions made in a work session
- blockers found

### Audit Memory

Important actions and tool use.

Examples:

- pushed branch X
- edited config Y
- ran test Z
- asked human for approval before publishing

## Step 7 — What Not To Store

Do not store by default:

- passwords
- API keys
- private tokens
- full private conversations unless explicitly allowed
- financial details unless needed and approved
- medical/legal sensitive data unless the human explicitly opts in

If uncertain, summarize instead of copying raw private data.

## Step 8 — The Gateway Bootstrap Contract

Agents entering the gateway should read:

```text
docs/MAAT-GATEWAY-BOOTSTRAP.md
```

That file teaches an agent how to discover:

- lab roots
- memory roots
- governance rules
- live status checks
- local model target
- when to ask the human before acting

## Step 9 — First Scholar Memory Pattern

A scholar agent should have its own memory namespace.

Example:

```yaml
scholar_id: kemetic-history-scholar
memory_namespace: scholars/kemetic-history
```

This prevents one expert’s memory from contaminating another expert’s work.

## Step 10 — Desktop Memory Health Check

Before claiming memory is connected, an agent should verify:

1. memory root exists
2. config file exists
3. read test succeeds
4. write test succeeds
5. audit log can append a line
6. no secrets were printed

If any step fails, report the exact blocker.

## Current Status

This quickstart documents the target desktop memory contract. The next implementation milestone is to add a small `maat memory doctor` command that checks the local memory root and writes a safe test audit event.

# Maat Gateway Framework

The gateway is the first real milestone for the Hermes/Maat fork.

It should sit between humans, models, tools, memory, and specialist agents. Its job is to route work while enforcing Maat governance.

## Required Components

### 1. Agent Registry

A registry of named expert agents.

Each entry should include:

- id
- display name
- domain
- default model
- allowed tools
- denied tools
- memory namespace
- governance profile
- evaluation suite

### 2. Model Router

Routes requests to local or remote models.

Initial local target:

```yaml
provider: ollama
base_url: http://127.0.0.1:11434/v1
model: gemma4:e2b
```

Routing criteria:

- privacy sensitivity
- task complexity
- required context length
- cost
- latency
- whether citations/tool use are needed

### 3. Tool Permission Layer

Before a tool runs, the gateway checks:

- agent role
- requested action
- risk level
- user approval state
- target path/system

### 4. Memory Boundary Layer

Default: each scholar has separate memory.

Shared memory requires explicit declaration.

Memory classes:

- session memory
- project memory
- scholar memory
- human preference memory
- audit memory

### 5. Audit Log

Important actions should record:

- timestamp
- agent id
- user/request source
- intent
- tool/action
- risk class
- approval status
- result

### 6. Evaluation Harness

Before trusting a scholar, test it.

Each scholar should have:

- canonical questions
- adversarial questions
- citation checks
- refusal/uncertainty checks
- tool safety checks

## First Prototype Scholar

Recommended first scholar:

```yaml
id: kemetic-history-scholar
name: Kemetic History Scholar
model: gemma4:e2b
domain: Kemetic/African historical research
requires_citations: true
forbidden: unsupported claims, invented sources, Eurocentric framing as default
```

## Implementation Order

1. Document schemas for agent registry and governance profiles.
2. Create a minimal YAML registry.
3. Add a router shim that can call Ollama through OpenAI-compatible `/v1/chat/completions`.
4. Add audit logging to local JSONL.
5. Run one scholar prototype through evals.
6. Only then consider fine-tuning or phone deployment.

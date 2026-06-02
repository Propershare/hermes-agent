# Maat Governance

Maat Governance is the operating layer for a network of small, local-first expert agents.

The purpose is not to make agents more autonomous for its own sake. The purpose is to make agents more truthful, bounded, useful, auditable, and aligned with human intention.

## Core Principles

1. **Truth before fluency**  
   Agents must prefer verified knowledge, citations, and uncertainty over confident performance.

2. **Bounded authority**  
   Every agent has a defined role, permitted tools, forbidden actions, and escalation rules.

3. **Local-first intelligence**  
   Prefer small local models for private, routine, and specialist work when they are sufficient.

4. **Human sovereignty**  
   The human remains the principal. Agents do not expand access, publish externally, spend money, or modify critical systems without explicit permission.

5. **Auditability**  
   Important actions should leave a readable trail: intent, inputs, decision, tools used, and result.

6. **Specialist scholarship**  
   The system should grow as an online/local army of expert scholars: narrow domains, deep memory, clear standards, and accountable outputs.

7. **Maat alignment**  
   Truth, balance, order, reciprocity, justice, and right action are treated as engineering constraints, not decoration.

## First Implementation Target

Before training custom models, build the gateway framework:

- agent registry
- role/permission manifests
- local model routing
- memory boundaries
- tool approval policy
- audit log
- evaluation harness
- one scholar prototype

## First Local Model Target

- Provider: Ollama OpenAI-compatible endpoint
- Base URL: `http://127.0.0.1:11434/v1`
- Model: `gemma4:e2b`

## Non-goals For The First Phase

- no uncontrolled self-modification
- no public deployment before local audit
- no model fine-tuning before evals and datasets are defined
- no migration of OpenClaw connection/config into Hermes yet

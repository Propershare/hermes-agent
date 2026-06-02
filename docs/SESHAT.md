# Seshat

Seshat is a Maat-governed framework for local-first expert agents and long-term desktop memory.

It begins as a fork of Hermes Agent and grows toward a network of small specialist scholars that can run locally, on modest hardware, and eventually on phone-class devices.

## Name

Seshat is the Kemetic keeper of writing, measurement, records, architecture, knowledge, and sacred calculation.

For this project, **Seshat** means:

- memory with structure
- scholarship with evidence
- agents with boundaries
- local intelligence with audit trails
- scientific method made practical
- a living library of expert workers

## Relationship To Maat Governance

Seshat is the project/product name.

Maat Governance is the constitutional layer underneath it:

- truth before fluency
- bounded authority
- human sovereignty
- auditability
- memory boundaries
- local-first intelligence
- justice, balance, order, reciprocity, and self-reflection

## Mission

Build an online and local army of small expert scholars in their fields.

Each scholar should have:

- a defined domain
- a memory namespace
- source/citation rules
- allowed and denied tools
- evaluation tests
- a governance profile
- a local model target when possible

## First Milestone

The first milestone is the gateway framework:

1. agent registry
2. governance profile loader
3. local model router
4. desktop memory connector
5. audit log
6. scholar eval harness
7. first scholar prototype

## First Scholar Prototype

Initial prototype:

```yaml
id: kemetic-history-scholar
name: Kemetic History Scholar
model: gemma4:e2b
requires_citations: true
memory_namespace: scholars/kemetic-history
```

## Local Model Target

Initial local test target:

```yaml
provider: ollama
base_url: http://127.0.0.1:11434/v1
model: gemma4:e2b
```

## Desktop Memory

Start here:

- [`MAAT-DESKTOP-MEMORY-QUICKSTART.md`](MAAT-DESKTOP-MEMORY-QUICKSTART.md)
- [`MAAT-GATEWAY-BOOTSTRAP.md`](MAAT-GATEWAY-BOOTSTRAP.md)

The goal is for anyone downloading the fork to turn it on, connect a long-term memory on their desktop, and begin growing bounded local scholars.

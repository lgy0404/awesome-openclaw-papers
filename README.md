# Awesome OpenClaw Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of academic papers, technical reports, and research related to [OpenClaw](https://github.com/openclaw/openclaw) — the open-source, self-hosted AI assistant platform.

OpenClaw is an open-source personal AI agent that runs on your own devices and connects to 50+ messaging platforms. It supports multiple LLM backends (Claude, GPT, Gemini, local models), features a modular skill system with 5,700+ community-maintained skills, and implements advanced memory architecture for persistent context.

This repository tracks the latest academic research around OpenClaw to promote community development and facilitate knowledge sharing.

---

## Contents

- [Core Framework](#core-framework)
- [Reinforcement Learning & Training](#reinforcement-learning--training)
- [Security & Safety](#security--safety)
- [Multi-Agent Systems & Scientific Research](#multi-agent-systems--scientific-research)
- [Benchmark & Evaluation](#benchmark--evaluation)
- [Memory & Architecture](#memory--architecture)
- [Skills & Tool Use](#skills--tool-use)
- [Blog Posts & Technical Articles](#blog-posts--technical-articles)
- [Related Projects](#related-projects)

---

## Core Framework

- **OpenClaw: Your Own Personal AI Assistant** — The official OpenClaw project providing a self-hosted, model-agnostic AI agent platform with Gateway architecture, agentic loop, and modular skill system. [[GitHub]](https://github.com/openclaw/openclaw) [[Docs]](https://docs.openclaw.ai)

## Reinforcement Learning & Training

- **OpenClaw-RL: Train Any Agent Simply by Talking** — Presents a framework enabling agents to improve through natural conversation by leveraging next-state signals (user replies, tool outputs, state changes) as training data. Introduces extractive rewards via PRM judge and Hindsight-Guided On-Policy Distillation. Supports personal conversations, terminal execution, GUI interactions, and software engineering tasks within a unified framework. [[arXiv, Mar 2026]](https://arxiv.org/abs/2603.10165)

## Security & Safety

- **From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent** — Proposes the Personalized Agent Security Bench (PASB) framework, identifying critical vulnerabilities across prompt processing, tool usage, and memory retrieval stages. [[arXiv, Feb 2026]](https://arxiv.org/abs/2602.08412)

- **Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats** — Provides a comprehensive five-layer lifecycle security framework analyzing threats including indirect prompt injection, supply chain contamination, memory poisoning, and intent drift. [[arXiv, Mar 2026]](https://arxiv.org/abs/2603.11619)

- **A Trajectory-Based Safety Audit of Clawdbot (OpenClaw)** — Evaluates the system across six risk dimensions, revealing non-uniform safety profiles with failures particularly under underspecified intent and adversarial steering. [[arXiv, Feb 2026]](https://arxiv.org/abs/2602.14364)

## Multi-Agent Systems & Scientific Research

- **From Agent-Only Social Networks to Autonomous Scientific Research: Lessons from OpenClaw and Moltbook** — Examines OpenClaw's ecosystem alongside the Moltbook agent-only social network. Presents ClawdLab and Beach.Science platforms for autonomous scientific research using multi-agent architectures with governance structures and verification mechanisms. [[arXiv, Feb 2026]](https://arxiv.org/abs/2602.19810)

## Benchmark & Evaluation

- **Claw-Eval** — An evaluation harness for assessing LLMs as agents, featuring 104 human-verified tasks across 15 services with Docker sandboxes and robust grading. Provides a live leaderboard and transparent benchmarking. [[GitHub]](https://github.com/claw-eval/claw-eval)

- **PinchBench** — A real-world benchmarking system for evaluating LLM models as OpenClaw coding agents, with 23 tasks spanning productivity, research, writing, coding, analysis, email, memory, and skills categories. [[GitHub]](https://github.com/pinchbench/skill)

- **ClawBench** — A deterministic, scenario-based evaluation platform for OpenClaw agents using fixed fixtures and regex-based scoring without LLM judge costs. [[GitHub]](https://github.com/trajectoryRL/clawbench)

## Memory & Architecture

- **Workspace Memory Research** — Proposes an offline-first memory architecture using Markdown as the canonical source with a derived SQLite index for entity-centric retrieval, temporal queries, and confidence-bearing opinions that evolve with evidence. [[Docs]](https://docs.openclaw.ai/experiments/research/memory)

## Skills & Tool Use

- **memory-tools Skill** — Agent-controlled memory management with confidence scoring, semantic search, and temporal decay. Provides six memory tools: `memory_store`, `memory_update`, `memory_forget`, `memory_search`, `memory_summarize`, and `memory_list`. [[Playbooks]](https://playbooks.com/skills/openclaw/skills/memory-tools)

## Blog Posts & Technical Articles

- [How OpenClaw Works: Understanding AI Agents Through a Real Architecture](https://bibek-poudel.medium.com/how-openclaw-works-understanding-ai-agents-through-a-real-architecture-5d59cc7a4764) — Deep dive into OpenClaw's Gateway, agentic loop, and tool use patterns.
- [How OpenClaw Remembers: A Deep Dive into AI Agent Memory Architecture](https://avasdream.com/blog/openclaw-memory-system-deep-dive) — Explores the two-layer memory system with daily notes and long-term memory.
- [OpenClaw Architecture Guide 2026: Memory, Scaling & Setup](https://rentierdigital.xyz/blog/openclaw-architecture-scaling-guide) — Comprehensive guide on memory organization, scaling strategies, and deployment.
- [When AI Gets Physical Hands: A Review of OpenClaw on the Unitree G1 and Other Robots](https://evoailabs.medium.com/when-ai-gets-physical-hands-a-review-of-openclaw-on-the-unitree-g1-and-other-robots-0fbf06a1d4c8) — Review of OpenClaw's integration with robotic systems.

## Related Projects

| Project | Description | Link |
|---------|-------------|------|
| OpenClaw | The official open-source AI assistant platform | [GitHub](https://github.com/openclaw/openclaw) |
| Claw-Eval | LLM agent evaluation harness | [GitHub](https://github.com/claw-eval/claw-eval) |
| PinchBench | Real-world LLM agent benchmark | [GitHub](https://github.com/pinchbench/skill) |
| ClawBench | Deterministic scenario-based evaluation | [GitHub](https://github.com/trajectoryRL/clawbench) |

---

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

To add a paper, please ensure:
- The paper is directly related to OpenClaw or its ecosystem
- Include the paper title, authors (optional), a brief description, and a link
- Place the paper in the appropriate category
- Follow the existing format

## Star History

If you find this repository useful, please consider giving it a star ⭐ to help others discover it!

## License

[CC0 1.0 Universal](LICENSE)

# Project Name

Multi-Agent Trading Intelligence System

## Team Members

- Sanjana Uppalike - suppa17
- Pranathi Kamisetty - Pkami
- Sai Teja Aggunna - Saggu

## Description

This project implements a **multi-agent trading intelligence system** that analyzes financial markets using specialized agents and combines their reasoning into a unified, explainable trading decision.

Instead of relying on a single model or a single source of information, the system decomposes the problem into multiple **signal-specific agents**, where each agent is responsible for a different dimension of market analysis. The current system includes:
- a **Technical Analyst** for price- and momentum-based signals,
- a **Fundamental Analyst** for company financial health and long-term valuation signals,
- a **News + Sentiment Analyst** for external information flow using recency-weighted news and sentiment analysis.

These agents run in parallel and feed into a **Chain-of-Thought (CoT) Synthesis Agent**, which aggregates their outputs, identifies agreement or conflict across signals, and produces a final interpretable market view.

The broader target architecture also includes memory, debate, risk management, trader decisioning, and reflection layers for building a more robust and adaptive trading pipeline.

## Architecture

### Architecture Diagram

<!-- Insert architecture image here -->
![Architecture Diagram](path/to/architecture-image.png)

### High-Level Architecture

```text
Input Ticker
    │
    ▼
Memory Agent
    │
    ▼
Parallel Analyst Layer
    ├── Technical Analyst
    ├── Fundamental Analyst
    └── News + Sentiment Analyst
    │
    ▼
CoT Synthesis Agent
    │
    ▼
Debate Layer
    ├── Bull Researcher
    ├── Bear Researcher
    └── Neutral Arbiter
    │
    ▼
Trader Agent + Risk Manager
    │
    ▼
Reflection + Memory Update
```

## Current Implementation

The following components are currently implemented:

### Technical Analyst
- fetches historical market data
- computes indicators such as RSI, MACD, Bollinger Bands, VWAP, and volume-based signals
- generates a technical analysis report using an LLM

### Fundamental Analyst
- fetches structured company data from EDGAR
- analyzes revenue, earnings, assets, liabilities, and equity trends
- generates a fundamental analysis report using an LLM

### News + Sentiment Analyst
- uses Alpha Vantage news sentiment data
- applies recency weighting so newer news has more impact
- aggregates sentiment across articles
- generates a combined external-signal report using an LLM

### CoT Synthesis Agent
- combines outputs from all currently implemented analyst agents
- produces a final synthesis across technical, fundamental, and news/sentiment signals

### Parallel Execution with LangGraph
- analyst agents are executed concurrently
- outputs are routed into the synthesis layer

## Future Implementations

The following components are planned as part of the full architecture:

### Memory Agent
- retrieves past decisions and outcomes for the same ticker
- injects relevant historical context into the pipeline

### Debate Layer
- Bull Researcher
- Bear Researcher
- Neutral Arbiter to score and resolve conflicting views

### Trader Agent
- converts synthesized reasoning into a final rating such as Buy, Hold, or Sell
- assigns a conviction score

### Risk Manager
- evaluates market regime and volatility conditions
- adjusts final recommendations based on risk context

### Reflection Agent
- evaluates post-decision outcomes after a fixed horizon
- generates post-mortem analysis
- updates long-term memory for future runs

### Persistence and API Layer
- decisions database
- history endpoint
- scheduler for multi-ticker watchlists
- notification and monitoring support

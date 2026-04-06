# # # tradingagents_v2/agents/synthesis/cot_synthesis.py

# # def run_cot_synthesis(state: dict, config: dict = None) -> dict:
# #     ticker = state["ticker"]
# #     tech   = state.get("technical_report", "")
# #     fund   = state.get("fundamental_report", "")

# #     separator = "=" * 60

# #     output = f"""
# # {separator}
# #  ANALYST RESULTS — {ticker}
# # {separator}

# # --- TECHNICAL ANALYST ---
# # {tech}

# # --- FUNDAMENTALS ANALYST ---
# # {fund}

# # {separator}
# # """
# #     print(output)
# #     return {"synthesis_output": output}

# from llm_clients.factory import get_llm

# SYSTEM_PROMPT = """You are a senior investment strategist.

# You will receive reports from multiple analysts.
# Your job is to:

# 1. Extract each analyst's conclusion (bullish / bearish / neutral)
# 2. Compare their reasoning
# 3. Resolve conflicts
# 4. Produce a final unified view

# Return structured output:
# - Technical summary
# - Fundamental summary
# - Synthesis
# - Final bias
# - Suggested action
# - Risk notes
# """

# def run_cot_synthesis(state: dict, config: dict = None) -> dict:
#     ticker = state["ticker"]
#     tech   = state.get("technical_report", "")
#     fund   = state.get("fundamental_report", "")

#     llm = get_llm(config)

#     prompt = f"""
# Ticker: {ticker}

# TECHNICAL ANALYST REPORT:
# {tech}

# FUNDAMENTAL ANALYST REPORT:
# {fund}

# Synthesize these into a final investment view.
# """

#     response = llm.invoke([
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": prompt},
#     ])

#     return {"synthesis_output": response.content}



from llm_clients.factory import get_llm

SYSTEM_PROMPT = """You are a senior market strategist.

You are given three analyst reports:
1. Technical analyst
2. Fundamental analyst
3. News + sentiment analyst

Your job is to:
1. Summarize each analyst briefly
2. Identify agreement and disagreement across them
3. Decide the overall market bias: bullish / bearish / neutral
4. State confidence: high / medium / low
5. Mention the key risks and uncertainty
6. Give a final actionable view for a trader

Return the answer in this exact structure:

## Technical View
## Fundamental View
## News + Sentiment View
## Cross-Analyst Synthesis
## Final Bias
## Confidence
## Key Risks
## Actionable Takeaway

Be specific and concise. Reference actual signals when possible.
"""


def run_cot_synthesis(state: dict, config: dict = None) -> dict:
    ticker = state["ticker"]

    tech = state.get("technical_report", "")
    fund = state.get("fundamental_report", "")
    news_sentiment = state.get("news_sentiment_report", "")

    llm = get_llm(config or {})

    prompt = f"""Ticker: {ticker}

TECHNICAL ANALYST REPORT:
{tech}

FUNDAMENTAL ANALYST REPORT:
{fund}

NEWS + SENTIMENT ANALYST REPORT:
{news_sentiment}

Synthesize these into one final view.
"""

    response = llm.invoke([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ])

    return {"synthesis_output": response.content}
# Nacelle Board Roadmap 🗺️

This document outlines planned improvements to the Nacelle Board engine to increase its resilience, cost-efficiency, and versatility.

## 🚀 Upcoming Features

### 1. Model Fallback Logic (Feature #2)
Currently, if a provider like Groq or OpenAI experiences downtime or rate-limiting, the agent execution fails. We plan to implement a "Fail-Safe" mechanism.
- **Priority:** High
- **Implementation:** Use LangChain's `.with_fallbacks()` method.
- **Benefit:** 99.9% uptime for agent runs. If the cheap model fails, the system automatically swaps to a more robust one.

### 2. Local LLM Support via Ollama (Feature #3)
To reduce API costs and improve privacy for sensitive store data, we will integrate support for local models.
- **Priority:** Medium
- **Implementation:** Add an `ollama` provider type to the `ModelFactory`.
- **Benefit:** $0 per token for tasks that don't require high-level reasoning (like basic data cleaning or formatting).

### 3. Usage & Cost Tracking
Implementation of a dashboard or log that calculates the cost of each "Kickoff" based on the tokens used by each specific provider.

### 4. Custom Tool Library
Expansion of the `tools/` directory to include:
- **ShopifyAdminTool:** To write back metadata or update tags.
- **CompetitorPriceScraper:** To compare store prices with the wider market.

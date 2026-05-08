# Nacelle Board 🚀

Nacelle Board is an agentic merchandising and growth engine designed for boutique e-commerce stores. It uses a "Crew" of AI agents to audit inventories, strategize growth, and scout brand opportunities.

## 🏗 Project Structure

```text
nacelle-board/
├── agents/            # AI Agent definitions (CrewAI)
├── tools/             # Custom tools for agents (Shopify JSON, Web Crawlers)
├── config/            # Store-specific configurations
│   ├── schemas.py     # Pydantic data models for validation
│   └── store_config.yaml
├── main.py            # Entry point to launch the crew
└── .env               # Secret keys (ignored by git)
```

## ✨ Features
- **Multi-Model Registry:** Mix and match OpenAI, Groq, and Gemini agents in a single run.
- **Strict Validation:** Pydantic-powered configuration ensures the engine never boots with a broken flight plan.
- **Modular Design:** Agents are decoupled from their LLM brains for maximum flexibility.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- A virtual environment (recommended)

### 2. Installation
```bash
# Create and activate venv
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
1. **API Keys:** Copy `.env.example` to `.env` and add your API keys.
   ```bash
   cp .env.example .env
   ```
2. **Store Settings:** Copy `config/store_config.yaml.example` to `config/store_config.yaml` and update it with your store's URL and niche.

### 4. Run the Engine
```bash
python main.py
```

## 🛡 Security
- `.env` and `config/store_config.yaml` are ignored by Git.
- Use the `.example` files as templates for your local setup.

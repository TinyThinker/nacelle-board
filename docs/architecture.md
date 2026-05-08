# System Architecture 🏗️

Nacelle Board is built on a **Modular Dependency Injection** architecture. It separates the "Identity" of the AI Agent from the "Brain" (LLM) it uses, allowing for a highly flexible and cost-effective system.

## 🧱 Core Components

### 1. Configuration Layer (`store_config.yaml`)
The "Source of Truth" for the entire system.
- **Store Data:** Metadata about the e-commerce target.
- **Model Registry:** A list of available LLM providers and their hyperparameters.
- **Agent Mapping:** A dictionary that assigns specific models to specific agent roles.

### 2. Validation Engine (`config/schemas.py`)
Driven by **Pydantic**, this layer defines the strict data models for the store and its models. It ensures that the YAML configuration is perfectly formatted before the engines start, preventing mid-run crashes and providing clear developer feedback.

### 3. The Model Factory
A centralized dispatch system that translates YAML model keys (e.g., `fast`, `creative`) into live, authenticated LangChain objects (`ChatGroq`, `ChatOpenAI`, etc.).

### 4. Agentic Logic (`agents/`)
Independent modules defined using the **CrewAI** framework. Each agent:
- Is role-based (e.g., Inventory Director).
- Receives its LLM instance via injection from `main.py`.
- Has access to specific tools (e.g., `WebsiteSearchTool`).

## 🔄 Execution Flow

1.  **Bootstrapping:** `main.py` loads `.env` secrets and validates `store_config.yaml` using the Pydantic models defined in `config/schemas.py`.
2.  **Model Instantiation:** The Model Factory creates the necessary LLM instances for the assigned agents.
3.  **Agent Assembly:** Agents are initialized with their injected LLMs and Tools.
4.  **Task Definition:** Objectives are linked to specific agents.
5.  **Kickoff:** The `Crew` orchestrates the agents, handling communication and task handoffs until the final report is generated.

## 🛡️ Security & Privacy
- **Separation of Secrets:** API keys are never stored in the config; they live in `.env`.
- **Private Configs:** Both `.env` and `store_config.yaml` are excluded from version control to protect proprietary store strategies.

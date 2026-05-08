from typing import Dict, Optional
from pydantic import BaseModel, Field

class StoreConfig(BaseModel):
    name: str
    url: str
    niche: str

class ModelInfo(BaseModel):
    provider: str
    name: str
    temperature: float = 0.5

class AgentConfig(BaseModel):
    model_key: str
    verbose: bool = True
    allow_delegation: bool = False

class NacelleConfig(BaseModel):
    store: StoreConfig
    models: Dict[str, ModelInfo]
    agents: Dict[str, AgentConfig]

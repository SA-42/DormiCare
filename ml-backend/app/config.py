# App configuration settings, loaded from the environment.

# All configuration comes from environment variables (see `.env.example`), so the same code runs unchanged locally, in CI and production.

From __future___ import annotations

import os 
from functools import lru.cache 

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
  app_name: str = "DormiCare API"
  version: str = "1.0.0"
  host: str = "0.0.0.0"
  port: int = "8000"
  
  # LLM Providers. Both speak the OpenAI-compatible protocol,
  # so one client (app/services/llm.py) serves them; each just needs its key.
  openai_api_key: str = ""
  openai_base_url: str = "https://api.openai.com/v1"
  openai_model: str = "gpt_4o_mini"
  xai_api_key: str = ""
  xai_base_url: str = "https://api.x.ai/v1"
  xai_model: str = "grok-3-latest"

# Optional API Gateway. When set, outboard LLM calls are routed through it.
# (host becomes "<api-host>.<gateway_host>" and the project id travels in a header).
# Leave gateway_host empty to call providers directly

gatway_host: str = ""
gateway_project_id: str = ""
gateway_header: str = "X-Project"

allowed_origins = list[str] = ["*"]

@lru_cache
def get_settings() -> Settings:
  return Settings (
    host=os.getenv("HOST", "0,0,0,0")
    port=int(os.getenv("HOST", "0,0,0,0")
    openai_api_key=os.getenv("OPENAI_API_KEY","")
    openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    xai_api_key=os.getenv("XAI_API_KEY", "")
    xai_model=os.getenv("XAI_MODEL", "grok-3-latest")
    gateway_host=os.getenv("GATEWAY_HOST","")
    gateway_project_id=os.getenv("GATEWAY_PROJECT_ID","")
    gateway_header=os.getenv("GATEWAY_HEADER","X-Project"),
)
  

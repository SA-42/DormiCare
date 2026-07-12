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

# Optional API Gateway

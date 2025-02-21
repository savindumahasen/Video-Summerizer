import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini 
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file
import google.generativeai as genai


import time
from pathlib import Path


import tempfile as tf

from dotenv import load_dotenv
load_dotenv()

import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)


## Page configuration

st.set_page_config(
    page_title="Multimodel AI",
    page_icon="",
    layout="wide"
)

st.title("Video Summerizer AI agent")

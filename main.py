import yaml
import os
from agents.product_specialist import create_product_agent, create_product_task
from crewai import Crew
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()

def load_config():
    with open("config/store_config.yaml", "r") as file:
        return yaml.safe_load(file)

def get_llm_for_agent(config, agent_key):
    """
    Retrieves the correct LLM instance based on the agent's configuration.
    """
    agent_config = config['agents'].get(agent_key)
    if not agent_config:
        return None
        
    model_key = agent_config.get('model_key')
    model_info = config['models'].get(model_key)
    
    if not model_info:
        return None
        
    provider = model_info['provider']
    name = model_info['name']
    temp = model_info.get('temperature', 0.5)
    
    if provider == "groq":
        return ChatGroq(model=name, temperature=temp)
    elif provider == "gemini":
        return ChatGoogleGenerativeAI(model=name, temperature=temp)
    elif provider == "openai":
        return ChatOpenAI(model=name, temperature=temp)
    
    return None

def run_nacelle_board():
    # 1. Load the "Flight Plan" from YAML
    config = load_config()
    store_url = config['store']['url']
    store_name = config['store']['name']
    
    print(f"### NACELLE BOARD: INITIALIZING ENGINES FOR {store_name.upper()} ###")

    # 2. Get the specific LLM for the Product Specialist
    product_llm = get_llm_for_agent(config, 'product_specialist')

    # 3. Initialize the Product Agent using config data and assigned LLM
    merchandiser = create_product_agent(store_url, product_llm)

    # 4. Define the Mission
    analysis_task = create_product_task(merchandiser)

    # 5. Fire up the Crew
    nacelle_crew = Crew(
        agents=[merchandiser],
        tasks=[analysis_task],
        verbose=config['agents']['product_specialist']['verbose']
    )

    result = nacelle_crew.kickoff()
    
    print("\n\n###############################")
    print(f"## {store_name.upper()} PRODUCT REPORT ##")
    print("###############################\n")
    print(result)

if __name__ == "__main__":
    run_nacelle_board()
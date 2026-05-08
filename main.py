import yaml
import os
from agents.product_specialist import create_product_agent, create_product_task
from crewai import Crew
from dotenv import load_dotenv

load_dotenv()

def load_config():
    with open("config/store_config.yaml", "r") as file:
        return yaml.safe_load(file)

def run_nacelle_board():
    # 1. Load the "Flight Plan" from YAML
    config = load_config()
    store_url = config['store']['url']
    store_name = config['store']['name']
    
    print(f"### NACELLE BOARD: INITIALIZING ENGINES FOR {store_name.upper()} ###")

    # 2. Initialize the Product Agent using config data
    merchandiser = create_product_agent(store_url)

    # 3. Define the Mission
    analysis_task = create_product_task(merchandiser)

    # 4. Fire up the Crew
    nacelle_crew = Crew(
        agents=[merchandiser],
        tasks=[analysis_task],
        verbose=config['agents']['verbose']
    )

    result = nacelle_crew.kickoff()
    
    print("\n\n###############################")
    print(f"## {store_name.upper()} PRODUCT REPORT ##")
    print("###############################\n")
    print(result)

if __name__ == "__main__":
    run_nacelle_board()
from crewai import Agent, Task
from crewai_tools import WebsiteSearchTool

def create_product_agent(store_url, llm):
    # Constructing the structured data endpoint
    json_endpoint = f"{store_url.rstrip('/')}/collections/all/products.json"
    
    # Tool for the agent to 'read' the inventory
    product_tool = WebsiteSearchTool(website_url=json_endpoint)

    return Agent(
        role='Inventory & Merchandising Director',
        goal=f'Perform a deep-dive audit of the product catalog at {store_url}.',
        backstory="""You are a high-level retail consultant. Your specialty is 
        analyzing boutique inventories to find the 'hidden gems' and identifying 
        where a store is missing out on higher margins.""",
        tools=[product_tool],
        llm=llm,
        verbose=True
    )

def create_product_task(agent):
    return Task(
        description="Analyze the product data to find: 1. Price outliers, 2. The most 'complete' product line, and 3. A recommendation for a 3-item starter bundle.",
        expected_output="A structured Merchandising Strategy report.",
        agent=agent
    )
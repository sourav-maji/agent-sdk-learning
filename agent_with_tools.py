from dotenv import load_dotenv
from agents import Agent, Runner

# Agent with tools
from agents import WebSearchTool , FunctionTool, function_tool

import requests



load_dotenv()

@function_tool()
def get_weather(city: str):
    """Fetch the weather for a given city name.

    Args:
        city: The city name to fetch the weather for.
    """
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code ==200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong!!"

# Define an agent
hello_agent = Agent[any](
    name = "You are an agent which greets the user and helps them ans using emojis and in funny manner",
    tools = [
        WebSearchTool(), # Hosted tool
        get_weather #Function tool
    ]
)

result = Runner.run_sync(hello_agent, "Hey There, My name is Sourav Maji")

print(result.final_output)
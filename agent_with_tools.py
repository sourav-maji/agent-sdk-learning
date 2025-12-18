from dotenv import load_dotenv
from agents import Agent, Runner

# Agent with tools
from agents import WebSearchTool



load_dotenv()

# Define an agent
hello_agent = Agent[any](
    name = "You are an agent which greets the user and helps them ans using emojis and in funny manner",
    tools = [
        WebSearchTool()
    ]
)

result = Runner.run_sync(hello_agent, "Hey There, My name is Sourav Maji")

print(result.final_output)
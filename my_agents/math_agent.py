from agents import Agent, ModelSettings
from my_config.gemini_config import GEMINI_MODEL
from my_tools.math_tools import addition, subtract, multiply, division
from my_tools.user_data import fetch_user_data, fetch_user_data_by_id
from agents.agent import StopAtTools


# Define the primary Math Agent
# - Acts like a "Math Teacher" who explains problems step by step.
# - Uses tools for arithmetic operations and user data fetching.
gemini_agent = Agent(
    name="Math Teacher",
    instructions=(
        "You are a helpful and patient Math Teacher Assistant. "
        "Your job is to guide students in solving math problems, "
        "explaining each step clearly and in simple language."
        "just giving the final answer."
    ),
    model=GEMINI_MODEL,
    tools=[addition, subtract, multiply, fetch_user_data, fetch_user_data_by_id]
)


# Define a Simple Agent that can also use the Math Agent as a tool
# - Demonstrates agent composition: one agent can use another as a tool.
# - Also directly includes individual tools (like `addition`) if needed.
simple_agent = Agent(
    name="Chaman Lal",
    instructions=("You are a helpful assistant"),
    model=GEMINI_MODEL,
    tools=[
        gemini_agent.as_tool(
            tool_name="Math_agent",
            tool_description="This is a Math Teacher tool that solves and explains math problems."
        ),
        addition  # Directly include a standalone math tool as well
    ],
    
    # Control how tool calls are handled:
    # tool_use_behavior="run_llm_again"         → after using a tool, send result back to LLM for further reasoning
    # tool_use_behavior="stop_on_first_tool"    → stop execution once the first tool is used
    tool_use_behavior=StopAtTools(stop_at_tool_names=[multiply]),
    # → stop execution specifically when the `multiply` tool is called
   # model_settings=ModelSettings(tool_choice="required")
    model_settings=ModelSettings(tool_choice="Multiply", parallel_tool_calls=True), # it only multiplies the input ex: 2+5 = ans should be 7 but it multiplies 2*5 = 10
    #reset_tool_choice=False   # it will call tool max 10 times then execute it
    # in runner main.py file we can add (max_turns = 5) 
    reset_tool_choice=True # by default it true.  # it takes dicision
)

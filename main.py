from agents import Runner, set_tracing_disabled
from my_agents.math_agent import gemini_agent, simple_agent

# Disable tracing for cleaner output
set_tracing_disabled(True)

# Run the agent synchronously
result = Runner.run_sync(
    starting_agent=simple_agent,
    input="2+2?"
)

# Print the agent's final output
print("\n=== Agent Response ===")
print(result.final_output)

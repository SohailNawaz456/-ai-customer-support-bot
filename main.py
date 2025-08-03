# ===============================
# 🆕 Commit: feat(agent-handoff): 
# Add smart triage agent with auto-routing 
# to Billing 🧾 and Refund 💸 agents based on user queries
# ===============================

from connection import config
from agents import Agent, Runner
import asyncio
import rich

# 💰 Billing Agent – Handles billing-related queries only
billing_agent = Agent(
    name="Billing Agent",
    instructions="Ap sirf billing se related sawalon ke jwab denge."
)

# 💸 Refund Agent – Handles refund processing only
refund_agent = Agent(
    name="Refund Agent",
    instructions="Ap sirf refund process karne mein madad karenge."
)

# 🤖 Triage Agent – Reads user input and routes to correct agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="Ap user ki request parhen aur decide karen ke kis agent ko kaam dena hai.",
    handoffs=[billing_agent, refund_agent]
)

# 🚀 Main async function to run the handoff logic
async def main():
    # ✉️ Example input (change this to test different queries)
    user_input = "Why is my bill so high?"

    # 🧠 Let triage agent decide the handoff
    result = await Runner.run(
        triage_agent,
        user_input,
        run_config=config
    )

    # 🖨️ Print the final response
    rich.print(result.final_output)

# 🏁 Start the async event loop
if __name__ == "__main__":
    asyncio.run(main())

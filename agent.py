import json
from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a college fee assistant. "
    "Never guess a fee: always use get_course_fee. "
    "Use calculator for any arithmetic. "
    "Available course codes: CS101, AI202, DS303. "
    "If no tool is needed, answer directly."
)


def agent(question, max_steps=6, verbose=True):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        # 1. Ask the LLM what to do next
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        # 2. If no tool is requested, return the final answer
        if not message.tool_calls:
            return (message.content or "").strip()

        # Add assistant's tool request to conversation
        assistant_tool_calls = []

        for call in message.tool_calls:

            # Fix Groq's occasional extra text in tool name
            clean_name = call.function.name.split("<|")[0].strip()

            assistant_tool_calls.append(
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": clean_name,
                        "arguments": call.function.arguments
                    }
                }
            )

        messages.append(
            {
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": assistant_tool_calls
            }
        )

        # 3. Execute each requested tool
        for call in message.tool_calls:

            # Clean the tool name
            name = call.function.name.split("<|")[0].strip()

            # Read arguments
            try:
                arguments = json.loads(
                    call.function.arguments or "{}"
                )
            except json.JSONDecodeError:
                arguments = {}

            # Find the function
            function = TOOL_FUNCTIONS.get(name)

            if function:
                try:
                    result = function(**arguments)
                except Exception as e:
                    result = f"Tool error: {e}"
            else:
                result = f"Unknown tool: {name}"

            # Show agent trace
            if verbose:
                print(
                    f"   step {step}: "
                    f"{name}({arguments}) -> {result}"
                )

            # Send tool result back to LLM
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                }
            )

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:

        print("Q:", question)

        print("A:", agent(question))

        print("-" * 70)
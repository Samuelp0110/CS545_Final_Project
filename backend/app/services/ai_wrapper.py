from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.services.logger import log_interaction

client = OpenAI(api_key=OPENAI_API_KEY)
model = OPENAI_MODEL

AFFIRMATIVE_TEMPLATE = "Answer this student's question clearly and supportively: {}"
CRITICAL_TEMPLATE = (
    "Instead of giving the answer directly, ask the student to think critically. "
    "Ask them what they believe the answer is and why. Then challenge or guide their reasoning: {}"
)

async def process_prompt(user_prompt: str, mode: str, user_id: str) -> str:
    if mode == "affirmative":
        final_prompt = AFFIRMATIVE_TEMPLATE.format(user_prompt)
    elif mode == "critical":
        final_prompt = CRITICAL_TEMPLATE.format(user_prompt)
    else:
        raise ValueError("Invalid mode: must be 'affirmative' or 'critical'")

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful teaching assistant."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()

    # Log to file
    log_interaction(user_id, user_prompt, reply, mode)
    return reply

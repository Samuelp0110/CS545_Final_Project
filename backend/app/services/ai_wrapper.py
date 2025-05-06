from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.services.logger import log_interaction

client = OpenAI(api_key=OPENAI_API_KEY)
model = OPENAI_MODEL

AFFIRMATIVE_TEMPLATE = (
    "Answer this student's question clearly and supportively using Markdown with proper formatting. "
    "Render math in display LaTeX (use `$$` blocks), and structure the answer with headings or bullet points if helpful. "
    "Make sure your response is readable and broken into steps where possible. Question: {}"
)

CRITICAL_TEMPLATE = (
    "Ask the student to think critically using a helpful tone. Prompt their reasoning first, then guide with follow-up questions. "
    "If examples or math are needed, use Markdown formatting and render math in display LaTeX using `$$` blocks. "
    "Structure your response clearly for readability. Question: {}"
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

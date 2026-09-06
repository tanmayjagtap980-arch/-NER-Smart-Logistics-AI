import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def ask_llm(question):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return (
            "OpenAI API key is not configured. "
            "Please add OPENAI_API_KEY to your .env file."
        )

    try:

        client = OpenAI(
            api_key=api_key
        )

        response = client.responses.create(
            model="gpt-5.6-luna",

            instructions="""
You are the AI Logistics Assistant for
NER Smart Logistics AI.

The platform is designed for logistics and
accessibility intelligence in the North Eastern
Region of India.

Help users with:

- Route optimization
- Delivery delays
- Disaster risk
- Accessibility
- Emergency logistics
- Warehouses
- Delivery tracking
- Demand prediction
- Logistics planning

Give clear and practical answers.

Do not claim that prototype or sample data
is official government data.

Do not invent live weather, traffic,
road-condition or disaster information.

If the user asks for live information that
the system does not have, clearly say that
live data is required.
""",

            input=question
        )

        return response.output_text

    except Exception as error:

        return (
            "LLM API error: "
            + str(error)
        )
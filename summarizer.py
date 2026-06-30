import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_text(transcript):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI meeting assistant. "
                    "Summarize the meeting professionally and "
                    "extract the key discussion points."
                ),
            },
            {
                "role": "user",
                "content": f"""
                Transcript:
                {transcript}

                Please provide:

                1. Meeting Summary
                2. Key Points
                """,
            },
        ],
        temperature=0.3,
        max_tokens=500,
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    with open("outputs/transcript.txt", "r", encoding="utf-8") as file:
        transcript = file.read()

    summary = summarize_text(transcript)

    print(summary)

    with open("outputs/summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)
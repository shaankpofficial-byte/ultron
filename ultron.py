from openai import OpenAI

MODEL_NAME = "GPT-5 (Ultron)"
CREATOR = "SHNX_editz studios"

API_KEY = "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"
client = OpenAI(api_key=API_KEY)

print(f"🔄 Loading {MODEL_NAME} by {CREATOR} (powered by GPT-4 API)...")
print(f"✅ {MODEL_NAME} is ready. Created by {CREATOR}. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print(f"{MODEL_NAME}: Goodbye, human. — {CREATOR}")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[{"role": "user", "content": user_input}],
        max_tokens=200
    )
    reply = response.choices[0].message.content.strip()
    print(f"{MODEL_NAME}: {reply}\n")

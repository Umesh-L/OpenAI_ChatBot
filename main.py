import openai

client = openai.OpenAI(api_key="") #Add your openAI api key here

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        try:
            response = chat_with_gpt(user_input)
            print("Chatbot:", response)
        except Exception as e:
            print("⚠️ Error:", e)

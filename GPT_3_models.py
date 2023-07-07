import os
import openai

openai.api_key = os.getenv("GPT_API")

# Define the available text models
text_models = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-16k-0613",
]

def generate_response(prompt, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

selected_model = None
model_selected = False

while not model_selected:
    print("Select a text model:")
    for i, model in enumerate(text_models, start=1):
        print(f"[{i}] {model}")
    model_number = input("Enter the model number: ")

    try:
        model_number = int(model_number)
        if 1 <= model_number <= len(text_models):
            selected_model = text_models[model_number - 1]
            model_selected = True
        else:
            print("Invalid model number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric model number.")

def chat_with_model():
    while True:
        user_input = input("You: ")
        selected_prompt = ''
        chat_prompt = selected_prompt + "\nUser: " + user_input
        response = generate_response(chat_prompt, selected_model)
        print("ChatGPT:", response)
        if user_input.lower() == "exit":
            break

chat_with_model()

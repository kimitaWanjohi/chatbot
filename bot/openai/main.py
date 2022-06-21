# from django.conf import settings
import openai

openai.api_key = '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'

def init_chat(prompt):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]

from groq import Groq

client = Groq(api_key='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')

def execute(prompt):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    return response

if __name__ == '__main__':
    print(execute("Tell me a joke"))
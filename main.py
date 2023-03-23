# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import sys
openai.api_key = sys.argv[1]
request = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": sys.argv[2]},
        {"role": "user", "content": sys.argv[0]},
    ]
)
print(request)

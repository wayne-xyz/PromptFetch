from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime


start_time=datetime.now()

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
client = OpenAI(
    api_key=os.getenv('openai_api_key')
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "tell me the result of 1+1"}
  ]
)


print(completion.choices[0].message)
end_time = datetime.now()
time_taken = (end_time - start_time).total_seconds()
print(f"Time taken to get response: {time_taken} seconds")

from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
from autogen import OpenAIWrapper


#  Original OpenAI code 
def get_openai_response(question):
    start_time = datetime.now()

    # Load environment variables from .env file
    load_dotenv()

    # Get API key from environment variable
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    response = completion.choices[0].message
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    print(f"Origenal OpenAI Time taken to get response: {time_taken} seconds")

    return response


# Autogen OpenAI code
def get_openai_response_autogen(question):
    # using the autogen.OpenAIWrapper class to do similar things 
    start_time = datetime.now()

    # Load environment variables from .env file
    load_dotenv()
    config_list=[]
    client=OpenAIWrapper(os.getenv('openai_api_key'))
    response=client.create(prompt=question,model="gpt-4o-mini")
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    print(f"Autogen version Time taken to get response: {time_taken} seconds")
    return response




test_question="What is the capital of France?"
print(get_openai_response(test_question))
print(get_openai_response_autogen(test_question))
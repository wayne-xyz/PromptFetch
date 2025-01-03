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


# Autogen OpenAI code OpenAIWrapper
# benifit 1: cach for faster response
def get_openai_response_autogen(message):
    start_time = datetime.now()

    # Load environment variables from .env file
    load_dotenv()

    # autogen using the llmconfig  https://docs.ag2.ai/docs/topics/llm_configuration
    config_list={
        "config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}],
    }
    config_list2=[{
        "model": "gpt-4",
        "api_key": os.environ["OPENAI_API_KEY"]
    }]

    base_config={
        "model": "gpt-4",
        "api_key": os.environ["OPENAI_API_KEY"],
        "cache":None
    }
    
    openai_warp=OpenAIWrapper(config_list=config_list2,**base_config)
    
    create_config = {}
    if isinstance(message, str):
        create_config['messages'] = [{"role": "user", "content": message}]
    elif isinstance(message, list):
        create_config['messages'] = message
    else:
        raise ValueError("Message must be either a string or a list of messages")

    response = openai_warp.create(**create_config)

    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    print(f"Autogen version Time taken to get response: {time_taken} seconds")
    return response




test_question="What answser of the 1 plus 1 ?"
print("=================response from Origenal OpenAI======================")
print(get_openai_response(test_question))
print('=================response from Autogen OpenAI OpenAIWrapper ======================')
print(get_openai_response_autogen(test_question))
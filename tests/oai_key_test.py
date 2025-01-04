from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
from autogen import OpenAIWrapper
from autogen import ConversableAgent


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
# https://microsoft.github.io/autogen/0.2/docs/Use-Cases/enhanced_inference 
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


#https://docs.ag2.ai/docs/tutorial/introduction by using the ConversableAgent to perform the Q and A 
# cached response 
def get_openai_response_autogenassitance(question):
    start_time = datetime.now() 
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY")}]}
    agent=ConversableAgent(name="assistant",llm_config=llm_config, human_input_mode="NEVER")
    reply = agent.generate_reply(messages=[{"role": "user", "content": question}])
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    print(f"Autogen version Time taken to get response: {time_taken} seconds")
    return reply


test_question="What answser of the 1 plus 1 ?"
print("=================response from Origenal OpenAI======================")
print(get_openai_response(test_question))
print('=================response from Autogen OpenAI OpenAIWrapper ======================')
print(get_openai_response_autogen(test_question))
print('=================response from Autogen OpenAI ConversableAgent ======================')
print(get_openai_response_autogenassitance(test_question))
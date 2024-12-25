#  this is the top agent will validate the user input and call the appropriate agent 


# import openai
# from dotenv import load_dotenv
# import os
# from datetime import datetime

class TopAgent:
    def __init__(self):
        self.start_time = datetime.now()
        load_dotenv()
        self.client = openai.ChatCompletion.create(
            api_key=os.getenv('
            openai_api_key')
        )
        self.completion = None
        self.end_time = None
        self.time_taken = None
        self.system_message=" You are helpful agent to avalidate the user input and call the appropriate agent based on this database schema{}

#        

#     def validate_input(self, user_input, schema_file):
#         """
#         Validate user input based on the database table schema
#         :param user_input: str: User input
#         :param schema_file: str: Database table schema file
#         :return: str: Validated user
#         """
#         if not user_input:
#             raise ValueError("User input cannot be empty")
        
#         if not schema_file:
#             raise ValueError("Schema file cannot be empty")
        


    
# this is the contains the functiosn for authentication from the firestore database and supabase and LLM

import firebase_admin
from firebase_admin import credentials, auth

class Authenticator:
    def __init__(self, service, credentials):
        """
        Authenticator class to authenticate with Firebase or Supabase
        :param service: str: "firebase" or "supabase"
        :param credentials: str: firebase credentials(service account) file path or supabase credentials path
        """
        self.service = service
        self.credentials = credentials
        self.session = None

    def authenticate(self):
        if self.service == "firebase":
            # Initialize Firebase
            import firebase_admin
            from firebase_admin import credentials
            cred = credentials.Certificate(self.credentials)
            self.session = firebase_admin.initialize_app(cred)
        elif self.service == "supabase":
            # Initialize Supabase
            # from supabase import create_client
            # self.session = create_client(self.credentials["url"], self.credentials["key"])
            print("Supabase not supported yet")
        else:
            raise ValueError(f"Unsupported service: {self.service}")

        return self.session

    
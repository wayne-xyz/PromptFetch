## Lib Structure:


```
/PromptFetch                # Main package directory
    ├── __init__.py                # Makes it a package
    ├── firebase_fetcher.py        # Handles Firestore interactions
    ├── supabase_fetcher.py        # Handles Supabase interactions
    ├── prompt_handler.py          # Manages prompt parsing and validation
    ├── data_formatter.py          # Formats data into JSON or other formats
    ├── sandbox.py                 # Ensures safe code execution
    ├── error_handler.py           # Centralized error handling
    ├── authentication.py          # Handles authentication for Firestore and Supabase and LLM
    ├── config.py                  # Stores global configurations and constants
    ├── core.py                    # Entry point to process user prompts

/tests                            # Unit tests for each module
    ├── test_firebase_fetcher.py  
    ├── test_supabase_fetcher.py
    ├── test_prompt_handler.py
    ├── test_core.py

/examples                         # Example usage scripts
/docs                             # Documentation

LICENSE                           # License file
README.md                         # Overview of the library
setup.py                          # Metadata for packaging
pyproject.toml                    # Modern build system configuration
requirements.txt                  # Library dependencies
```

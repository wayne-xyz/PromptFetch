# PromptFetch

AI-Driven Data Query Library for Firebase and Supabase

PromptFetch is an open-source Python library that bridges natural language prompts with database queries, enabling developers to fetch structured data effortlessly from Firebase Firestore and Supabase. Powered by large language models (LLMs), PromptFetch simplifies data retrieval by dynamically generating code to query databases based on user-friendly prompts.




## Installation

```bash
pip install promptfetch
```

## Usage

```python
from promptfetch import PromptFetch

# Basic usage example will go here
```

## Development

1. Clone the repository
```bash
git clone https://github.com/yourusername/PromptFetch.git
cd PromptFetch
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies
```bash
pip install -r requirements.txt
```

4. Run tests
```bash
pytest
```

## Publishing to PyPI

1. Update version in `pyproject.toml`
2. Build the package:
```bash
python -m build
```

3. Upload to PyPI:
```bash
python -m twine upload dist/*
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

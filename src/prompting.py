import json
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


EXAMPLES_FILE = "src/examples.txt"
MODEL_NAME = "meta-llama/Llama-3-8b-instruct"    # you can change this
MAX_TOKENS = 512


def load_examples():
    """Load raw few-shot examples from examples.txt"""
    path = Path(EXAMPLES_FILE)
    if not path.exists():
        raise FileNotFoundError(f"Missing examples file at {EXAMPLES_FILE}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def build_prompt(user_query: str):
    """Combines examples + the user's query into one training-style prompt."""
    examples = load_examples()

    # Prompt format for Llama/Gemma style instruction models
    return f"""
Below are examples of how to respond to user queries.

{examples}

Now follow the same format for this new query:

USER QUERY:
{user_query}

MODEL OUTPUT:
""".strip()


class BookRecommender:
    def __init__(self, model_name: str = MODEL_NAME):
        print(f"Loading model: {model_name}")
        self.pipe = pipeline(
            "text-generation",
            model=model_name,
            tokenizer=model_name,
            max_new_tokens=MAX_TOKENS,
            temperature=0.2,
        )

    def query(self, user_query: str):
        """Generate a model response for a book search query."""
        prompt = build_prompt(user_query)

        raw_output = self.pipe(prompt)[0]["generated_text"]

        # Only return the part AFTER "MODEL OUTPUT:"
        if "MODEL OUTPUT:" in raw_output:
            raw_output = raw_output.split("MODEL OUTPUT:", 1)[1].strip()

        # Try to load JSON if the model responded in JSON
        try:
            parsed = json.loads(raw_output)
            return parsed
        except json.JSONDecodeError:
            # Return raw text if parsing fails
            return raw_output


# Example run
if __name__ == "__main__":
    br = BookRecommender()
    result = br.query("Recommend books like The Lord of the Rings, epic fantasy with adventure.")
    print(result)

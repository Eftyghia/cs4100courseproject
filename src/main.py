import sys
from prompting import BookRecommender

def main():
    # Initialize the agent
    print("Loading book recommender agent...")
    agent = BookRecommender(
        data_path="data/books_clean.csv",
        examples_path="src/examples.txt"
    )
    print("Agent loaded!\n")
    print("Ask for a recommendation (or type 'quit' to exit):")
    
    # Command-line loop
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        
        try:
            response = agent.recommend(user_input)
            print("\nAgent:", response)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

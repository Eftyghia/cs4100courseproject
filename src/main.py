from prompting import BookRecommender

def main():
    print("Loading book recommender agent...")

    agent = BookRecommender()  

    while True:
        user_query = input("\nEnter a search request (or 'quit'): ").strip()
        if user_query.lower() in {"quit", "exit"}:
            break

        response = agent.query(user_query)
        print("\n--- Model Response ---")
        print(response)

if __name__ == "__main__":
    main()

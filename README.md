# Book Recommender Project

## Abstract
This project addresses the problem of providing personalized book recommendations based on user queries. We leverage a large language model (LLM) to generate recommendations by understanding user preferences and the content of books. Key outcomes include a working command-line interface (CLI) for querying the system and generating JSON-formatted recommendations that can easily be parsed for further applications.

## Overview
The problem we address is helping users discover books that match their interests, genres, or themes. Traditional search engines often return results based on popularity or keywords rather than semantic understanding of user intent. Our approach aims to solve this by using a language model that can comprehend natural language queries and match them with relevant book summaries.

This problem is interesting because personalized recommendation systems are widely used in online retail, libraries, and digital reading platforms. Improving recommendations not only enhances user experience but also increases engagement and adoption of reading resources. Potential use cases include online bookstores, library catalog systems, and educational platforms where users seek targeted suggestions.

Our approach uses a few-shot prompting strategy, providing the LLM with curated examples of query-response pairs. This guides the model to produce outputs in a structured JSON format, including book title, author, and reasoning for the recommendation. Unlike traditional collaborative filtering or content-based recommender systems, our method leverages natural language understanding to handle nuanced queries.

Key components of the approach include:
- Preprocessed book data (`books_clean.csv`) derived from raw summaries.
- Few-shot prompting examples (`examples.txt`) for guiding the LLM.
- A Python interface (`BookRecommender`) to generate structured recommendations.
- CLI-based interaction through `main.py`.

Limitations include dependency on model availability and quality of book data. The LLM may sometimes generate recommendations that are plausible but not perfectly accurate.

## Approach
The methodology consists of the following components:
1. **Data Preparation**: Raw book summaries are cleaned and formatted into a CSV file with fields such as title, author, and summary.
2. **Prompting**: Few-shot examples are included in the prompt to teach the model how to respond to queries in a structured format.
3. **Language Model**: We use a transformer-based causal language model (e.g., Gemma 2B or Microsoft Phi-3-mini) via the Hugging Face `transformers` library. The model generates structured JSON recommendations.
4. **Query Handling**: The CLI allows users to enter queries, which are transformed into prompts. The model output is parsed into structured JSON.
5. **Assumptions**: We assume the user provides queries in natural language. Recommendations rely on the content of `books_clean.csv` and may not cover books outside the dataset.
6. **Limitations**: The system depends on the LLM’s understanding, which can sometimes generate unexpected or irrelevant results. Performance is also constrained by the model size and local computing resources.

## Experiments
The dataset consists of a curated list of books with cleaned summaries, totaling several thousand entries. Each entry includes the book title, author, and a concise summary.

The implementation uses:
- Python 3.13
- Hugging Face `transformers` for the LLM
- CLI interface via `main.py`
- Model parameters: maximum generated tokens set to 512, temperature 0.2 to reduce randomness

The architecture is a pre-trained transformer causal LM with few-shot prompting. The model generates a continuation of the prompt and is parsed into structured JSON output.

## Results
**Main results:** The system successfully generates JSON-formatted book recommendations that match user queries, including rationale for each recommendation. Sample queries such as "Recommend books like Harry Potter" returned titles and authors with appropriate reasoning.

**Supplementary results:** Various prompt examples and model parameters were tested. Lower temperatures improved consistency of output, while higher temperatures increased diversity but sometimes reduced relevance.

## Discussion
The results show that few-shot prompting with a large language model can produce semantically meaningful book recommendations. While performance is strong for general genres and well-known books, the system may struggle with very niche or obscure queries. Future improvements could include fine-tuning on domain-specific data, adding a retrieval-augmented generation (RAG) system for more up-to-date book content, or integrating feedback from users to iteratively improve recommendations.

## Conclusion
We built a working book recommender system using a few-shot prompting approach with a transformer-based language model. The system demonstrates the ability to understand natural language queries and generate structured recommendations. Future directions could include model fine-tuning, integration with larger datasets, or deployment in a web application.

## References
1. Hugging Face Transformers Documentation: https://huggingface.co/docs/transformers
2. Microsoft Phi-3 Model Card: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct
3. Meta Gemma Model Card: https://huggingface.co/meta-llama/Gemma-2b-instruct
4. Brown, T., et al. (2020). Language Models are Few-Shot Learners. *arXiv preprint arXiv:2005.14165*. https://arxiv.org/abs/2005.14165
5. GitHub Repository Examples: Hugging Face `transformers` pipelines tutorials and examples

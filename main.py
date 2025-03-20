import streamlit as st
import chromadb
from openai import OpenAI

client_openai = OpenAI()


def get_completion(prompt):
    response = client_openai.chat.completions.create(

        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful assistant who looks up answers for a user from the references provided and returns the answer to the user's question.  If the answer is not in the references, you say 'I'm sorry, I don't have access to that information' At the end of each search result will be Metadata. Cite the passages you rely on, their chunk index, and url in your answer.  If you are going to refer the user to a financial authority you should direct them to their funds manager for questions about funds certification, funds usage, or funds acceptance. You should refer them to their financial management analyst with questions about reconciliation, billing, or invoicing.  Both of these roles are within the Financial Services Division"},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content


client = chromadb.PersistentClient("./mycollection")
collection = client.get_or_create_collection(
    name="RAG_Assistant", metadata={"hnsw:space": "cosine"})

st.title("RAG FSD Model")
st.markdown("This is an example model and framework")

st.sidebar.title("Configuration")
st.sidebar.markdown("Adjust the settings for your query")

user_question = st.text_area("Ask a question", key="user_question")

n_results = st.sidebar.number_input(
    "Number of results", min_value=1, max_value=10, value=1)


if st.button("Get Answers"):
    st.write(f"Question: {user_question}")
    st.write(f"Number of results: {n_results}")
    results = collection.query(
        query_texts=[user_question], n_results=n_results, include=["documents", "metadatas"])

    search_results = []

    for res in results["documents"]:
        for doc, meta in zip(res, results["metadatas"][0]):
            metadata_str = ", ".join(
                f"{key}: {value}" for key, value in meta.items())
            search_results.append(f"{doc}\nMetadata:: {metadata_str}")
    search_text = "\n\n".join(search_results)

    prompt = f"""Your task is to answer the following user question using the supplied search results. User Question: {user_question}
    Search Results: {search_text}
    """

    response = get_completion(prompt)
    st.write(response)

    metadata_prompt = f"""
    Your task is to answer the following user queston using the supplied search results. At the end of each search result will be Metadata. Cite the passages, their chunk index, and their URL in your answer.
    User Question: {user_question}
    Search Results: {search_text}
    """

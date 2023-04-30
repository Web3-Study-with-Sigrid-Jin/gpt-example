import streamlit
from langchain import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore import InMemoryDocstore
import faiss
from package.babyagi import BabyAGI
from package.input import get_text

streamlit.title('Personal AI Assistant for SOPT Study')

embeddings_model = OpenAIEmbeddings()

embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

user_input = get_text()

OBJECTIVE = user_input
llm = OpenAI(temperature=0)

# Logging of LLMChains
verbose = True

# If None, will keep on going forever. Customize the number of loops you want it to go through.
max_iterations = 2
baby_agi = BabyAGI.from_llm(
    llm=llm, vectorstore=vectorstore, verbose=verbose, max_iterations=max_iterations
)

if (user_input):
    baby_agi({"objective": OBJECTIVE})

    # Download the file using Streamlit's download_button() function
    streamlit.download_button(
        label='Download Results',
        data=open('output.txt', 'rb').read(),
        file_name='output.txt',
        mime='text/plain'
    )
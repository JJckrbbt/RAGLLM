import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter

files = [
    {
        "title":
        "Principles of Federal Appropriations Law 4th Edition Chapter 1",
        "source_url": "https://www.gao.gov/assets/2019-11/675699.pdf",
        "filename": "redbook1-4.pdf"
    },
    {
        "title":
        "Principles of Federal Appropriations Law 4th Edition Chapter 2",
        "source_url": "https://www.gao.gov/assets/2019-11/675709.pdf",
        "filename": "redbook2-4.pdf"
    },
    {
        "title":
        "Principles of Federal Appropriations Law 4th Edition Chapter 3",
        "source_url": "https://www.gao.gov/assets/2019-11/687162.pdf",
        "filename": "redbook3-4.pdf"
    },
    {
        "title":
        "Principles of Federal Appropriations Law 3rd Edition Volume 1",
        "source_url": "https://www.gao.gov/assets/2019-11/202437.pdf",
        "filename": "redbook3ev1.pdf"
    },
    {
        "title":
        "Principles of Federal Appropriations Law 3rd Edition Volume 2",
        "source_url": "https://www.gao.gov/assets/2019-11/202819.pdf",
        "filename": "redbook3ev2.pdf"
    },
    {
        "title":
        "Principles of Federal Appropriations Law 3rd Edition Volume 3",
        "source_url": "https://www.gao.gov/assets/2019-11/203470.pdf",
        "filename": "redbook3ev3.pdf"
    },
    {
        "title":
        "Principles of Federal Appropriations Law Annual Update of the Third Edition",
        "source_url": "https://www.gao.gov/assets/2019-11/668991.pdf",
        "filename": "redbookAnnual3e.pdf"
    },
    {
        "title":
        "Treasury Financial Manual Vol. 1 Part 2, Chapter 4700 Appendix 8",
        "source_url": "https://tfx.treasury.gov/sites/default/files/2024-03/Appendix-8-2-4700_0.pdf",
        "filename": "TFMChap4700Appendix8.pdf"
    },
    {
        "title":
        "FASAB Handbook of Accounting Standards and Other Pronouncements, as Amended",
        "source_url": "https://files.fasab.gov/pdffiles/2024_FASAB%20Handbook.pdf",
        "filename": "2024_FASABHandbook1.pdf"
    }
]

folder_path = "markdown_collection"


client = chromadb.PersistentClient("./mycollection/")
collection = client.get_or_create_collection(
    name='RAG_Assistant', metadata={"hnsw:space": "cosine"})

# with open(f"./{folder_path}/{files[0]['filename']}", "r") as file:
#     content = file.read()

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ". ", "? ", "! "],
                                               chunk_size=1500,
                                               chunk_overlap=200
                                               )

# chunks = text_splitter.create_documents([content])
# print(chunks[:3])

documents = []
metadatas = []
ids = []

for file_info in files:
    with open(f"./{folder_path}/{file_info['filename']}", "r") as file:
        content = file.read()

        chunks = text_splitter.create_documents([content])

        for index, chunk in enumerate(chunks):
            metadatas.append({
                             "title": file_info["title"],
                             "source_url": file_info["source_url"],
                             "chunk_idx": index
                             })

            ids.append(f"{file_info['filename']}_{index}")

            documents.append(chunk.page_content)

collection.add(documents=documents, metadatas=metadatas, ids=ids)

collection.query(query_texts=["what is continuing need?",
                 "what is bona fide need?"], n_results=1)

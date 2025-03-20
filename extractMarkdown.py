import os
import pymupdf4llm

folder_path = "./markdown_collection/"
directory = "/home/Code/Projects/Rag/AppropLaw/approp"


def save_markdown(content, folder_path, filename):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "w") as file:
        file.write(content)

    print(f"Markdown file saved to {file_path}")


def process_files_in_directory(directory_path):
    try:

        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        for filename in os.listdir(directory_path):
            source_path = os.path.join(directory_path, filename)

            if os.path.isfile(source_path):
                print(f"Processing file: {filename}")
                md_text = pymupdf4llm.to_markdown(source_path)
                save_markdown(md_text, folder_path, filename)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")


process_files_in_directory(directory)

# splitter = MarkdownTextSplitter(chunk_size=600, chunk_overlap=50)

# split_text = splitter.create_documents([md_text])

# print(split_text)

# save_json(split_text, folder_path, "split redbook1-4.json")

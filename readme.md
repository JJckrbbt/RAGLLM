# RRG LLM Demo

## Intent
This project is intended as an early stage test of completion quality for a Financial Mangement RAG-LLM. 

## Subject
The subject matter is the Government Accountability Office's *Principles of Appropriation Law*, also known as the Redbook.  Also included are the *FASAB Handbook* and the *Treasury Financial Manual Chapter 4700 Appendix 8*.  Other sources may be added.  

## To run
Pre-requisite: For demo to work, an OpenAI API Key must be set as an environment variable. 

1. Run `python extractMarkdown.py` to extract Markdown from PDF documents contained in data/documents folder.
2. Run `python chroma.py` to create collection.
3. Run `streamlit run main.py` to start Streamlit app
4. Ctrl click on url to view in browser
5. Set maximum number of results in sidebar of new browser tab/window
6. Enter question in *Ask a question* field and click on *Get Answers*

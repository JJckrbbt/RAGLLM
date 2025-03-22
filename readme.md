# RRG LLM Demo

## Intent
This project is intended as an early stage test of completion quality for an Financial Mangement RAG-LLM. 

## Subject
The subject matter is the Government Accountability Office's *Principles of Appropriation Law*, also known as the Redbook.  Also included are the *FASAB Handbook* and the *Treasury Financial Manual Chapter 4700 Appendix 8*.  Other sources may be added.  

## To run

1. Run `python extractMarkdown.py` to extract Markdown from PDF documents contained in data/documents folder.
2. Run `python chroma.py` to create collection.
3. Run `streamlit run main.py` to start Streamlit app
4. Ctrl click on url to view in browser

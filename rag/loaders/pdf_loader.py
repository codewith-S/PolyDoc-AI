import os
from langchain_community.document_loaders import PyPDFLoader

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts and combines text from all pages of a given PDF file.
    
    Args:
        file_path (str): The path to the PDF file.
        
    Returns:
        str: The extracted text.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # 1. Input & Extract: Initialize the LangChain loader and extract documents
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    # 2. Process: Combine the text from all parsed pages into a single string
    extracted_text = "\n".join([doc.page_content for doc in documents])
    
    # 3. Return: Pass back the pure text string
    return documents

if __name__ == "__main__":
    # Define the input file (ensure you have a sample.pdf in this directory)
    from pathlib import Path

sample_file = Path("uploads") / "sample.pdf"
    
    try:
        # Execute the extraction
        text_output = extract_text_from_pdf(sample_file)
        
        # 4. Print text
        print(f"--- Successfully extracted text from {sample_file} ---")
        print(text_output)
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred during extraction: {e}")
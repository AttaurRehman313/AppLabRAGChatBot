from langchain_community.document_loaders import PyPDFLoader,TextLoader,Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



# Loading a PDF
def load_file(file):

    """
    Loads a file based on its extension and returns its content.

    This function supports loading files with the following extensions:
    - PDF (.pdf)
    - Text (.txt)
    - Word document (.docx)

    If the file extension is invalid, a message is returned indicating the issue.
    """
    if isinstance(file, str) and file.lower().endswith('.pdf'):
    
        loader = PyPDFLoader(file)
        Text= loader.load()
        return Text
    
    elif isinstance(file, str) and file.lower().endswith('.txt'):
        loader = TextLoader(file)
        Text= loader.load()
        return Text
    
    elif isinstance(file, str) and file.lower().endswith('.docx'):
        loader = Docx2txtLoader(file)
        Text= loader.load()
        return Text
    
    return "you upload invalide .extention file your file must be a .txt and .pdf  "



def create_chunks(data):
    """
    This function loads the provided file data and splits it into chunks 
    using RecursiveCharacterTextSplitter with a specified chunk size 
    and overlap.
    """
    text=load_file(data)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
    text_chunks = text_splitter.split_documents(text)
    return text_chunks

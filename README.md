RAG Chatbot Application
This repository contains the implementation of a Retrieval-Augmented Generation (RAG) chatbot using Flask for the backend and HTML, CSS, and JavaScript for the frontend. The application allows users to upload files, create vector embeddings, and perform conversational retrieval with the data.
Features
File Upload and Processing


Supports .pdf, .txt, and .docx file formats.
Reads and processes uploaded files into manageable chunks.
Creates vector embeddings using FAISS and stores them locally.
Conversational Chatbot


Allows users to ask questions based on the uploaded documents.
Uses a conversational retrieval chain with memory to provide context-aware responses.
File Deletion


Enables deletion of uploaded files along with their associated vector stores.
Blueprint Architecture


Modular structure with separate blueprints for file upload, chat, and file deletion.
Frontend Integration


Uses HTML, CSS, and JavaScript for the user interface.
JavaScript fetch API is used for seamless integration with backend routes.
Project Structure
├── mainapp
│   ├── routes
│   │   ├── conversation_route.py
│   │   ├── uploadfile_route.py
│   │   ├── deletefile_route.py
│   ├── utils
│   │   ├── file_loadin_and_chunking.py
│   ├── __init__.py
├── app.py
├── requirements.txt
└── README.md

Setup Instructions
Python 3.8+
Flask
FAISS
LangChain
Google Generative AI SDK
Installation
Clone the repository:

 git clone <repository-url>
cd <repository-folder>


Create a virtual environment and activate it:

 python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install the required dependencies:

 pip install -r requirements.txt


Set up environment variables:


Create a .env file in the root directory.
Add the following variable:
 GEMINI_API_KEY=your_google_api_key


Run the application:

 python main.py


Access the application at http://127.0.0.1:5000.


Routes
1. File Upload Route
Endpoint: /upload_pdf
 Method: POST
Uploads a file and creates a vector store for it.
Supported file types: .pdf, .txt, .docx
Example Request:
curl -X POST -F "file=@example.pdf" http://127.0.0.1:5000/upload_pdf

2. Chat Route
Endpoint: /chat
 Method: POST
Handles user queries and provides AI-generated responses.
Requires a vector store to be created first.
Example Request:
curl -X POST -H "Content-Type: application/json" -d '{"query": "What is in the document?"}' http://127.0.0.1:5000/chat

3. Delete File Route
Endpoint: /delete
 Method: DELETE
Deletes a specified file and its associated vector store.
Example Request:
curl -X DELETE -H "Content-Type: application/json" -d '{"file_delete": "example.pdf"}' http://127.0.0.1:5000/delete

Core Functions
1. File Loading and Chunking
load_file(file): Loads and processes files based on their extensions.
create_chunks(data): Splits loaded text into smaller chunks for embedding creation.
2. Embedding and Vector Store
create_vector_db(data): Creates a FAISS vector database from the input data.
retrievers(): Loads the vector database and sets up a retriever for similarity searches.
3. Chat Model
chat_model(retriever): Initializes a conversational chain using Google Generative AI and conversation memory.
Frontend Integration
HTML and CSS: Provide the structure and styling of the user interface.
JavaScript Fetch API: Enables asynchronous communication with the backend for file uploads, chats, and deletions.
Example Workflow
Upload a File


User uploads a .pdf, .txt, or .docx file via the /upload_pdf route.
Backend saves the file, processes it, and creates a vector store.
Start a Conversation


User sends a query to the /chat route.
Backend retrieves relevant information from the vector store and provides a response.
Delete a File


User deletes an uploaded file via the /delete route.
Backend removes the file and its associated vector store.
Future Improvements
Add support for additional file types.
Implement user authentication for secure file uploads.
Enhance frontend with a more interactive user interface.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss changes.


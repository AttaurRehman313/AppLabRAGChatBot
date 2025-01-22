from flask import Blueprint, request,jsonify
from mainapp.utils.functions import prompts
from mainapp.model.file_embedding import retrievers
from mainapp.model.textgeneration import chat_model
import os

chat=Blueprint("chat",__name__)


@chat.route('/chat', methods=['POST'])
def chating():
    """
    This route handles incoming POST requests to the '/chat' endpoint. 
    It extracts the user's query from the request, processes it, and returns the AI-generated response in HTML format.
    """
    if request.method=="POST":
        userquery=request.json['query']
        if userquery=='':
            return jsonify({"message":"user query not be null. Please wirte somethin in user query"}),400
        
        if not os.path.exists("faiss_index"):
            return jsonify({"message": "Your vector store is not created. Please upload a file first."}), 400
        
        input_prompt=prompts(userquery)

        retriever=retrievers()

        try:
            chain=chat_model(retriever)
            response=chain.invoke({"question":input_prompt,"chat_history":""})
            return jsonify({"answer": response['answer']}),200
        except Exception as e:
            return jsonify({"message",f"An error occurred during text generation: {e}"}),400
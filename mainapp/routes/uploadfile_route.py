from flask import Blueprint, request,jsonify
from mainapp.utils.filesave import save_file
from mainapp.model.file_embedding import create_vector_db
upload=Blueprint("upload_pdf",__name__)


@upload.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    """
    This route handles the upload of PDF files via a POST request. 
    It ensures the file is saved and processed into a vector database.
    """
    if request.method=="POST":
        file = request.files['file']
        if file == '':
            return jsonify({"message": "No file selected."}), 400
        
        file_path = save_file(file)

        if "File Already Exists" in file_path or "Invalid file type" in file_path:
            return jsonify({"message": file_path}), 400
        
        create_vector_db(file_path)
        return jsonify({"message": "Your vector is stored successfully."}), 200

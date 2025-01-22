from flask import Blueprint, request,jsonify
import os,shutil

remove=Blueprint("delete",__name__)



@remove.route("/delete", methods=["DELETE"])
def delete():
    """
    Handles DELETE requests for deleting files of specific types (PDF, TXT, DOCX).
    Validates the file path, ensures the file exists, and removes both the file 
    and associated FAISS index directory. Returns appropriate status messages.
    """
    if request.method=="DELETE":
        file = request.json.get("file_delete")
        if file == '':
            return jsonify({"message": "No file selected."}), 400
        
        if file.lower().endswith('.pdf'):
            file_path = os.path.join("PDF_Files", file)
            if not os.path.exists(file_path):
                return jsonify({"message": f"{file} does not exist."}), 404
            os.remove(file_path)
            if os.path.exists("faiss_index"):
                shutil.rmtree("faiss_index")
            return jsonify({"message": f"{file} deleted successfully."}), 200
        
        elif file.lower().endswith('.txt'):
            file_path = os.path.join("TXT_File", file)
            if not os.path.exists(file_path):
                return jsonify({"message": f"{file} does not exist."}), 404
            os.remove(file_path)
            if os.path.exists("faiss_index"):
                shutil.rmtree("faiss_index")
            return jsonify({"message": f"{file} deleted successfully."}), 200
        
        elif file.lower().endswith('.docx'):
            file_path = os.path.join("Docx_File", file)
            if not os.path.exists(file_path):
                return jsonify({"message": f"{file} does not exist."}), 404
            os.remove(file_path)
        
            if os.path.exists("faiss_index"):
                shutil.rmtree("faiss_index")

            return jsonify({"message": f"{file} deleted successfully."}), 200
        
        return jsonify({"message": "Invalid file type."}), 400

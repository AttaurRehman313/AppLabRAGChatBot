import os

def save_file(file):
    """
    This block checks if the file's filename is empty. If no file 
    is selected, it returns "No file selected."
    """
    if file.filename == '':
        return "No file selected."


    if file and file.filename.lower().endswith('.pdf'):
        """
        If the file ends with '.pdf', this block creates a directory for 
        PDFs if it doesn't exist and saves the file if not already present.
        """
        if not os.path.exists('PDF_Files'):  
            os.makedirs('PDF_Files')
        file_path = os.path.join('PDF_Files', file.filename)  
        if os.path.exists(file_path):  
            return "File Already Exists"
        file.save(file_path) 
        return file_path
    

    elif file and file.filename.lower().endswith('.txt'):
        """
        If the file ends with '.txt', it creates a TXT directory if needed 
        and saves the file after checking for its existence in the directory.
        """
        if not os.path.exists('TXT_File'):  
            os.makedirs('TXT_File')
        file_path = os.path.join('TXT_File', file.filename)  
        if os.path.exists(file_path): 
            return "File Already Exists"
        file.save(file_path)  
        return file_path
    
    elif file and file.filename.lower().endswith('.docx'):
        """
        If the file ends with '.txt', it creates a TXT directory if needed 
        and saves the file after checking for its existence in the directory.
        """
        if not os.path.exists('Docx_File'):  
            os.makedirs('Docx_File')
        file_path = os.path.join('Docx_File', file.filename)  
        if os.path.exists(file_path):  
            return "File Already Exists"
        file.save(file_path) 
        return file_path
    
    # Returns an error message if file type is unsupported
    return "Invalid file type."
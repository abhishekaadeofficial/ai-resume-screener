import PyPDF2
import docx2txt

def extract_text(file):
    if file.name.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    
    elif file.name.endswith('.docx'):
        return docx2txt.process(file)
    
    else:
        return "Unsupported file format"

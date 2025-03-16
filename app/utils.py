from langchain_community.document_loaders import PyPDFLoader
import os


# UPLOAD_FOLDER = "../data"
def get_latest_path(folder_path):
    if os.listdir(folder_path):
        files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
        latest_file = max(files, key=os.path.getctime)
    else:
        return None
    return latest_file
        
# Get the last PDF file
def load_latest_pdf(folder_path):
    file_path = get_latest_path(folder_path)
    if file_path:
        loader = PyPDFLoader(file_path)
        pages = []
        for page in loader.load():
            pages.append(page)
    else:
        return None
    return pages

# pages = (load_latest_pdf(UPLOAD_FOLDER))
# print(pages)

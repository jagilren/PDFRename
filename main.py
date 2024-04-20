import fitz
import os
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import tkinter as tk

def rename_pdf(pdf_instance,pdf_path, new_name):
    directory_path, filename = os.path.split(pdf_path)
    # Rename the file
    os.rename(pdf_path,directory_path +"/" + new_name + ".pdf")
    global numero
    numero +=1
    print("File renamed successfully.")

def extract_text_from_pdf(pdf_path):
    text = ""
    text_list = []
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            text += page.get_text()
            text_list.extend(text.split('\n'))
            Subscriptor = text_list[11]
        print(Subscriptor)
    # pdf_document.close()
    rename_pdf(pdf_document,pdf_path,Subscriptor)
    return Subscriptor



def process_pdf_files(folder_path):
    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a PDF
        if file_name.endswith(".pdf"):
            # Create the full path to the PDF file
            pdf_path = os.path.join(folder_path, file_name)
            suscriptor  = extract_text_from_pdf(pdf_path)


def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory()  # Open the folder selection dialog

    if folder_path:
        print("Selected folder:", folder_path)
    else:
        print("No folder selected.")

    process_pdf_files(folder_path)




try:
    numero = 0
    select_folder()
    messagebox.showinfo('Información',f'Fueron cambiados {numero} nombres de archivos en forma correcta')
except Exception as e:
    print(e)
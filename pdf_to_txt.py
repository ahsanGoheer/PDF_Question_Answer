import PyPDF2
import re


def pdf_to_txt(pdf_path, save_path):

    pdf_obj = open(pdf_path, "rb")

    pdf_manager = PyPDF2.PdfReader(pdf_obj)

    pdf_pages = len(pdf_manager.pages)
    for page in range(1):
        pdf_page_data = pdf_manager.pages[5]

        pdf_text = pdf_page_data.extract_text()
        pdf_text = re.sub(r'(.) ',r'\1', pdf_text)
        pdf_txt_file = open(save_path, "a")

        pdf_txt_file.writelines(pdf_text)

    pdf_txt_file.close()

    print("PDF Converted to Text")

    return save_path
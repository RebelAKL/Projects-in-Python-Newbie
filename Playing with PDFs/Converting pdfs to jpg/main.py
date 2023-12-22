import fitz 
from PIL import Image

def pdf_to_jpg(pdf_path, output_folder, dpi = 600):

    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):

        page = pdf_document[page_number]

        image = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        
        output_path = f"{output_folder}/page_{page_number + 1}.jpg"

        pil_image.save(output_path, "JPEG")

    pdf_document.close()

if __name__ == "__main__":
    pdf_path = "E:\Dushy\Ananay\Certs\Google Cybersecurity\GCS_Assets,Threats and Vulnerabilities.pdf"

    output_folder = "E:\Dushy\Ananay\Certs\Google Cybersecurity"

    pdf_to_jpg(pdf_path, output_folder, dpi = 600)

    print("Conversion completed.")

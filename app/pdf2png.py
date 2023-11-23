import fitz
import os


def convert_pdf_to_images(pdf_folder, output_folder):
    # Iterate through each PDF in the folder
    for pdf_file in os.listdir(pdf_folder):
        if not pdf_file.endswith(".pdf"):
            continue

        pdf_path = os.path.join(pdf_folder, pdf_file)
        pdf_name = os.path.splitext(pdf_file)[0]

        # Open the PDF
        doc = fitz.open(pdf_path)  # type: ignore

        # Create a folder for this PDF's images
        pdf_output_folder = os.path.join(output_folder, pdf_name)
        os.makedirs(pdf_output_folder, exist_ok=True)

        # Iterate through each page
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # number of page
            pix = page.get_pixmap()
            output_path = os.path.join(pdf_output_folder, f"page_{page_num}.png")
            pix.save(output_path)

        doc.close()


if __name__ == "__main__":
    pdf_folder = os.path.join("static", "private", "pdfs")
    output_folder = os.path.join("static", "private", "imgs")
    os.makedirs(output_folder, exist_ok=True)
    convert_pdf_to_images(pdf_folder, output_folder)

from flask import Flask, render_template
import os
from pdf2image.pdf2image import convert_from_path


app = Flask(__name__)

# Directory where PDFs are stored
PDF_DIR = 'pdfs'

def pdf_to_img(pdf_path):
    # Convert the first page of the PDF to an image
    images = convert_from_path(pdf_path, first_page=1, last_page=1)

    if images:
        image = images[0]
        # Save the image to a directory and return the path
        image_path = os.path.join('path/to/save/images', os.path.basename(pdf_path) + '.png')
        image.save(image_path, 'PNG')
        return image_path

    return None  # Return None if conversion failed

@app.route('/')
def index():
    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith('.pdf')]

    # Convert each PDF's first page to an image and store the paths
    pdf_previews = [(pdf, pdf_to_img(os.path.join(PDF_DIR, pdf))) for pdf in pdf_files]

    # Render the template with the PDF previews
    return render_template('index.html', pdf_previews=pdf_previews)

if __name__ == '__main__':
    app.run(debug=True)

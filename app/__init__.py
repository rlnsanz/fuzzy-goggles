from flask import Flask, render_template
from PIL import Image
import os
from pdf2image.pdf2image import convert_from_path


app = Flask(__name__)

# Directory where PDFs are stored
PDF_DIR = 'pdfs'
os.makedirs(PDF_DIR, exist_ok=True)

IMGS_DIR = 'app/static/imgs'
os.makedirs(IMGS_DIR, exist_ok=True)

def pdf_to_img(pdf_path, size=(300, 400)):  # Define your desired size (width, height)
    # Convert the first page of the PDF to an image
    images = convert_from_path(pdf_path, first_page=1, last_page=1)

    if images:
        image = images[0]
        # Resize the image to the desired size using the LANCZOS filter
        image = image.resize(size, Image.Resampling.LANCZOS)
        
        # Save the image to a directory and return the path
        new_name = os.path.basename(pdf_path).replace('.pdf', '.png')
        image_path = os.path.join(IMGS_DIR, new_name)
        image.save(image_path, 'PNG')
        return new_name  # Return only the basename

    return None  # Return None if conversion failed

@app.route('/')
def index():
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith('.pdf')]

    # Convert each PDF's first page to an image, store only the basenames
    image_path = [pdf_to_img(os.path.join(PDF_DIR, pdf)) for pdf in pdf_files]

    pdf_previews = [(pdf, os.path.basename(imgp)) if imgp is not None else (pdf, None) for pdf,imgp in zip(pdf_files, image_path)]

    # Render the template with the PDF previews
    return render_template('index.html', pdf_previews=pdf_previews)


if __name__ == '__main__':
    app.run(debug=True)

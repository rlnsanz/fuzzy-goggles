// app/static/js/script.js

function openPdfViewer(pdfName) {
    // Construct the URL for the Flask route which will serve the PDF
    const url = `/view-pdf?name=${encodeURIComponent(pdfName)}`;
    // Open the PDF in a new browser tab
    window.open(url, '_blank');
}

import fitz  # pip install pymupdf
import os
import sys
import re

def extract_and_export_first_sentences(pdf_path, output_filename='first_sentences.txt'):
    # Extract paragraphs using PyMuPDF
    doc = fitz.open(pdf_path)
    paragraphs = []
    for page in doc:
        blocks = page.get_text("blocks")  # Returns list of (x0, y0, x1, y1, text, block_no, block_type)
        for block in blocks:
            if block[4].strip():  # block[4] is the text
                paragraphs.append(block[4].strip())
    doc.close()
    
    first_sentences = []
    for para in paragraphs:
        # Remove leading numbers like "1.", "2.", etc.
        para = re.sub(r'^\d+\.\s*', '', para)
        # Simple sentence split; for better accuracy, use NLTK or spaCy
        sentences = para.split('.')
        if sentences:
            first = sentences[0].strip() + '.'
            first_sentences.append(first)
    
    # Get the directory of the input PDF
    output_dir = os.path.dirname(pdf_path)
    output_path = os.path.join(output_dir, output_filename)
    
    # Export to .txt file
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for sentence in first_sentences:
            outfile.write(sentence + '\n')
    
    print(f"Exported first sentences to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <pdf_filename>")
        sys.exit(1)
    pdf_file = sys.argv[1]
    extract_and_export_first_sentences(pdf_file)
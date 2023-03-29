from pypdf import PdfMerger
import os

dir = 'PDFBin'

outDir = 'Output'

files = os.listdir(dir)

pdfs = []

for file in files:
    if file.endswith('.pdf'):
        pdfs.append(os.path.join(dir, file))


merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(os.path.join(outDir, "merged.pdf"))
merger.close()


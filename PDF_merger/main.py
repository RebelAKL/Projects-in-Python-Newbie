import PyPDF2
def merge_pdf(input_files, output_files):
    pdf_merger = PyPDF2.PdfMerger()
    for pdf_file in input_files:
        with open(pdf_file, 'rb') as file:
            pdf_merger.append(file)
    with open(output_files, 'wb') as merged_file:
        pdf_merger.write(merged_file)
if __name__ == "__main__":
    input_files = ['file1.pdf', 'file2.pdf']
    output_file = 'merged.pdf'
    merge_pdf(input_files, output_file)
    print("Successfully merged")

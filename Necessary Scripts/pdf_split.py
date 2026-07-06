import os 
from pikepdf import Pdf 
from datetime import datetime 
 
print("\n PDF Splitter - Custom Page Range \n") 
print("\n Application splits the PDF based on user-defined page range \n") 
print("\n Date: 03 February 2025 \n\n") 
 
# Get PDF file path 
while True:
    filepath1 = input("Enter the full path of the PDF file: ").strip() 
    
    # Normalize path separators and expand user home directory
    filepath1 = os.path.normpath(os.path.expanduser(filepath1))
    
    # Validate file exists and is a PDF 
    if os.path.exists(filepath1) and filepath1.lower().endswith('.pdf'): 
        break
    else:
        print("Invalid file path. Please provide a valid PDF file.")
 
# Get page range 
while True: 
    try: 
        start_page = int(input("Enter the starting page number (1-based index): ")) 
        end_page = int(input("Enter the ending page number (1-based index): ")) 
        
        # Validate page range 
        if start_page < 1 or end_page < start_page: 
            print("Invalid page range. Please try again.") 
            continue 
        
        break 
    except ValueError: 
        print("Please enter valid integer page numbers.") 
 
# Create output directory 
output_dir = os.path.join(os.path.dirname(filepath1), "Output") 
os.makedirs(output_dir, exist_ok=True) 
 
# Open the input PDF 
try: 
    input_file = Pdf.open(filepath1) 
    
    # Validate page range against total pages 
    if end_page > len(input_file.pages): 
        print(f"Warning: Specified end page exceeds total pages. Using last page {len(input_file.pages)}.") 
        end_page = len(input_file.pages) 
    
    # Get PDF filename without extension 
    pdfname = os.path.splitext(os.path.basename(filepath1))[0] 
    
    # Split specified page range 
    output_pdf = Pdf.new() 
    for page_num in range(start_page-1, end_page): 
        output_pdf.pages.append(input_file.pages[page_num]) 
    
    # Save the output PDF 
    output_path = os.path.join(output_dir, f"{pdfname}_pages_{start_page}-{end_page}.pdf") 
    
    # Save with metadata 
    with output_pdf.open_metadata(set_pikepdf_as_editor=False) as meta: 
        meta["pdf:Producer"] = "pikepdf" 
        meta["xmp:CreateDate"] = datetime.now(datetime.utcnow().astimezone().tzinfo).isoformat() 
        meta["xmp:ModifyDate"] = datetime.now(datetime.utcnow().astimezone().tzinfo).isoformat() 
    
    output_pdf.save(output_path, linearize=True, force_version="1.4") 
    
    print(f"\nPDF successfully split. Output saved to: {output_path}") 
 
except Exception as e: 
    print(f"An error occurred: {e}")
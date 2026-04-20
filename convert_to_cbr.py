import os
import zipfile
import shutil
from pdf2image import convert_from_path


def batch_convert_to_cbz(input_folder, output_folder="chandamama_cbz", dpi=150):
    """
    Scans a folder for PDFs and converts each one into a CBZ archive.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all PDF files in the directory
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in {input_folder}")
        return

    print(f"Found {len(pdf_files)} PDFs. Starting conversion...")

    for pdf_name in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_name)
        base_name = os.path.splitext(pdf_name)[0]
        cbz_path = os.path.join(output_folder, f"{base_name}.cbz")

        # Skip if already converted
        if os.path.exists(cbz_path):
            print(f"Skipping {base_name} (Already exists)")
            continue

        print(f"Processing: {base_name}...")
        temp_img_dir = f"temp_{base_name}"
        os.makedirs(temp_img_dir, exist_ok=True)

        try:
            # 1. Convert PDF pages to images
            # Note: Lower DPI = Faster conversion & smaller file size
            pages = convert_from_path(pdf_path, dpi=dpi)

            for i, page in enumerate(pages):
                image_name = f"page_{str(i + 1).zfill(3)}.jpg"
                page.save(os.path.join(temp_img_dir, image_name), "JPEG")

            # 2. Create CBZ (Zip) Archive
            with zipfile.ZipFile(cbz_path, 'w', zipfile.ZIP_DEFLATED) as cbz:
                for root, _, files in os.walk(temp_img_dir):
                    for file in files:
                        cbz.write(os.path.join(root, file), file)

            print(f"Successfully created: {cbz_path}")

        except Exception as e:
            print(f"Error processing {pdf_name}: {e}")

        finally:
            # 3. Cleanup temp folder
            if os.path.exists(temp_img_dir):
                shutil.rmtree(temp_img_dir)


if __name__ == "__main__":
    # Point this to the folder where your PDFs are stored
    batch_convert_to_cbz("chandamama_english")
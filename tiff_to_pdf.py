"""" Convert multiple TIFF images to a single PDF file using Python """
import argparse
from PIL import Image

def process_arguments():
    """ Process command line arguments """
    parser = argparse.ArgumentParser(\
      description="Convert multiple TIFF images to a single PDF file using Python")
    parser.add_argument("pdf_output_file", type=str, \
      help="Output PDF file, it will be appended with all TIFF images")
    parser.add_argument("tiff_files", nargs='+', \
      help="TIFF files to be converted to PDF and appended to the output PDF file")
    return parser.parse_args()

def main_loop():
    """ Main loop """
    args = process_arguments()
    tiff_files = args.tiff_files
    output_pdf = args.pdf_output_file

    # Open the first image and convert to RGB
    first_image = Image.open(tiff_files[0]).convert("RGB")

    # Open the rest of the images and convert to RGB
    other_images = \
        [Image.open(file).convert("RGB") for file in tiff_files[1:]]

    # Save all images into a single PDF
    first_image.save(output_pdf, save_all=True, append_images=other_images)

    print(f"PDF successfully created: {output_pdf}")

if __name__ == "__main__":
    main_loop()

# pic_test

抛落物和雨雪雾的照片 (Photos of falling objects and rain, snow, and fog)

## Description

This repository contains a collection of images and a PDF generation tool.

## PDF Generation

### Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Usage

Generate a PDF from all images in the repository:

```bash
python generate_pdf.py
```

This will create a PDF file named `images_collection.pdf` containing all images with a greeting page.

#### Options

- `-o, --output`: Specify the output PDF filename (default: `images_collection.pdf`)
- `-g, --greeting`: Specify the greeting text for the first page (default: `你好`)

#### Examples

```bash
# Generate PDF with default settings
python generate_pdf.py

# Generate PDF with custom filename
python generate_pdf.py -o my_images.pdf

# Generate PDF with custom greeting
python generate_pdf.py -g "Hello World"

# Both custom filename and greeting
python generate_pdf.py -o gallery.pdf -g "Welcome to my gallery"
```

## Images

The repository contains fire-related images in various formats:
- PNG
- JPG
- WEBP

All images follow the naming convention: `fire_img_0630_XXXX.ext`

## License

This is a test repository for image collection and PDF generation.

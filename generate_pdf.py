#!/usr/bin/env python3
"""
PDF Generation Script for Image Repository
Converts images to PDF format with optional text content.
"""

import os
import sys
import glob
from pathlib import Path
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    from PIL import Image
except ImportError:
    print("Required libraries not found. Please install:")
    print("  pip install reportlab Pillow")
    sys.exit(1)


def create_pdf_from_images(output_filename="output.pdf", greeting_text="你好"):
    """
    Create a PDF document from images in the current directory.
    
    Args:
        output_filename: Name of the output PDF file
        greeting_text: Greeting text to display on the first page
    """
    # Get all image files
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.webp']
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(ext))
    
    image_files.sort()
    
    if not image_files:
        print("No image files found in the current directory.")
        return
    
    print(f"Found {len(image_files)} image files")
    
    # Create PDF
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4
    
    # First page with greeting
    c.setFont("Helvetica", 24)
    c.drawString(100, height - 100, greeting_text)
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 130, f"Image Gallery - {len(image_files)} images")
    c.showPage()
    
    # Add each image on a new page
    for idx, img_file in enumerate(image_files, 1):
        try:
            print(f"Processing {idx}/{len(image_files)}: {img_file}")
            
            # Open image to get dimensions
            img = Image.open(img_file)
            img_width, img_height = img.size
            
            # Calculate scaling to fit page while maintaining aspect ratio
            margin = 50
            available_width = width - 2 * margin
            available_height = height - 2 * margin
            
            scale = min(available_width / img_width, available_height / img_height)
            scaled_width = img_width * scale
            scaled_height = img_height * scale
            
            # Center the image
            x = (width - scaled_width) / 2
            y = (height - scaled_height) / 2
            
            # Draw image
            c.drawImage(img_file, x, y, width=scaled_width, height=scaled_height, 
                       mask='auto')
            
            # Add caption
            c.setFont("Helvetica", 10)
            c.drawString(margin, margin - 20, f"Image {idx}: {img_file}")
            
            c.showPage()
        except Exception as e:
            print(f"Error processing {img_file}: {e}")
            continue
    
    # Save PDF
    c.save()
    print(f"\nPDF created successfully: {output_filename}")
    print(f"Total pages: {len(image_files) + 1}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate PDF from images')
    parser.add_argument('-o', '--output', default='images_collection.pdf',
                       help='Output PDF filename (default: images_collection.pdf)')
    parser.add_argument('-g', '--greeting', default='你好',
                       help='Greeting text for the first page (default: 你好)')
    
    args = parser.parse_args()
    
    create_pdf_from_images(args.output, args.greeting)

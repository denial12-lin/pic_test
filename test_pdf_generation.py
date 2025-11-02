#!/usr/bin/env python3
"""
Test script for PDF generation functionality
"""

import os
import sys
import tempfile
import shutil
import subprocess
from pathlib import Path

# Import the PDF generation module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_pdf import create_pdf_from_images


def test_pdf_generation():
    """Test PDF generation with sample images"""
    print("Testing PDF generation...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Test directory: {tmpdir}")
        
        # Copy a few sample images to test directory
        sample_images = [
            "fire_img_0630_0001.png",
            "fire_img_0630_0005.jpg",
            "fire_img_0630_0021.webp"
        ]
        
        for img in sample_images:
            src = img
            if os.path.exists(src):
                dst = os.path.join(tmpdir, img)
                shutil.copy2(src, dst)
                print(f"Copied: {img}")
        
        # Change to test directory
        original_dir = os.getcwd()
        os.chdir(tmpdir)
        
        try:
            # Test PDF creation
            output_file = "test_output.pdf"
            create_pdf_from_images(output_file, "你好 - Test")
            
            # Verify PDF was created
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                print(f"\n✓ PDF created successfully: {output_file}")
                print(f"  File size: {file_size} bytes")
                
                # Basic validation - PDF should have reasonable size
                if file_size > 1000:  # At least 1KB
                    print("✓ PDF has reasonable size")
                    return True
                else:
                    print("✗ PDF size is too small, may be corrupted")
                    return False
            else:
                print("✗ PDF file was not created")
                return False
                
        finally:
            # Return to original directory
            os.chdir(original_dir)


def test_command_line():
    """Test command-line execution"""
    print("\nTesting command-line execution...")
    
    # Test help option
    result = subprocess.run(
        [sys.executable, "generate_pdf.py", "--help"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("✓ Help option works")
    else:
        print("✗ Help option failed")
        return False
    
    return True


def main():
    """Run all tests"""
    print("="*60)
    print("PDF Generation Test Suite")
    print("="*60)
    
    tests_passed = 0
    tests_total = 2
    
    # Test 1: PDF generation
    if test_pdf_generation():
        tests_passed += 1
    
    # Test 2: Command-line
    if test_command_line():
        tests_passed += 1
    
    print("\n" + "="*60)
    print(f"Tests passed: {tests_passed}/{tests_total}")
    print("="*60)
    
    return tests_passed == tests_total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

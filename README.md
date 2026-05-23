# 📄 PDF Toolbox

A modern, feature-rich Python library for comprehensive PDF manipulation and processing. Merge, compress, rotate, scan, extract, and transform PDFs with an elegant API.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen.svg)]()

## ✨ Features

### Core Functionality
- 📑 **Merge PDFs** - Combine multiple PDF files seamlessly
- 🗜️ **Compress** - Reduce file size without quality loss
- 🔄 **Rotate Pages** - Rotate individual or all pages
- 📸 **Scan to PDF** - Convert scanned images to high-quality PDFs
- 📋 **Extract Text** - Extract text from any PDF
- 🖼️ **Extract Images** - Save all images from PDFs
- ✂️ **Split Documents** - Split PDFs by page ranges
- 🔀 **Reorder Pages** - Rearrange pages in any order
- 🔒 **Password Protection** - Encrypt and secure PDFs
- 🔓 **Decrypt** - Unlock password-protected PDFs
- 📝 **Add Watermarks** - Embed watermarks and signatures
- 🏷️ **Metadata Management** - Read and write PDF metadata
- 🔍 **OCR Support** - Optical Character Recognition
- 📊 **Page Operations** - Get page info, dimensions, count

## 🚀 Quick Start

### Installation

```bash
pip install pdf-toolbox
```

### Basic Usage

```python
from pdf_toolbox import PDFToolbox

# Initialize
pdf = PDFToolbox()

# Merge PDFs
pdf.merge(['file1.pdf', 'file2.pdf'], 'merged.pdf')

# Compress PDF
pdf.compress('large.pdf', 'compressed.pdf', quality='high')

# Rotate pages
pdf.rotate('document.pdf', 'rotated.pdf', degrees=90)

# Extract text
text = pdf.extract_text('document.pdf')
print(text)

# Split PDF
pdf.split('document.pdf', 'output_', start_page=1, end_page=5)

# Compress and optimize
pdf.optimize('input.pdf', 'output.pdf', remove_duplicates=True)
```

## 📖 Documentation

### Merge
```python
pdf.merge(
    input_files=['file1.pdf', 'file2.pdf'],
    output_file='merged.pdf',
    page_ranges=None,  # Optional: [(1, 3), (5, 10)]
    bookmark=True      # Add bookmarks
)
```

### Compress
```python
pdf.compress(
    input_file='large.pdf',
    output_file='compressed.pdf',
    quality='high',     # 'low', 'medium', 'high'
    remove_duplicates=True,
    remove_streams=True
)
```

### Rotate
```python
pdf.rotate(
    input_file='document.pdf',
    output_file='rotated.pdf',
    degrees=90,         # 90, 180, 270, or -90
    pages='all'         # 'all' or list [1, 2, 3]
)
```

### Extract Operations
```python
# Extract text
text = pdf.extract_text('document.pdf', page_range=(1, 10))

# Extract images
images = pdf.extract_images('document.pdf', output_dir='./images')

# Extract metadata
metadata = pdf.get_metadata('document.pdf')
```

### Security
```python
# Encrypt with password
pdf.encrypt('document.pdf', 'secured.pdf', password='mypassword')

# Decrypt
pdf.decrypt('secured.pdf', 'unlocked.pdf', password='mypassword')

# Add watermark
pdf.add_watermark(
    input_file='document.pdf',
    output_file='watermarked.pdf',
    watermark_text='CONFIDENTIAL',
    opacity=0.3
)
```

### Split & Reorder
```python
# Split PDF
pdf.split('document.pdf', 'page_', start_page=1, end_page=50)

# Reorder pages
pdf.reorder_pages('document.pdf', 'reordered.pdf', page_order=[3, 1, 2])

# Remove pages
pdf.remove_pages('document.pdf', 'cleaned.pdf', pages_to_remove=[1, 3, 5])
```

### Image to PDF
```python
pdf.images_to_pdf(
    image_files=['scan1.jpg', 'scan2.jpg'],
    output_file='scanned.pdf',
    dpi=300,
    auto_rotate=True
)
```

### OCR (Optical Character Recognition)
```python
pdf.ocr(
    input_file='scanned.pdf',
    output_file='ocr_output.pdf',
    language='eng',     # 'eng', 'fra', 'deu', etc.
    keep_original=False
)
```

## 🔧 Advanced Usage

### Batch Processing
```python
from pdf_toolbox import PDFToolbox

pdf = PDFToolbox()

# Process multiple files
files = ['doc1.pdf', 'doc2.pdf', 'doc3.pdf']
for file in files:
    pdf.compress(file, f'compressed_{file}', quality='medium')
```

### Pipeline Operations
```python
# Chain operations
result = (pdf
    .load('input.pdf')
    .rotate(90)
    .compress(quality='high')
    .add_watermark('DRAFT')
    .save('output.pdf')
)
```

### Custom Configuration
```python
from pdf_toolbox import PDFToolbox, Config

config = Config(
    compression_level=9,
    image_quality=85,
    preserve_metadata=True,
    thread_count=4
)

pdf = PDFToolbox(config=config)
```

## 📋 Supported Formats

- **Input:** PDF, images (JPG, PNG, BMP, TIFF)
- **Output:** PDF (various compression levels)
- **Metadata:** Standard PDF properties (Title, Author, Subject, etc.)

## 🛠️ Requirements

- Python 3.8+
- PyPDF2 - PDF manipulation
- Pillow - Image processing
- opencv-python - Image scanning/processing
- pytesseract - OCR support
- reportlab - PDF generation

## 💻 System Requirements

- Tesseract-OCR (for OCR features)
- ImageMagick (for advanced image operations)

## 🧪 Testing

```bash
pytest tests/ -v
pytest tests/ --cov=pdf_toolbox
```

## 📝 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🐛 Bug Reports & Feature Requests

Please use [GitHub Issues](https://github.com/Langatcorne/pdf-toolbox/issues) to report bugs or request features.

## 📞 Support

For questions and support, please open an issue or check the [documentation](docs/).

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ by Langatcorne**

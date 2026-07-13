"""Core PDF manipulation functionality."""

import os
from pathlib import Path
from typing import List, Optional, Tuple, Union
import logging

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    raise ImportError("PyPDF2 is required. Install with: pip install PyPDF2")

try:
    from PIL import Image
except ImportError:
    raise ImportError("Pillow is required. Install with: pip install Pillow")

logger = logging.getLogger(__name__)


class PDFToolbox:
    """Main PDF manipulation class with comprehensive features."""

    def __init__(self, config=None):
        """Initialize PDFToolbox.
        
        Args:
            config: Optional Config object with custom settings
        """
        self.config = config or {}
        logger.info("PDFToolbox initialized")

    def merge(self, input_files: List[str], output_file: str, 
              page_ranges: Optional[List[Tuple[int, int]]] = None,
              bookmark: bool = True) -> bool:
        """Merge multiple PDF files.
        
        Args:
            input_files: List of PDF file paths to merge
            output_file: Output file path
            page_ranges: Optional list of (start, end) page tuples
            bookmark: Whether to add bookmarks
            
        Returns:
            bool: True if successful
        """
        try:
            writer = PdfWriter()
            
            for pdf_file in input_files:
                if not os.path.exists(pdf_file):
                    logger.error(f"File not found: {pdf_file}")
                    continue
                    
                reader = PdfReader(pdf_file)
                
                if page_ranges:
                    for start, end in page_ranges:
                        for page_num in range(start - 1, min(end, len(reader.pages))):
                            writer.add_page(reader.pages[page_num])
                            if bookmark:
                                writer.add_bookmark(f"{Path(pdf_file).stem} - Page {page_num + 1}")
                else:
                    for page_num, page in enumerate(reader.pages):
                        writer.add_page(page)
                        if bookmark:
                            writer.add_bookmark(f"{Path(pdf_file).stem} - Page {page_num + 1}")
            
            with open(output_file, 'wb') as out:
                writer.write(out)
            
            logger.info(f"Successfully merged {len(input_files)} PDFs to {output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error merging PDFs: {str(e)}")
            return False

    def compress(self, input_file: str, output_file: str,
                 quality: str = 'medium', remove_duplicates: bool = True,
                 remove_streams: bool = True) -> bool:
        """Compress PDF file.
        
        Args:
            input_file: Input PDF file path
            output_file: Output file path
            quality: Compression quality ('low', 'medium', 'high')
            remove_duplicates: Whether to remove duplicate objects
            remove_streams: Whether to remove duplicate streams
            
        Returns:
            bool: True if successful
        """
        try:
            if not os.path.exists(input_file):
                logger.error(f"File not found: {input_file}")
                return False
            
            reader = PdfReader(input_file)
            writer = PdfWriter()
            
            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)
            
            with open(output_file, 'wb') as out:
                writer.write(out)
            
            logger.info(f"Successfully compressed {input_file} to {output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error compressing PDF: {str(e)}")
            return False

    def rotate(self, input_file: str, output_file: str,
               degrees: int = 90, pages: Union[str, List[int]] = 'all') -> bool:
        """Rotate PDF pages.
        
        Args:
            input_file: Input PDF file path
            output_file: Output file path
            degrees: Rotation degrees (90, 180, 270, -90)
            pages: 'all' or list of page numbers
            
        Returns:
            bool: True if successful
        """
        try:
            if not os.path.exists(input_file):
                logger.error(f"File not found: {input_file}")
                return False
            
            reader = PdfReader(input_file)
            writer = PdfWriter()
            
            pages_to_rotate = range(len(reader.pages)) if pages == 'all' else pages
            
            for page_num, page in enumerate(reader.pages):
                if page_num in pages_to_rotate:
                    page.rotate(degrees)
                writer.add_page(page)
            
            with open(output_file, 'wb') as out:
                writer.write(out)
            
            logger.info(f"Successfully rotated {input_file} by {degrees}° to {output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error rotating PDF: {str(e)}")
            return False

    def extract_text(self, input_file: str, page_range: Optional[Tuple[int, int]] = None) -> str:
        """Extract text from PDF.
        
        Args:
            input_file: Input PDF file path
            page_range: Optional (start, end) page tuple
            
        Returns:
            str: Extracted text
        """
        try:
            if not os.path.exists(input_file):
                logger.error(f"File not found: {input_file}")
                return ""
            
            reader = PdfReader(input_file)
            text = ""
            
            if page_range:
                start, end = page_range
                pages = range(start - 1, min(end, len(reader.pages)))
            else:
                pages = range(len(reader.pages))
            
            for page_num in pages:
                text += reader.pages[page_num].extract_text()
            
            logger.info(f"Successfully extracted text from {input_file}")
            return text
            
        except Exception as e:
            logger.error(f"Error extracting text: {str(e)}")
            return ""

    def split(self, input_file: str, output_prefix: str,
              start_page: int = 1, end_page: Optional[int] = None) -> bool:
        """Split PDF into individual pages.
        
        Args:
            input_file: Input PDF file path
            output_prefix: Prefix for output files
            start_page: Starting page number
            end_page: Ending page number
            
        Returns:
            bool: True if successful
        """
        try:
            if not os.path.exists(input_file):
                logger.error(f"File not found: {input_file}")
                return False
            
            reader = PdfReader(input_file)
            total_pages = len(reader.pages)
            
            if end_page is None:
                end_page = total_pages
            
            for page_num in range(start_page - 1, min(end_page, total_pages)):
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])
                
                output_file = f"{output_prefix}{page_num + 1}.pdf"
                with open(output_file, 'wb') as out:
                    writer.write(out)
            
            logger.info(f"Successfully split {input_file} into pages {start_page}-{end_page}")
            return True
            
        except Exception as e:
            logger.error(f"Error splitting PDF: {str(e)}")
            return False

    def remove_pages(self, input_file: str, output_file: str,
                    pages_to_remove: List[int]) -> bool:
        """Remove specific pages from PDF.
        
        Args:
            input_file: Input PDF file path
            output_file: Output file path
            pages_to_remove: List of page numbers to remove
            
        Returns:
            bool: True if successful
        """
        try:
            if not os.path.exists(input_file):
                logger.error(f"File not found: {input_file}")
                return False
            
            reader = PdfReader(input_file)
            writer = PdfWriter()
            
            for page_num, page in enumerate(reader.pages):
                if (page_num + 1) not in pages_to_remove:
                    writer.add_page(page)
            
            with open(output_file, 'wb') as out:
                writer.write(out)
            
            logger.info(f"Successfully removed pages from {input_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error removing pages: {str(e)}")
            return False

    def get_metadata(self, input_file: str) -> dict:
        """Get PDF metadata.
        
        Args:
            input_file: Input PDF file path
            
        Returns:
            dict: Metadata dictionary
        """
        try:
            if not os.path.exists(input_file):
                logger.error(f"File not found: {input_file}")
                return {}
            
            reader = PdfReader(input_file)
            metadata = reader.metadata
            
            return metadata if metadata else {}
            
        except Exception as e:
            logger.error(f"Error getting metadata: {str(e)}")
            return {}

    def get_page_count(self, input_file: str) -> int:
        """Get total page count.
        
        Args:
            input_file: Input PDF file path
            
        Returns:
            int: Number of pages
        """
        try:
            if not os.path.exists(input_file):
                logger.error(f"File not found: {input_file}")
                return 0
            
            reader = PdfReader(input_file)
            return len(reader.pages)
            
        except Exception as e:
            logger.error(f"Error getting page count: {str(e)}")
            return 0

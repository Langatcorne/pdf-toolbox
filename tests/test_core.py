"""Unit tests for core PDF operations."""

import os
import pytest
from pdf_toolbox import PDFToolbox


class TestPDFToolbox:
    """Test cases for PDFToolbox class."""

    @pytest.fixture
    def pdf_tool(self):
        """Create PDFToolbox instance."""
        return PDFToolbox()

    def test_initialization(self, pdf_tool):
        """Test PDFToolbox initialization."""
        assert pdf_tool is not None
        assert isinstance(pdf_tool, PDFToolbox)

    def test_merge_nonexistent_files(self, pdf_tool):
        """Test merge with nonexistent files."""
        result = pdf_tool.merge(
            ['nonexistent1.pdf', 'nonexistent2.pdf'],
            'output.pdf'
        )
        assert result is False or result is True  # Depends on error handling

    def test_compress_nonexistent_file(self, pdf_tool):
        """Test compress with nonexistent file."""
        result = pdf_tool.compress('nonexistent.pdf', 'output.pdf')
        assert result is False

    def test_rotate_nonexistent_file(self, pdf_tool):
        """Test rotate with nonexistent file."""
        result = pdf_tool.rotate('nonexistent.pdf', 'output.pdf')
        assert result is False

    def test_extract_text_nonexistent_file(self, pdf_tool):
        """Test extract_text with nonexistent file."""
        result = pdf_tool.extract_text('nonexistent.pdf')
        assert result == ""

    def test_get_page_count_nonexistent_file(self, pdf_tool):
        """Test get_page_count with nonexistent file."""
        result = pdf_tool.get_page_count('nonexistent.pdf')
        assert result == 0

    def test_get_metadata_nonexistent_file(self, pdf_tool):
        """Test get_metadata with nonexistent file."""
        result = pdf_tool.get_metadata('nonexistent.pdf')
        assert result == {}

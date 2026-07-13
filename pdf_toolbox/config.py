"""Configuration module for PDFToolbox."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """Configuration class for PDFToolbox."""
    
    compression_level: int = 6
    image_quality: int = 85
    preserve_metadata: bool = True
    thread_count: int = 4
    temp_dir: Optional[str] = None
    output_dir: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert config to dictionary.
        
        Returns:
            dict: Configuration as dictionary
        """
        return {
            'compression_level': self.compression_level,
            'image_quality': self.image_quality,
            'preserve_metadata': self.preserve_metadata,
            'thread_count': self.thread_count,
            'temp_dir': self.temp_dir,
            'output_dir': self.output_dir,
        }

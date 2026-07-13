# Contributing to PDF Toolbox

We welcome contributions! Here's how you can help:

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/pdf-toolbox.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\\Scripts\\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`

## Development Workflow

1. Create a new branch for your feature: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests: `pytest tests/ -v`
4. Format code: `black pdf_toolbox`
5. Commit changes: `git commit -am 'Add feature'`
6. Push to your fork: `git push origin feature/your-feature`
7. Submit a pull request

## Code Standards

- Follow PEP 8
- Use type hints
- Add docstrings to all functions
- Write unit tests for new features
- Maintain >80% code coverage

## Report Issues

Use GitHub Issues to report bugs or request features.

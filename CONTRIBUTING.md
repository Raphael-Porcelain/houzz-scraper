# Contributing to Houzz Scraper

Thank you for your interest in contributing to the Houzz Scraper project! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Getting Started

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/houzz-scraper.git
   cd houzz-scraper
   ```

2. Install dependencies with uv:
   ```bash
   uv sync --group dev
   ```

3. Install pre-commit hooks:
   ```bash
   uv run pre-commit install --hook-type commit-msg --hook-type pre-push
   ```

## Development Workflow

### Code Quality

This project uses `ruff` for linting and formatting:

```bash
# Run linting with auto-fix
uv run ruff check . --fix

# Format code
uv run ruff format .
```

### Testing

Run tests with pytest:

```bash
# Run all tests with coverage
uv run pytest

# Run specific test file
uv run pytest tests/test_specific.py

# Run with coverage report
uv run pytest --cov=src --cov-report=term-missing
```

### Type Checking

Run type checking with mypy:

```bash
uv run mypy src
```

## Code Style Guidelines

- **Line length**: 88 characters
- **Python version**: 3.11+
- **Naming conventions**:
  - Functions and variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`
- **Type hints**: Required on all functions
- **Docstrings**: Google-style docstrings with Args/Returns/Raises sections
- **Imports**: Organized as stdlib → third-party → local

Example function:

```python
def extract_emails(soup: BeautifulSoup) -> list[str]:
    """Extract email addresses from a BeautifulSoup object.

    Args:
        soup: A BeautifulSoup object to extract emails from.

    Returns:
        A list of unique email addresses found in the page.

    Raises:
        ValueError: If soup is None or invalid.
    """
    # Implementation
```

## Git Workflow

### Branching

Use conventional branch names:

- `feat/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation changes
- `refactor/description` - Code refactoring
- `test/description` - Test additions/changes
- `chore/description` - Maintenance tasks

### Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/). Use `uv run cz commit` for guided commits:

```bash
uv run cz commit
```

Format: `type(scope): description`

Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Test changes
- `chore:` - Maintenance tasks
- `perf:` - Performance improvements

Examples:
```
feat(spider): add support for pagination limit
fix(utils): handle empty email lists correctly
docs(readme): update installation instructions
```

### Pull Requests

1. Create a new branch from `main`
2. Make your changes following the code style guidelines
3. Add tests for new functionality
4. Ensure all tests pass and coverage is maintained
5. Update documentation as needed
6. Submit a pull request with a clear description

## Security

- Never commit secrets or API keys
- Use environment variables for sensitive data
- Add `.env` to `.gitignore`
- Run `detect-secrets` pre-commit hook

## Questions or Issues?

Feel free to:
- Open an issue for bugs or feature requests
- Start a discussion for questions
- Reach out to maintainers

Thank you for contributing! 🎉

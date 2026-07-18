# Contributing to FastAPI Workshop

Thank you for your interest in contributing! This project is designed for
beginners, so do not hesitate to ask questions by opening an issue.

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/fastapi-workshop.git
   cd fastapi-workshop
   ```
3. Create a **virtual environment** and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Run the **tests** to make sure everything works:
   ```bash
   pytest tests/ -v
   ```

## Making Changes

1. Create a new **branch** for your work:
   ```bash
   git checkout -b fix/issue-number-short-description
   ```
2. Make your changes. Keep commits small and focused.
3. Run the tests again to verify nothing is broken:
   ```bash
   pytest tests/ -v
   ```
4. **Commit** with a clear message:
   ```bash
   git commit -m "fix: short description of what you fixed (#issue-number)"
   ```
5. **Push** your branch:
   ```bash
   git push origin fix/issue-number-short-description
   ```
6. Open a **Pull Request** on GitHub against the `main` branch.

## Code Style

- Follow PEP 8.
- Use type hints where possible.
- Add docstrings to public functions.
- Keep functions short and focused.

## Reporting Bugs

If you find a bug not covered by existing issues, please open a new issue with:
- A clear title
- Steps to reproduce
- Expected vs actual behavior
- The file and line number if you can find it

## Code of Conduct

Be respectful and constructive. We are all here to learn.

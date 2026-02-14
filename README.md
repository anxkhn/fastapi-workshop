# FastAPI Workshop

A tiny FastAPI application built for practicing open-source contributions.
This project is designed for third-year CS students participating in
contribution workshops and open-source programs.

## Features

- Health check endpoint
- Arithmetic sum endpoint
- User profile CRUD (in-memory store)
- Profile search with pagination

## Quick Start

```bash
# Clone the repository
git clone https://github.com/anxkhn/fastapi-workshop.git
cd fastapi-workshop

# Create a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the tests
pytest tests/

# Start the development server
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Path                  | Description              |
|--------|-----------------------|--------------------------|
| GET    | `/health`             | Health check             |
| GET    | `/sum?a=1&b=2`        | Compute sum of two ints  |
| GET    | `/profile`            | Create a new profile     |
| GET    | `/profile/{username}` | Get a profile by name    |
| DELETE | `/profile/{username}` | Delete a profile         |
| GET    | `/search?q=term`      | Search profiles          |

## Running Tests

```bash
pytest tests/ -v
```

## Project Structure

```
fastapi-workshop/
  app/
    __init__.py
    main.py       # FastAPI application and route handlers
    models.py     # Pydantic data models
    store.py      # In-memory data store
  tests/
    conftest.py       # Shared test fixtures
    test_health.py    # Health endpoint tests
    test_sum.py       # Sum endpoint tests
    test_profile.py   # Profile endpoint tests
    test_search.py    # Search endpoint tests
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started.

## License

MIT

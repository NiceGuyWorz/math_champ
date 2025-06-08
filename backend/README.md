# Math Champ Backend

This is a simple FastAPI backend that generates math problems for the mobile app.

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Usage

Send a GET request to `/generate/<topic>` where `<topic>` is one of:

- `sumatorias`
- `algebra`

Optionally, you can specify a `timer` query parameter indicating the time limit in seconds.

# Alert Explainer API

A FastAPI service that stores alerts in SQLite and generates human-readable explanations using fixed rules based on alert severity, metric value, and threshold.

## Project Structure

```text
.
├── database.py                 # SQLite engine, session, and ORM base
├── main.py                     # FastAPI app and database table initialization
├── models.py                   # SQLAlchemy Alert model
├── requirements.txt            # Project dependencies
├── routers/
│   └── alerts.py               # Alert and explanation endpoints
├── schemas.py                  # Request and response models
├── services/
│   └── explainer.py            # Rule-based explanation generation
├── test_alerts.py              # API tests
└── docs/
    └── adr/
        ├── 0001-rule-based-explanations.md
        └── 0002-human-approval-for-alert-summaries.md
```

The SQLite database file, `alerts.db`, is created in the working directory when the app initializes.

## Alert Fields

Create-alert requests require:

| Field | Type | Description |
| --- | --- | --- |
| `title` | string | Alert title |
| `severity` | string | One of `critical`, `warning`, or `info` |
| `source` | string | Alert source |
| `metric_name` | string | Name of the monitored metric |
| `metric_value` | number | Current metric value |
| `threshold` | number | Metric threshold |

Alert responses also include `id` (integer) and `created_at` (date-time).

## API Endpoints

| Method | Path | Status codes | Description |
| --- | --- | --- | --- |
| `GET` | `/` | `200` | Health/status response |
| `POST` | `/alerts/` | `201`, `422` | Create an alert; `422` for an invalid request body |
| `GET` | `/alerts/` | `200` | List all alerts |
| `GET` | `/alerts/{alert_id}` | `200`, `404`, `422` | Retrieve an alert; `404` if it does not exist, `422` if the ID is not an integer |
| `GET` | `/alerts/{alert_id}/explain` | `200`, `404`, `422` | Generate an explanation; `404` if the alert does not exist, `422` if the ID is not an integer |
| `POST` | `/alerts/{alert_id}/explain` | `200`, `404`, `422` | Generate an explanation; `404` if the alert does not exist, `422` if the ID is not an integer |

## Install and Run on Windows

Run these commands in PowerShell from the project directory. Python and the Python launcher (`py`) must be installed.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

If PowerShell blocks virtual-environment activation, allow it for the current process and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

## Run Tests

With the virtual environment activated, run:

```powershell
python -m pytest test_alerts.py -v
```

## Architecture Decision Records

- [Rule-Based Explanations](docs/adr/0001-rule-based-explanations.md)
- [Human Approval for Alert Summaries](docs/adr/0002-human-approval-for-alert-summaries.md)

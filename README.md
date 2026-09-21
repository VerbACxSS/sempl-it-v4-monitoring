# SEMPL-IT V4 monitoring

This is the monitoring module of SEMPL-IT, a web application designed to simplify and analyze Italian administrative documents.

## WebApp

The SEMPL-IT web app consists of the following repositories:

- Frontend: https://github.com/VerbACxSS/sempl-it-v4-frontend
- Backend: https://github.com/VerbACxSS/sempl-it-v4-backend
- Monitoring Module: https://github.com/VerbACxSS/sempl-it-v4-monitoring

## Getting Started

### Pre-requisites

This application is developed using the FastAPI framework.

To run the application locally, Python 3.12 is required.

Alternatively, the application can be run using Docker. The current setup uses:

- Python 3.12.8 (`python:3.12.8-slim-bookworm`)
- uv 0.8.12
- Docker 29.8.0
- Docker Compose v5.5.1

### Configuration

The Docker Compose setup supports the following environment variables:

```text
PYTHONUNBUFFERED=1
MONITORING_API_KEY=...
MYSQL_USER=...
MYSQL_PASSWORD=...
MYSQL_DATABASE=...
MYSQL_ROOT_PASSWORD=...
```

The monitoring service connects to the database using the internal Docker Compose hostname `sempl-it-monitoring-database` on port `3306`.

### Using `python` and `pip`

Create a Python virtual environment:

```shell
python3 -m venv venv
```

Activate the virtual environment:

```shell
source venv/bin/activate    # Linux/macOS
./venv/Scripts/activate     # Windows
```

Install all dependencies from `requirements.txt`:

```shell
pip install -r requirements.txt
```

Start the server:

```shell
python -m uvicorn app.app:app --host=0.0.0.0 --port=30050 --log-level=info --timeout-keep-alive=60
```

When started directly in this way, the monitoring API is available at `http://localhost:30050`.

### Using `docker`

Run the application using `docker compose`:

```shell
docker compose up --build -d
```

The Docker Compose setup exposes:

- Monitoring API: `http://localhost:10050`
- phpMyAdmin: `http://localhost:20050`

The monitoring API runs internally on port `30050` and is mapped to port `10050` on the host.

## Built With

- FastAPI
- MySQL
- phpMyAdmin
- uv

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This contribution is a result of the research conducted within the framework of the PRIN 2020 (Progetti di Rilevante Interesse Nazionale) "VerbACxSS: on analytic verbs, complexity, synthetic verbs, and simplification. For accessibility" (Prot. 2020BJKB9M), funded by the Italian Ministero dell'Università e della Ricerca.

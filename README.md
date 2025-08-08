# Sanlam Data Engineering Take-Home Challenge

This project is a compact batch pipeline for ingesting, processing, and querying the Financial Sanctions List (XML) as part of the Sanlam Data Engineering Take-Home.

---

## 🏗 Architecture

See `/diagrams` for open-source and AWS-based architecture diagrams.

---

## 🚀 Pipeline Components

- **Ingestion**: Parses XML to CSV
- **Processing**: Cleans data, normalizes fields, outputs Parquet
- **Query Layer**: Easily extendable to DuckDB, PostgreSQL
- **Scheduling**: Python scheduler (`schedule.py`)
- **Dockerized**: Runs everything in a container
- **Orchestrated**: Optional Airflow DAG

---

## 📦 How to Run (Locally)

```bash
# Build container
docker build -t sanlam-pipeline .

# Run container
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/output:/app/output sanlam-pipeline

```
---

## ⏰ To Schedule with Python

```bash
python scripts/schedule.py
```

---

## ☁️ Airflow Orchestration

# Example airflow trigger
airflow dags trigger sanctions_batch_pipeline

---

## ✅ Requirements

Python 3.11+

Docker

Airflow (optional)

---

Now let's move on to:

---

## 🚀 Streamlit App: Sanctions Data Explorer

This app:

- Loads `sanctions_cleaned.parquet`
- Shows it as a filterable table
- Supports search by:
  - Full Name
  - Nationality
  - Alias

---

## 🧪 How to Run the App Locally

From inside your project folder:
```bash
streamlit run streamlit_app.py
```

---

This will:

Load sanctions_cleaned.parquet from the output/ directory

Let you:

🔍 Search by Full Name

🌍 Filter by Nationality

🧛 Search by Alias

---

## ▶️ How to Run It
Make sure you're in the root of the project directory:
```bash
docker-compose up --build
```

Then open your browser at:

[http://localhost:8501](http://localhost:8501)



# 📄 Scalable Intelligent Document Processing (IDP) Pipeline

## Overview
An end-to-end Intelligent Document Processing (IDP) microservice designed for production environments. This system ingests unstructured text and files, structures the data using custom feature engineering pipelines, and routes the documents through a machine learning classification engine. 

Built with a heavy emphasis on **system observability, infrastructure health, and data reliability**, this project moves beyond isolated Jupyter Notebooks to demonstrate full-stack AI/ML system architecture.

## ⚙️ Core Architecture & Features
* **Automated Data Ingestion:** Asynchronous RESTful API built with FastAPI to handle raw text and file payloads. Includes built-in data validation and edge-case handling.
* **Feature Engineering Pipeline:** Pandas-driven preprocessing to normalize unstructured text and extract structured ML features (e.g., financial markers, keyword frequency, document length).
* **ML Classification Engine:** Lightweight inference node for automated document routing (e.g., Invoices vs. Application Forms) complete with confidence scoring.
* **System Observability:** Custom monitoring decorators and centralized logging to actively track infrastructure health, sub-system execution latency (in milliseconds), and pipeline failures.
* **Containerized Deployment:** Fully Dockerized architecture ensuring environment consistency, scalability, and rapid deployment.

## 🗂️ Project Structure
```text
production-idp-pipeline/
├── api/
│   └── main.py              # FastAPI routing and async ingestion handlers
├── core/
│   ├── processor.py         # Pandas text normalization & feature engineering
│   └── classifier.py        # ML inference and confidence scoring
├── infrastructure/
│   └── monitoring.py        # Centralized logging and latency decorators
├── Dockerfile               # Container configuration
└── requirements.txt         # System dependencies

🛠️ Tech Stack
Core API: FastAPI, Uvicorn, Python-Multipart

Data Processing: Pandas

Machine Learning Context: Scikit-learn architecture

Infrastructure & DevOps: Docker, Custom Python Logging

📡 API Reference & Example Output
Endpoint: POST /api/v1/ingest
Accepts multipart/form-data (either a .txt/.csv file upload or a raw_text string).

Example Successful Response (200 OK):

JSON
{
  "status": "healthy",
  "result": {
    "document_type": "Invoice",
    "confidence_score": 0.92
  }
}
📊 System Observability
The application features built-in infrastructure monitoring. Sub-system execution times and edge-case rejections are automatically logged to a local system_health.log file to ensure pipeline transparency.

Example Log Output:

Plaintext
2026-05-16 20:26:01,102 - INFO - IDP_Oversight - --- New Ingestion Request ---
2026-05-16 20:26:01,104 - INFO - IDP_Oversight - Processing raw text payload.
2026-05-16 20:26:01,105 - INFO - IDP_Oversight - Starting text normalization and extraction.
2026-05-16 20:26:01,118 - INFO - IDP_Oversight - Sub-system 'extract_and_clean' executed in 13.02ms.
2026-05-16 20:26:01,119 - INFO - IDP_Oversight - Running inference on extracted document features.
2026-05-16 20:26:01,121 - INFO - IDP_Oversight - Inference complete: Invoice (Confidence: 0.92)
2026-05-16 20:26:01,122 - INFO - IDP_Oversight - Sub-system 'predict' executed in 3.15ms.
2026-05-16 20:26:01,123 - INFO - IDP_Oversight - Pipeline execution complete. Returning response.
🚀 Getting Started
Option 1: Run with Docker (Recommended)
Ensure Docker is installed and running on your system.

Bash
# Clone the repository
git clone [https://github.com/harsh7266/production-idp-pipeline.git](https://github.com/harsh7266/production-idp-pipeline.git)
cd production-idp-pipeline

# Build the Docker image
docker build -t idp-system .

# Run the container
docker run -p 8000:8000 idp-system
Option 2: Run Locally (Python 3.10+)
Bash
# Clone the repository
git clone [https://github.com/harsh7266/production-idp-pipeline.git](https://github.com/harsh7266/production-idp-pipeline.git)
cd production-idp-pipeline

# Install dependencies
python -m pip install -r requirements.txt

# Start the server
python -m uvicorn api.main:app --reload
Once the server is running, navigate to http://127.0.0.1:8000/docs to test the pipeline using the built-in interactive Swagger UI.

# 📄 Scalable Intelligent Document Processing (IDP) Pipeline

## Overview
An end-to-end Intelligent Document Processing (IDP) microservice designed for production environments. This system ingests unstructured text and files, structures the data using custom feature engineering pipelines, and routes the documents through a machine learning classification engine. 

Built with a heavy emphasis on **system observability, infrastructure health, and data reliability**, this project moves beyond isolated Jupyter Notebooks to demonstrate full-stack AI/ML system architecture.

## ⚙️ Core Architecture & Features
* **Automated Data Ingestion:** RESTful API built with FastAPI to handle raw text and file payloads. Includes built-in data validation and edge-case handling.
* **Feature Engineering Pipeline:** Pandas-driven preprocessing to normalize unstructured text and extract structured ML features (e.g., financial markers, keyword frequency, document length).
* **ML Classification Engine:** Lightweight inference node for automated document routing (e.g., Invoices vs. Application Forms) complete with confidence scoring.
* **System Observability:** Custom monitoring decorators and centralized logging to actively track infrastructure health, sub-system execution latency (in milliseconds), and pipeline failures.
* **Containerized Deployment:** Fully Dockerized architecture ensuring environment consistency, scalability, and rapid deployment.

## 🛠️ Tech Stack
* **Core API:** FastAPI, Uvicorn, Python-Multipart
* **Data Processing:** Pandas
* **Machine Learning Context:** Scikit-learn architecture
* **Infrastructure & DevOps:** Docker, Custom Python Logging

## 🚀 Getting Started

### Option 1: Run with Docker (Recommended)
Ensure Docker is installed and running on your system.
```bash
# Clone the repository
git clone [https://github.com/harsh7266/production-idp-pipeline.git](https://github.com/harsh7266/production-idp-pipeline.git)
cd production-idp-pipeline

# Build the Docker image
docker build -t idp-system .

# Run the container
docker run -p 8000:8000 idp-system
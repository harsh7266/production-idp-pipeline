from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from core.processor import extract_and_clean
from core.classifier import DocumentClassifier
from infrastructure.monitoring import sys_logger, monitor_performance

app = FastAPI(
    title="IDP Production Node",
    description="Intelligent Document Processing API for classifying unstructured text."
)

# Initialize the ML engine at startup
classifier_engine = DocumentClassifier()

@app.post("/api/v1/ingest")
async def ingest_document(
    file: UploadFile = File(None), 
    raw_text: str = Form(None)
):
    """
    Accepts either a file upload (.txt, .csv) or raw text via form data.
    """
    sys_logger.info("--- New Ingestion Request ---")
    
    # Data extraction
    content = ""
    if file:
        sys_logger.info(f"Processing uploaded file: {file.filename}")
        if not file.filename.endswith(('.txt', '.csv')):
            sys_logger.warning("Invalid file format. Rejecting payload.")
            raise HTTPException(status_code=400, detail="System only accepts .txt or .csv")
        
        file_bytes = await file.read()
        content = file_bytes.decode('utf-8')
    elif raw_text:
        sys_logger.info("Processing raw text payload.")
        content = raw_text
    else:
        sys_logger.warning("Empty payload received.")
        raise HTTPException(status_code=400, detail="Provide either a file or raw_text.")

    if not content.strip():
        raise HTTPException(status_code=400, detail="Provided content is empty.")

    # 1. Route through Pandas pipeline
    structured_data = extract_and_clean(content)
    
    # 2. Route through ML engine
    inference_result = classifier_engine.predict(structured_data)
    
    sys_logger.info("Pipeline execution complete. Returning response.")
    
    return {
        "status": "healthy", 
        "result": inference_result
    }
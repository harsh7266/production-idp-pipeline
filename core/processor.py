import pandas as pd
from infrastructure.monitoring import sys_logger, monitor_performance

@monitor_performance
def extract_and_clean(raw_text: str) -> pd.DataFrame:
    """
    Simulates extracting entities from a document and structuring it.
    In a production environment, this is where OCR or regex pipelines would live.
    """
    sys_logger.info("Starting text normalization and extraction.")
    
    try:
        # Normalizing text
        text_lower = raw_text.lower()
        
        # Feature engineering: Extracting specific markers
        features = {
            "doc_length": len(raw_text),
            "contains_amount": "$" in raw_text or "₹" in raw_text or "total" in text_lower,
            "keyword_invoice": "invoice" in text_lower or "bill" in text_lower,
            "keyword_application": "apply" in text_lower or "application" in text_lower,
            "keyword_urgent": "urgent" in text_lower or "immediate" in text_lower
        }
        
        # Structuring into Pandas DataFrame
        df = pd.DataFrame([features])
        sys_logger.info("Data structured successfully into Pandas DataFrame.")
        
        return df
        
    except Exception as e:
        sys_logger.error(f"Pipeline failure during extraction: {e}")
        raise
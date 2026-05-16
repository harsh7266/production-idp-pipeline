import logging
import time
from functools import wraps

# Centralized System Logger
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
sys_logger = logging.getLogger("IDP_Oversight")

def monitor_performance(func):
    """Decorator to track pipeline execution speed and system health."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            duration = round((time.time() - start_time) * 1000, 2)
            sys_logger.info(f"Sub-system '{func.__name__}' executed in {duration}ms.")
            return result
        except Exception as e:
            sys_logger.error(f"Critical failure in '{func.__name__}': {str(e)}")
            raise
    return wrapper
import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = "log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'{log_dir}/api.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

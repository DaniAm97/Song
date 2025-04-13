import logging
import os
import sys

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Logger configuration
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# File Handler
file_handler = logging.FileHandler('logs/api_test.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Console Handler (send to stdout so pytest will catch it!)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Add handlers to the logger (make sure no duplicates)
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

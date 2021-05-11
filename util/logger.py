import logging


def log_response(response, context=""):
    """
    logs status_code and JSON response
    """
    json = response.json()

    logger = logging.getLogger(context)
    logger.info(response.status_code)
    logger.info(json)

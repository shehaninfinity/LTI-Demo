# backend/services/pdf_similarity.py
import random

def check_pdf_similarity(pdf_id):
    """
    Dummy function to simulate PDF similarity checking.
    In production, implement your own logic or use a library to extract text and compare PDFs.
    """
    # Return a random similarity score between 0 and 1 for demo purposes.
    return round(random.uniform(0, 1), 2)

# backend/services/pdf_similarity.py

import random

def check_pdf_similarity(pdf_id):
    """
    Return a random similarity score for demonstration.
    In a real app, you'd parse the PDF, compare text, etc.
    """
    return round(random.uniform(0, 1), 2)

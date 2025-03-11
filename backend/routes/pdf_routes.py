# backend/routes/pdf_routes.py
from flask import Blueprint, request, jsonify
from services.pdf_similarity import check_pdf_similarity

pdf_bp = Blueprint('pdf', __name__)

# Dummy list of PDFs; in production, you might load these from a directory or database.
PDFS = [
    {"id": 1, "name": "document1.pdf"},
    {"id": 2, "name": "document2.pdf"},
    {"id": 3, "name": "document3.pdf"}
]

@pdf_bp.route('/', methods=['GET'])
def list_pdfs():
    return jsonify(PDFS), 200

@pdf_bp.route('/similarity', methods=['POST'])
def pdf_similarity():
    data = request.json
    pdf_id = data.get('pdf_id')
    if not pdf_id:
        return jsonify({'error': 'Missing pdf_id'}), 400

    # Dummy similarity check (replace with actual logic in production)
    similarity_score = check_pdf_similarity(pdf_id)
    return jsonify({'pdf_id': pdf_id, 'similarity': similarity_score}), 200

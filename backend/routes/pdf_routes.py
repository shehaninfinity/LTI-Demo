# backend/routes/pdf_routes.py

from flask import Blueprint, jsonify, request
from services.pdf_similarity import check_pdf_similarity

pdf_bp = Blueprint('pdf', __name__)

PDFS = [
    {"id": 1, "name": "doc1.pdf"},
    {"id": 2, "name": "doc2.pdf"},
    {"id": 3, "name": "doc3.pdf"},
]

@pdf_bp.route('/', methods=['GET'])
def list_pdfs():
    return jsonify(PDFS), 200

@pdf_bp.route('/similarity', methods=['POST'])
def pdf_similarity():
    data = request.json
    pdf_id = data.get('pdf_id')
    if not pdf_id:
        return jsonify({"error": "No pdf_id provided"}), 400

    score = check_pdf_similarity(pdf_id)
    return jsonify({"pdf_id": pdf_id, "similarity": score}), 200

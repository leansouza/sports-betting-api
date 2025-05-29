
from flask import Blueprint, jsonify
import json

odds_bp = Blueprint('odds', __name__)

@odds_bp.route('/odds', methods=['GET'])
def get_odds():
    with open('data/mock_odds.json') as f:
        odds = json.load(f)
    return jsonify(odds)

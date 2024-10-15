from flask import Flask, request, jsonify
import pandas as pd
from extract_features import extract_features
from train_model import run_model
from flask_cors import CORS

app = Flask(__name__)  # Créez d'abord l'application Flask
CORS(app)  # Ensuite, appliquez CORS

# Charger le modèle KNN
model = run_model()

@app.route('/verifier', methods=['POST'])
def verifier_mot_de_passe():
    """Vérifie la force d'un mot de passe."""
    data = request.get_json()  # Récupérer les données JSON de la requête
    mot_de_passe = data.get('password')  # Récupérer le mot de passe

    if not mot_de_passe:
        return jsonify({'error': 'Aucun mot de passe fourni.'}), 400

    # Extraction des caractéristiques
    caracteristiques = pd.DataFrame([extract_features(mot_de_passe)])

    # Prédiction avec le modèle
    prediction = model.predict(caracteristiques)

    # Interpréter la prédiction
    resultats = {0: "faible", 1: "moyen", 2: "fort"}
    force_mot_de_passe = resultats[prediction[0]]

    return jsonify({'force': force_mot_de_passe})

if __name__ == '__main__':
    app.run(debug=True)

import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'; // Assurez-vous d'importer votre fichier CSS personnalisé

function App() {
  const [motDePasse, setMotDePasse] = useState('');
  const [resultat, setResultat] = useState('');
  const [motDePasseGenere, setMotDePasseGenere] = useState('');

  const verifierMotDePasse = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/verifier', { password: motDePasse });
      setResultat(`Le mot de passe est : ${response.data.force}`);
    } catch (error) {
      console.error("Erreur lors de la vérification :", error);
      setResultat('Erreur lors de la vérification du mot de passe.');
    }
  };

  const genererMotDePasse = () => {
    const caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";
    let motDePasseGenere = "";
    for (let i = 0; i < 12; i++) {  // Longueur du mot de passe généré
      motDePasseGenere += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
    }
    setMotDePasseGenere(motDePasseGenere);  // Affiche le mot de passe généré
  };

  return (
    <div className="container mt-5">
      <div className="card text-center">
        <div className="card-header">
          <h1 className="display-4">Vérificateur de mot de passe</h1>
        </div>
        <div className="card-body">
          <div className="input-group mb-3">
            <input
              type="password"
              className="form-control"
              value={motDePasse}
              onChange={(e) => setMotDePasse(e.target.value)}
              placeholder="Entrez votre mot de passe"
              aria-label="Mot de passe"
            />
            <button className="btn btn-primary" type="button" onClick={verifierMotDePasse}>
              Vérifier
            </button>
          </div>
          {resultat && <p className="mt-3">{resultat}</p>}
          
          <button className="btn btn-secondary mt-3" type="button" onClick={genererMotDePasse}>
            Générer un mot de passe
          </button>
          {motDePasseGenere && <p className="mt-3">Mot de passe généré : <strong>{motDePasseGenere}</strong></p>}
        </div>
        <div className="card-footer text-muted">
          Créez un mot de passe fort pour protéger vos informations !
        </div>
      </div>
    </div>
  );
}

export default App;

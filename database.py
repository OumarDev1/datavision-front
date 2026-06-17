"""
Couche de stockage des prédictions (SQLite).
Chaque prédiction faite par l'utilisateur est enregistrée ici, puis relue
par la page Historique. Le fichier predictions.db est créé automatiquement
à la racine du projet, à côté de app.py.
"""
import sqlite3
from datetime import datetime
import pandas as pd

DB_PATH = "predictions.db"


def init_db():
    """Crée la table des prédictions si elle n'existe pas encore."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            date_heure  TEXT    NOT NULL,
            humidite    REAL    NOT NULL,
            temperature REAL    NOT NULL,
            co2         REAL    NOT NULL,
            o2          REAL    NOT NULL,
            statut      TEXT    NOT NULL,
            precision   REAL
        )
        """
    )
    conn.commit()
    conn.close()


def save_prediction(humidite, temperature, co2, o2, statut, precision=None):
    """
    Enregistre une prédiction.
    - statut    : la classe prédite ("Optimal" / "Avertissement" / "Critique"
                  ou "Faible" / "Modéré" / "Élevé")
    - precision : confiance du modèle entre 0 et 1 (ex. 0.924)
    """
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO predictions "
        "(date_heure, humidite, temperature, co2, o2, statut, precision) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            humidite, temperature, co2, o2, statut, precision,
        ),
    )
    conn.commit()
    conn.close()


def get_predictions():
    """Renvoie toutes les prédictions, de la plus récente à la plus ancienne."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM predictions ORDER BY id DESC", conn)
    conn.close()
    return df


def vider_historique():
    """Supprime toutes les prédictions (utile pour les tests)."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM predictions")
    conn.commit()
    conn.close()

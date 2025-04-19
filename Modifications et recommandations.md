# Modifications et recommandations

## Généralités

- Création de GitHub Actions.
- Modifications de `pre-commit`
    - Remplacement de _flake8_ et _black_ par __Ruff__
    - Ajout de hooks basiques : `check-yaml`, `check-docstring`, `end-of-file-fixer`, _etc._

## Application

- Ajout de `python-dotenv` dans `requirements-dev.txt` pour la gestion des variables d'environnement via un fichier `.env`.
- Création des routes `/healthz` et `/readyz`.
- Ajout de Gunicorn (présent dans `requirements.txt`) pour un déploiement en production.
- Ajout de tests unitaires sur la route `health` uniquement pour démonstration.

### Lancement de l'application avec Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8888 src:application
```
### Suggestions complémentaires

- Passage de Flask à FastAPI pour gérer l'asynchrone
- Documentation du code (Docstring)

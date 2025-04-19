# Modifications et recommandations

## Généralités

- Mise en place d'une intégration continue via GitHub Actions.
- Mise à jour de la configuration `pre-commit` :
    - Remplacement de *flake8* et *black* par **Ruff**.
    - Ajout de hooks basiques : `check-yaml`, `check-docstring`, `end-of-file-fixer`, etc.

## Application

- Ajout de `python-dotenv` dans `requirements-dev.txt` pour la gestion des variables d'environnement via un fichier `.env`.
- Création des routes `/healthz` et `/readyz` pour l’intégration dans des probes Kubernetes.
- Intégration de Gunicorn (présent dans `requirements.txt`) pour un usage en production.
- Ajout de tests unitaires sur le script `health.py` à titre de démonstration.

### Lancement de l'application avec Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8888 src:application
```
### Suggestions complémentaires

- Migration vers FastAPI pour une meilleure gestion de l'asynchrone
- Ajout de documentation technique (exemple de docstring dans `health.py`).

## Deploiement

- Creation d'un _Dockerfile_ optimisé.
- Mise à jour de Python de la version 3.11 à 3.12 pour corriger une vulnérabilité critique.
- Ajout d’un workflow de build automatique dans GitHub Actions pour la publication d’image sur GHCR.

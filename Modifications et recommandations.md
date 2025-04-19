# Modifications et recommandations

![CI](https://github.com/cecilegltslmcs/testing-repository-simple-python/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-via--pytest-blue)
[![codecov](https://codecov.io/gh/cecilegltslmcs/testing-repository-simple-python/branch/main/graph/badge.svg)](https://codecov.io/gh/cecilegltslmcs/testing-repository-simple-python)

## Généralités

- Mise en place d'une intégration continue via GitHub Actions.
- Mise à jour de la configuration `pre-commit` :
    - Remplacement de *flake8* et *black* par **Ruff**.
    - Ajout de hooks basiques : `check-yaml`, `check-docstring`, `end-of-file-fixer`, etc.

## Application

- Mise en place de `python-dotenv` dans `requirements-dev.txt` pour la gestion des variables d'environnement via un fichier `.env`.
- Mise en place des routes `/healthz` et `/readyz` pour l’intégration dans des probes Kubernetes.
- Mise en place de Gunicorn (présent dans `requirements.txt`) pour un usage en production.
- Mise en place de tests unitaires sur le script `health.py` à titre de démonstration.

### Lancement de l'application avec Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8888 src:application
```
> (cf. fichier Dockerfile pour plus de détails)

### Suggestions complémentaires

- Migration vers __FastAPI__ pour une meilleure gestion de l'asynchrone
- Ajout de documentation technique (exemple de docstring dans `health.py`).
- Migration vers __uv__ pour une gestion plus rapide et fiable des environnements, et la génération d’un requirements.lock utilisable dans CI.
- Remplacer le fichier _data.json_ par une base de données in-memory comme _Redis_, afin d'assurer la persistance des données partagées entre plusieurs instances et améliorer la gestion des accès concurrents.

## Déploiement

- Mise en place d'un _Dockerfile_ optimisé.
- Mise à jour de Python de la version 3.11 à 3.12 pour corriger une vulnérabilité critique.
- Mise en place d’un workflow de build automatique dans GitHub Actions pour la publication d’image sur GHCR.
- Mise en place d'un scan de sécurité de l'image buildé avec __Trivy__.

### Déploiement Kubernetes local (K3d)

- Mise en place des manifests Kubernetes associés à l'application dans `kube_config` :
    - _config-map.yaml_ : Contient les variables d'environnement pour la base de données. Pourra être modifié en secrets si besoin de cacher des mots de passe ou d'autres informations sensibles
    - _deployment.yaml_ : Informations du déploiement en lien avec l'application
    - _hpa.yaml_ : Gestion de la montée en charge en se basant sur les ressources liées au CPU
    - _ingress.yaml_ : Permet d'accéder à l'API à travers un reverse proxy propre à Kubernetes
    - _service.yaml_ : Permet d'exposer le déploiement.

Tous les fichiers mentionnés sont disponibles dans [`kube_config/`](kube_config/).
- Mise en place d’un workflow de déploiement local dans K3d, avec vérification automatique de l’endpoint `/readyz` via un _port-forward_ dans le pipeline CI.
- Mise en place d'un scan de sécurité du cluster après déploiement avec __Kubescape__.

### Suggestions complémentaires

- Passer le déploiement Kubernetes en charts Helm pour améliorer la portabilité, le templating et la gestion des environnements.
- Utiliser Kustomize pour gérer facilement plusieurs overlays (développement, staging, production) à partir des mêmes bases YAML.

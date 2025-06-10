# 📡 PiHunter – Analyse et Surveillance Réseau

Projet cybersécurité développé sur un Raspberry Pi 5 sous Kali Linux, destiné à scanner, surveiller et consigner les appareils connectés à un réseau local.

---

## 🧠 Introduction

PiHunter est un projet pédagogique et pratique de cybersécurité conçu pour :
- Comprendre le fonctionnement d’un réseau local
- S’entraîner à l’analyse passive et active
- Automatiser la collecte d’informations réseau
- Apprendre Docker, Git, Python et Linux en situation réelle

---

## 🛠️ Objectifs du projet

- Scanner le réseau local automatiquement
- Identifier les hôtes connectés (IP, MAC, nom, ports)
- Enregistrer les résultats dans des fichiers de logs
- Créer une interface simple en ligne de commande ou web
- Conteneuriser le tout avec Docker
- Automatiser les scans (via cron ou service systemd)

---

## 📦 Matériel utilisé

- Raspberry Pi 5 (8 Go recommandé)
- Carte microSD (au moins 32 Go, classe 10 ou UHS-1)
- Alimentation 5V/5A
- Connexion Internet (Wi-Fi ou Ethernet)
- Éventuellement : clavier, écran HDMI, boîtier (optionnel)

---

## 💻 Prérequis logiciels

- Kali Linux à jour (ou Raspberry Pi OS avec les bons outils)
- Python 3.11+
- Git
- Docker + Docker Compose
- VS Code (optionnel mais recommandé)

---

## 📁 Structure du projet

```
PiHunter/
├── src/                     # Scripts Python principaux
│   └── main.py              # Script de scan principal
├── logs/                    # Résultats des scans avec horodatage
├── docker/                  # Fichiers Docker liés
│   └── Dockerfile           # Image Python + dépendances
├── requirements.txt         # Dépendances Python
├── .dockerignore            # Fichiers à ignorer pour Docker
├── README.md                # Documentation projet
└── LICENSE                  # (Optionnel) Licence du projet
```

---

## 🧱 Étapes de développement

1. Créer le dépôt Git et l’environnement de travail
2. Développer le script Python principal (scan avec nmap)
3. Tester localement avec un fichier de log généré
4. Dockeriser le projet
5. Automatiser le lancement (crontab ou systemd)
6. Ajouter interface web ou CLI si besoin
7. Ajouter logs horodatés, export CSV, alertes mail
8. Documenter proprement tout dans ce README

---

## 🚀 Lancer le projet

- Lancer le script principal manuellement pour tester
- Utiliser Docker pour exécuter le conteneur
- Configurer l’automatisation du lancement

---

## 📑 À venir

- Interface web Flask
- Système de détection d’intrusion léger
- Dashboard local
- Surveillance continue

---

## 🤝 Contribuer

Projet librement modifiable. Idéal pour apprendre :
- le pentest éthique
- l’analyse réseau
- l’automatisation Linux
- la création de mini-applis Dockerisées

---

## 🧠 Auteur

Projet conçu par sanskalape, étudiant en cybersécurité.


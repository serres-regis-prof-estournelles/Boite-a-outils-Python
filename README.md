## 🧰 Boîte à outils Python

> **10 scripts Python pratiques réunis dans un seul programme avec menu interactif.**  
> Automatisez votre quotidien sans effort — les dépendances s'installent automatiquement.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Licence](https://img.shields.io/badge/Licence-Libre-green?style=flat)
![Niveau](https://img.shields.io/badge/Niveau-Débutant%20à%20Intermédiaire-orange?style=flat)

---

## 🚀 Lancement rapide

```bash
# Cloner le dépôt
git clone https://github.com/serres-regis-prof-estournelles/Boite-a-outils-Python.git

# Se placer dans le dossier
cd Boite-a-outils-Python

# Lancer le programme
python Utilitaires_en-Python.py
```

> ✅ Les bibliothèques manquantes sont **détectées et installées automatiquement** au démarrage.

---

## 📋 Les 10 outils disponibles

| # | Outil | Description |
|---|-------|-------------|
| 1 | 🧹 **Nettoyage des fichiers temporaires** | Supprime les fichiers inutiles qui encombrent votre système |
| 2 | 🏷️ **Renommage en masse** | Renomme plusieurs fichiers d'un dossier en une seule opération |
| 3 | 📊 **Surveillance CPU / RAM** | Affiche en temps réel l'utilisation du processeur et de la mémoire |
| 4 | 📥 **Téléchargement YouTube** | Télécharge des vidéos ou de l'audio depuis YouTube |
| 5 | ⏱️ **Minuteur Pomodoro** | Gère des sessions de travail focalisé avec pauses intégrées |
| 6 | 📄 **Convertisseur CSV / Excel** | Convertit des fichiers CSV en Excel (et inversement) |
| 7 | 📝 **Bloc-notes graphique** | Un éditeur de texte simple avec interface graphique (Tkinter) |
| 8 | 🔔 **Rappel de pause** | Envoie des notifications régulières pour vous inciter à faire une pause |
| 9 | 🌐 **Scan réseau** | Analyse les appareils connectés sur votre réseau local |
| 10 | 🪢 **Jeu du pendu** | Le classique jeu du pendu pour se détendre entre deux tâches |

---

## 🖥️ Interface

Le programme démarre sur un **menu interactif en ligne de commande** :

```
========================================
       🧰 BOÎTE À OUTILS PYTHON
========================================
  1. Nettoyage des fichiers temporaires
  2. Renommage en masse
  3. Surveillance CPU / RAM
  4. Téléchargement YouTube
  5. Minuteur Pomodoro
  6. Convertisseur CSV / Excel
  7. Bloc-notes graphique
  8. Rappel de pause
  9. Scan réseau
 10. Jeu du pendu
  0. Quitter
========================================
Votre choix :
```

---

## 📦 Dépendances

Les bibliothèques nécessaires sont installées automatiquement. En voici la liste :

| Bibliothèque | Utilisation |
|---|---|
| `psutil` | Surveillance CPU/RAM et scan réseau |
| `yt-dlp` | Téléchargement YouTube |
| `openpyxl` | Conversion CSV ↔ Excel |
| `tkinter` | Bloc-notes graphique (inclus dans Python standard) |
| `plyer` | Notifications de pause |

---

## ⚙️ Prérequis

- **Python 3.x** installé sur votre machine
- Connexion Internet (pour l'installation automatique des dépendances et le téléchargement YouTube)
- Windows, macOS ou Linux

---

## 🎓 Contexte pédagogique

Ce projet a été conçu pour illustrer concrètement la puissance de Python dans des cas d'usage réels du quotidien.

Il montre aux étudiants qu'avec quelques bibliothèques et un menu bien structuré, on peut créer un véritable outil polyvalent et utile.

**Compétences illustrées :**
- Utilisation de bibliothèques tierces (`pip`, imports)
- Programmation modulaire (une fonction par outil)
- Interface utilisateur en ligne de commande (menu `while` + `input`)
- Interface graphique avec `tkinter`
- Interactions système (fichiers, réseau, notifications)

---

## 👨‍🏫 Licence

Projet libre — réutilisable et adaptable librement.

---

👤 Auteur : SERRES Régis - Lycée E de Constant, La Flèche (72) - https://serres-regis-prof-estournelles.github.io/

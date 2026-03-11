#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PC Utilities – Collection de scripts pratiques pour votre ordinateur.
Sélectionnez un outil dans le menu pour l'exécuter.
"""

import os
import sys
import time
import subprocess
import random
import shutil
import importlib.util

# ----------------------------------------------------------------------
# Vérification / installation des dépendances optionnelles
# ----------------------------------------------------------------------
def check_and_install(package_name, import_name=None):
    """Vérifie si un module est installé, propose de l'installer si besoin."""
    if import_name is None:
        import_name = package_name
    if importlib.util.find_spec(import_name) is None:
        print(f"Le module '{package_name}' n'est pas installé.")
        rep = input("Voulez-vous l'installer maintenant ? (o/n) : ").lower()
        if rep == 'o':
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print("Installation terminée. Redémarrez le script si nécessaire.")
        else:
            print("Fonction désactivée.")
        return False
    return True

# ----------------------------------------------------------------------
# 1. Nettoyage des fichiers temporaires
# ----------------------------------------------------------------------
def nettoyage_temp():
    print("\n--- Nettoyage des fichiers temporaires ---")
    temp_dirs = []
    if os.name == 'nt':  # Windows
        temp_dirs.append(os.environ.get('TEMP', ''))
        temp_dirs.append(os.environ.get('TMP', ''))
    else:  # Linux / Mac
        temp_dirs.append('/tmp')
        temp_dirs.append(os.path.expanduser('~/.cache'))
    
    total = 0
    for d in set(temp_dirs):
        if d and os.path.exists(d):
            for root, dirs, files in os.walk(d):
                for f in files:
                    try:
                        path = os.path.join(root, f)
                        os.remove(path)
                        total += 1
                    except Exception:
                        pass
    print(f"Nettoyage terminé. {total} fichiers supprimés.")

# ----------------------------------------------------------------------
# 2. Renommage en masse de fichiers
# ----------------------------------------------------------------------
def renommage_masse():
    print("\n--- Renommage en masse ---")
    dossier = input("Chemin du dossier contenant les fichiers : ").strip()
    if not os.path.isdir(dossier):
        print("Dossier introuvable.")
        return
    extensions = input("Extensions à prendre en compte (séparées par des virgules, ex: jpg,png) : ").strip().split(',')
    extensions = [ext.strip().lower() for ext in extensions if ext.strip()]
    if not extensions:
        extensions = ['jpg', 'png', 'jpeg', 'gif', 'bmp']  # défaut
    
    prefix = input("Préfixe pour les nouveaux noms (ex: photo) : ").strip() or "fichier"
    
    fichiers = [f for f in os.listdir(dossier)
                if os.path.isfile(os.path.join(dossier, f)) and
                f.split('.')[-1].lower() in extensions]
    fichiers.sort()
    
    for i, fichier in enumerate(fichiers):
        ext = fichier.split('.')[-1]
        nouveau = f"{prefix}_{i+1:03d}.{ext}"
        ancien_path = os.path.join(dossier, fichier)
        nouveau_path = os.path.join(dossier, nouveau)
        os.rename(ancien_path, nouveau_path)
        print(f"{fichier} -> {nouveau}")
    print(f"Renommé {len(fichiers)} fichiers.")

# ----------------------------------------------------------------------
# 3. Surveillance des ressources système (psutil)
# ----------------------------------------------------------------------
def surveillance_ressources():
    if not check_and_install('psutil'):
        return
    import psutil
    print("\n--- Ressources système ---")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print(f"CPU : {cpu}%")
    print(f"RAM : {ram}%")
    print(f"Disque : {disk}%")

# ----------------------------------------------------------------------
# 4. Téléchargement de vidéos YouTube (pytube)
# ----------------------------------------------------------------------
def youtube_download():
    if not check_and_install('pytube'):
        return
    from pytube import YouTube
    print("\n--- Téléchargement YouTube ---")
    url = input("URL de la vidéo : ").strip()
    try:
        yt = YouTube(url)
        print(f"Titre : {yt.title}")
        stream = yt.streams.get_highest_resolution()
        print("Téléchargement en cours...")
        stream.download()
        print("Terminé.")
    except Exception as e:
        print(f"Erreur : {e}")

# ----------------------------------------------------------------------
# 5. Minuteur Pomodoro
# ----------------------------------------------------------------------
def minuteur_pomodoro():
    print("\n--- Minuteur Pomodoro ---")
    def minuteur(duree):
        while duree:
            mins, secs = divmod(duree, 60)
            print(f"{mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            duree -= 1
        print("\nC'est l'heure !")
    
    try:
        cycles = int(input("Nombre de cycles (1 cycle = travail + pause) : ") or 1)
    except ValueError:
        cycles = 1
    
    for i in range(cycles):
        print(f"\nCycle {i+1}/{cycles} – Travail (25 min)")
        minuteur(25*60)
        if i < cycles-1:
            print("Pause courte (5 min)")
            minuteur(5*60)
    print("Pause longue (15 min)")
    minuteur(15*60)

# ----------------------------------------------------------------------
# 6. Convertisseur CSV ↔ Excel (pandas)
# ----------------------------------------------------------------------
def convert_csv_excel():
    if not check_and_install('pandas'):
        return
    import pandas as pd
    print("\n--- Convertisseur CSV / Excel ---")
    print("1. CSV → Excel")
    print("2. Excel → CSV")
    choix = input("Votre choix : ").strip()
    if choix == '1':
        csv_file = input("Fichier CSV à convertir : ").strip()
        if not os.path.isfile(csv_file):
            print("Fichier introuvable.")
            return
        try:
            df = pd.read_csv(csv_file)
            excel_file = csv_file.rsplit('.', 1)[0] + '.xlsx'
            df.to_excel(excel_file, index=False)
            print(f"Fichier Excel créé : {excel_file}")
        except Exception as e:
            print(f"Erreur : {e}")
    elif choix == '2':
        excel_file = input("Fichier Excel à convertir : ").strip()
        if not os.path.isfile(excel_file):
            print("Fichier introuvable.")
            return
        try:
            df = pd.read_excel(excel_file)
            csv_file = excel_file.rsplit('.', 1)[0] + '.csv'
            df.to_csv(csv_file, index=False)
            print(f"Fichier CSV créé : {csv_file}")
        except Exception as e:
            print(f"Erreur : {e}")
    else:
        print("Choix invalide.")

# ----------------------------------------------------------------------
# 7. Bloc-notes avec Tkinter
# ----------------------------------------------------------------------
def bloc_notes():
    print("\n--- Lancement du bloc-notes ---")
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox
    except ImportError:
        print("Tkinter n'est pas disponible sur votre système.")
        return
    
    def ouvrir():
        chemin = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt"), ("Tous", "*.*")])
        if chemin:
            try:
                with open(chemin, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                texte.delete(1.0, tk.END)
                texte.insert(tk.END, contenu)
                root.title(f"Bloc-notes - {os.path.basename(chemin)}")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
    
    def sauvegarder():
        chemin = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Fichiers texte", "*.txt"), ("Tous", "*.*")])
        if chemin:
            try:
                with open(chemin, 'w', encoding='utf-8') as f:
                    f.write(texte.get(1.0, tk.END))
                root.title(f"Bloc-notes - {os.path.basename(chemin)}")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
    
    root = tk.Tk()
    root.title("Bloc-notes")
    texte = tk.Text(root, wrap='word')
    texte.pack(expand=True, fill='both')
    
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    fichier_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Fichier", menu=fichier_menu)
    fichier_menu.add_command(label="Ouvrir", command=ouvrir)
    fichier_menu.add_command(label="Sauvegarder", command=sauvegarder)
    fichier_menu.add_separator()
    fichier_menu.add_command(label="Quitter", command=root.quit)
    
    root.mainloop()

# ----------------------------------------------------------------------
# 8. Rappel de pause (eye rest)
# ----------------------------------------------------------------------
def rappel_pause():
    print("\n--- Rappel de pause ---")
    print("Toutes les 20 minutes, une notification apparaîtra.")
    print("Appuyez sur Ctrl+C dans le terminal pour arrêter.")
    try:
        while True:
            time.sleep(20*60)  # 20 minutes
            if os.name == 'nt':
                import ctypes
                ctypes.windll.user32.MessageBoxW(0, "Levez les yeux de l'écran !", "Pause", 1)
            else:
                # Tentative d'utilisation de notify-send (Linux) ou osascript (Mac)
                if shutil.which('notify-send'):
                    subprocess.run(['notify-send', 'Pause', 'Levez les yeux de l’écran !'])
                elif shutil.which('osascript'):
                    subprocess.run(['osascript', '-e', 'display notification "Levez les yeux !" with title "Pause"'])
                else:
                    print("\n[Pause] Levez les yeux de l'écran !")
    except KeyboardInterrupt:
        print("\nRappel arrêté.")

# ----------------------------------------------------------------------
# 9. Scanner de réseau local (ping)
# ----------------------------------------------------------------------
def scanner_reseau():
    print("\n--- Scanner de réseau local ---")
    base = input("Plage réseau (ex: 192.168.1.) : ").strip()
    if not base.endswith('.'):
        base += '.'
    
    actifs = []
    total = 254
    print("Scan en cours...")
    for i in range(1, 255):
        adresse = base + str(i)
        print(f"\rTest de {adresse}...", end='')
        if os.name == 'nt':
            param = ['ping', '-n', '1', '-w', '500', adresse]
        else:
            param = ['ping', '-c', '1', '-W', '1', adresse]
        try:
            result = subprocess.run(param, capture_output=True, timeout=2)
            if result.returncode == 0:
                actifs.append(adresse)
        except subprocess.TimeoutExpired:
            pass
    print("\n\nAdresses actives :")
    for a in actifs:
        print(a)

# ----------------------------------------------------------------------
# 10. Mini-jeu : Pendu
# ----------------------------------------------------------------------
def jeu_pendu():
    print("\n--- Jeu du Pendu ---")
    mots = ["python", "programme", "ordinateur", "utilitaire", "developpement",
            "algorithme", "boucle", "variable", "fonction", "bibliotheque"]
    mot = random.choice(mots)
    lettres_trouvees = []
    essais = 6
    trouve = False
    
    while essais > 0 and not trouve:
        affichage = ''.join([l if l in lettres_trouvees else '_' for l in mot])
        print(f"\nMot : {affichage}")
        print(f"Essais restants : {essais}")
        lettre = input("Lettre : ").lower()
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue
        if lettre in lettres_trouvees:
            print("Lettre déjà proposée.")
            continue
        lettres_trouvees.append(lettre)
        if lettre in mot:
            print("Bonne lettre !")
            if all(l in lettres_trouvees for l in mot):
                trouve = True
        else:
            print("Mauvaise lettre.")
            essais -= 1
    if trouve:
        print(f"\nGagné ! Le mot était '{mot}'.")
    else:
        print(f"\nPerdu ! Le mot était '{mot}'.")

# ----------------------------------------------------------------------
# Menu principal
# ----------------------------------------------------------------------
def menu():
    while True:
        print("\n" + "="*50)
        print("         PC UTILITIES - MENU PRINCIPAL")
        print("="*50)
        print(" 1. Nettoyage des fichiers temporaires")
        print(" 2. Renommage en masse de fichiers")
        print(" 3. Surveillance des ressources système (psutil)")
        print(" 4. Téléchargement de vidéos YouTube (pytube)")
        print(" 5. Minuteur Pomodoro")
        print(" 6. Convertisseur CSV ↔ Excel (pandas)")
        print(" 7. Bloc-notes avec interface graphique")
        print(" 8. Rappel de pause (eye rest)")
        print(" 9. Scanner de réseau local")
        print("10. Mini-jeu : Pendu")
        print(" 0. Quitter")
        print("-"*50)
        choix = input("Votre choix : ").strip()
        print()
        
        if choix == '1':
            nettoyage_temp()
        elif choix == '2':
            renommage_masse()
        elif choix == '3':
            surveillance_ressources()
        elif choix == '4':
            youtube_download()
        elif choix == '5':
            minuteur_pomodoro()
        elif choix == '6':
            convert_csv_excel()
        elif choix == '7':
            bloc_notes()
        elif choix == '8':
            rappel_pause()
        elif choix == '9':
            scanner_reseau()
        elif choix == '10':
            jeu_pendu()
        elif choix == '0':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nInterruption utilisateur. Au revoir !")
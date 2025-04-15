# 📊 Declarateur d'impôt 3000

> Application locale pour calculer vos plus-values crypto en méthode FIFO + 2086 3N et estimer l'impôt associé via le barème de l'impôt progressif.

---

## 🚀 Lancer l'application en local (Windows)

### 🧰 1. Pré-requis
Assurez-vous d'avoir **Python 3.10 ou plus récent** installé.

#### 👉 Pour installer Python :
1. Faites **Win + X** puis sélectionnez **Terminal (administrateur)**.
2. Tapez la commande suivante pour télécharger l'installeur officiel :
   ```powershell
   Start-Process "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
   ```
3. Pendant l'installation, cochez ✅ **"Add Python to PATH"** avant de cliquer sur "Install Now".

---

### 📦 2. Installer les dépendances nécessaires

#### 📁 Étape A : Accédez au dossier contenant le fichier
1. Téléchargez le fichier `declarateur-d-impot-3000.py` sur votre ordinateur.
2. Cliquez avec le **bouton droit** sur le dossier contenant ce fichier et sélectionnez **"Copier comme chemin d’accès"**.
3. Ouvrez le Terminal (Win + X > Terminal (administrateur)).
4. Tapez `cd ` (avec un espace) puis **collez le chemin** copié :
   ```bash
   cd "C:\Users\votre_nom\Exemple\De\Chemin"
   ```

#### 🧱 Étape B : Installer les modules Python requis

Dans ce même terminal, tapez :

```bash
pip install streamlit pandas
```

---

### ▶️ 3. Lancer l'application

Toujours dans le même terminal, lancez l'application avec :

```bash
streamlit run declarateur-d-impot-3000.py
```

Cela ouvrira automatiquement l’application dans votre navigateur (par défaut à l’adresse `http://localhost:8501`).

---

## 🔐 Fonctionnement

L’application fonctionne **hors ligne**. Aucune donnée personnelle ou fichier CSV n’est envoyé sur Internet.  
Tout reste **sur votre ordinateur**.

---

## ✨ Fonctionnalités

- Upload CSV (Bitpanda ou autre)
- Calcul FIFO des plus-values et formulaire 2086 - 3N
- Simulation fiscale avec barème progressif modifiable depuis l'interface
- Export CSV au format français
- Code source consultable via un onglet dédié dans l’interface

---

## 📜 Licence

Projet open source – librement modifiable, redistribuable et utilisable.

---

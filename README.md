# 📊 Declarateur d'impôt 3000

> Application locale pour calculer vos plus-values crypto en méthode FIFO et estimer l'impôt associé via un barème progressif.

---

## 🚀 Lancer l'application en local (Windows)

### 🧰 1. Pré-requis
Assurez-vous d'avoir **Python 3.10 ou plus récent** installé.

#### 👉 Pour installer Python :
1. Faites **Win + X** puis choisissez **Windows PowerShell (admin)**.
2. Tapez la commande suivante pour télécharger l'installeur officiel :
   ```powershell
   Start-Process "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
   ```
3. Pendant l'installation, cochez ✅ **"Add Python to PATH"**.

---

### 📦 2. Installer les dépendances
Dans PowerShell ou Terminal, allez dans le dossier contenant ce projet, puis exécutez :

```bash
pip install streamlit pandas
```

---

### ▶️ 3. Lancer l'application
Toujours dans le dossier du script, exécutez :

```bash
streamlit run declarateur-d-impot-3000.py
```

Cela ouvrira l'application dans votre navigateur.

---

## 🔐 Fonctionnement

L’application fonctionne **hors ligne**. Aucune donnée personnelle ou fichier CSV n’est envoyé sur Internet.  
Tout reste **sur votre ordinateur**.

---

## ✨ Fonctionnalités

- Upload CSV (Bitpanda ou autre)
- Calcul FIFO des plus-values
- Simulation fiscale avec barème progressif personnalisable
- Export CSV au format français
- Code source consultable via un onglet dédié dans l’interface

---

## 📜 Licence

Projet open source – librement modifiable, redistribuable et utilisable.

---


Dépôt officiel domOpen lab

# 📚 Applications disponibles

---

<details closed>

<summary>📊 DI-3000 — Déclarer vos plus-values crypto selon le barème de l'impôt (Formulaire 2086 - 3N)</summary>

---

**DI-3000** est une interface locale pour :

- 📥 Charger un fichier CSV (testé avec : bitpanda)
- 🔁 Appliquer la méthode **FIFO** pour les ventes de crypto
- 🧾 Générer automatiquement les lignes fiscales du **formulaire 2086 (3N)**
- 📊 Simuler votre impôt via un **barème progressif modifiable**
- 📤 Exporter les résultats au format **CSV français**
- 👨‍💻 Accéder au **code source** depuis l’interface

---

<details closed>
<summary>Installation sous Windows 10-11</summary>

#### 🧰 1. Installation de Python 3.10+

- Appuyez sur **Win + X** et choisissez **Terminal (administrateur)**.
- Tapez cette commande pour télécharger et installer Python :
   ```powershell
   Start-Process "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
   ```

Pendant l'installation, cochez ✅ **"Add Python to PATH"**

---

#### 📁 2. Accéder au dossier de l'application

- Cliquez avec le **bouton droit** sur le dossier contenant `declarateur-d-impot-3000.py`  
- Choisissez **"Copier comme chemin d’accès"**
- Ouvrez une nouvelle fenêtre **Terminal (administrateur)** avec le raccourci **Win + X**, tapez **cd suivi d'un espace** et collez votre chemin :

```bash
cd "C:\Users\votre_nom\Chemin\vers\le\dossier"
```

---

#### 📦 3. Installer les dépendances

- Dans la même fenêtre copier puis coller la commande suivante : 

```bash
pip install streamlit pandas
```

---

#### ▶️ 4. Lancer l’application

- Et toujours dans la même fenêtre copier puis coller la commande suivante :

```bash
streamlit run declarateur-d-impot-3000.py
```

Cela ouvre automatiquement une page dans votre navigateur à l’adresse `http://localhost:8501`.

---

</details>

---

## 📜 Licence

Projets open source — librement modifiable, redistribuable et utilisable.

---

</details>

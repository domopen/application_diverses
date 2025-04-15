Dépôt officiel domOpen lab

# 📚 Applications disponibles

---

<details closed>

<summary>📊 DI-3000 — Calculateur de plus-values crypto</summary>

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

#### 🧰 1. Prérequis

1. Appuyez sur **Win + X** et choisissez **Terminal (administrateur)**.
2. Tapez cette commande pour télécharger et installer Python :
   ```powershell
   Start-Process "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
   ```

Pendant l'installation, cochez ✅ **"Add Python to PATH"**

---

#### 📁 2. Accéder au dossier de l'application

- Cliquez avec le **bouton droit** sur le dossier contenant `declarateur-d-impot-3000.py`  
- Choisissez **"Copier comme chemin d’accès"**
- Ouvrez le **Terminal (administrateur)**, puis tapez :

```bash
cd "C:\Users\votre_nom\Chemin\vers\le\dossier"
```

---

#### 📦 3. Installer les dépendances

```bash
pip install streamlit pandas
```

---

#### ▶️ 4. Lancer l’application

```bash
streamlit run declarateur-d-impot-3000.py
```

Cela ouvre automatiquement une page dans votre navigateur à l’adresse `http://localhost:8501`.

---

## 📜 Licence

Projets open source — librement modifiable, redistribuable et utilisable.

</details>
</details>

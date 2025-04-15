# 📚 Applications disponibles

Ce dépôt contient plusieurs outils fiscaux open source, tous exécutables **en local**.

---

<details closed>
<summary>📊 DI-3000 — Calculateur de plus-values crypto</summary>

**DI-3000** est une interface locale pour :

- 📥 Charger un fichier CSV (Bitpanda, Binance, etc.)
- 🔁 Appliquer la méthode **FIFO** pour les ventes de crypto
- 🧾 Générer automatiquement les lignes fiscales du **formulaire 2086 (3N)**
- 📊 Simuler votre impôt via un **barème progressif modifiable**
- 📤 Exporter les résultats au format **CSV français**
- 👨‍💻 Accéder au **code source** depuis l’interface

### 🚀 Lancer l’application DI-3000 sous Windows

#### 🧰 1. Prérequis

- Avoir **Python 3.10+** installé.

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

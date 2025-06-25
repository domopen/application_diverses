import pandas as pd
import streamlit as st
from datetime import datetime
from io import StringIO

tab1, tab2 = st.tabs(["DI-3000", "Pour les curieux"])

with tab1:
    st.title("DI-3000")

    uploaded_file = st.file_uploader("Étape 1 — Dépose ton fichier CSV", type=["csv"])

    if uploaded_file:
        # Lecture du contenu et détection de l'en-tête
        raw_lines = uploaded_file.getvalue().decode("utf-8").splitlines()
        skip = 0
        for i, line in enumerate(raw_lines):
            if line.startswith("\"Transaction ID"):
                skip = i
                break

        # Lecture du CSV
        df = pd.read_csv(StringIO('\n'.join(raw_lines[skip:])))

        # Nettoyage et conversions de colonnes
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce', utc=True)
        df['Amount Asset'] = pd.to_numeric(df['Amount Asset'], errors='coerce')
        df['Amount Fiat'] = pd.to_numeric(df['Amount Fiat'], errors='coerce')
        df['Fee'] = pd.to_numeric(df['Fee'], errors='coerce')

        # Filtrage des crypto uniquement
        crypto_df = df[df['Asset class'] == 'Cryptocurrency']

        # Sélection des paramètres d’analyse
        asset = st.selectbox("Choisis l'actif à analyser (ex: BTC)", sorted(crypto_df['Asset'].unique()))
        year = st.number_input("Année fiscale à analyser (ex: 2024)", min_value=2014, max_value=datetime.now().year, value=2024)

        df_asset = crypto_df[crypto_df['Asset'] == asset].sort_values(by='Timestamp')
        df_asset = df_asset[df_asset['Timestamp'] <= pd.Timestamp(f"{year}-12-31T23:59:59Z")]

        # Préparation des achats et ventes
        purchases, sales = [], []
        for _, row in df_asset.iterrows():
            if row['Transaction Type'] in ['buy', 'deposit'] and row['Amount Asset'] > 0:
                purchases.append({
                    'date': row['Timestamp'],
                    'amount': row['Amount Asset'],
                    'cost_total': row['Amount Fiat'],
                    'remaining': row['Amount Asset']
                })
            elif row['Transaction Type'] == 'sell' and row['Amount Asset'] > 0:
                sales.append({
                    'date': row['Timestamp'],
                    'amount': row['Amount Asset'],
                    'value_total': row['Amount Fiat']
                })

        # Totaux globaux
        total_bought_btc = sum(p['amount'] for p in purchases)
        total_bought_eur = sum(p['cost_total'] for p in purchases)
        total_sold_btc = sum(s['amount'] for s in sales)
        total_sold_eur = sum(s['value_total'] for s in sales)

        st.subheader("🔢 ToTaux globaux")
        st.markdown(f"- **BTC achetés** : {total_bought_btc:.8f}")
        st.markdown(f"- **BTC vendus** : {total_sold_btc:.8f}")
        st.markdown(f"- **Montant total investi (€)** : {total_bought_eur:.2f} €")
        st.markdown(f"- **Montant total récupéré (€)** : {total_sold_eur:.2f} €")

        # Application
        results = []
        for sale in sales:
            remaining = sale['amount']
            cost_total = 0
            for purchase in purchases:
                if purchase['remaining'] <= 0:
                    continue
                used = min(purchase['remaining'], remaining)
                cost_unit = purchase['cost_total'] / purchase['amount']
                cost_total += cost_unit * used
                purchase['remaining'] -= used
                remaining -= used
                if remaining <= 0:
                    break
            results.append({
                'Date de la cession': sale['date'].date(),
                'Quantité': sale['amount'],
                'Prix de cession': round(sale['value_total'], 2),
                'Prix d\'acquisition': round(cost_total, 2),
                'Gain net': round(sale['value_total'] - cost_total, 2)
            })

        df_results = pd.DataFrame(results)

        if not df_results.empty:
            df_filtered = df_results[df_results['Date de la cession'].apply(lambda d: d.year) == year]
        else:
            df_filtered = pd.DataFrame(columns=["Date de la cession", "Quantité", "Prix de cession", "Prix d'acquisition", "Gain net"])

        st.subheader("Récapitulatif des ventes pour l'année fiscale")
        st.dataframe(df_filtered)

        # Calculs fiscaux complémentaires
        prix_de_cession_total = df_filtered['Prix de cession'].astype(float).sum()
        prix_total_acquisition = (total_bought_eur - total_sold_eur)
        gain_brut_total = df_filtered['Gain net'].astype(float).sum()
        quantite_totale_vendue = df_filtered['Quantité'].astype(float).sum()
        prix_moyen_vente = prix_de_cession_total / quantite_totale_vendue if quantite_totale_vendue > 0 else 0
        valeur_portefeuille_restante = (total_bought_btc - total_sold_btc) * prix_moyen_vente
        proportion_du_portefeuille_vendue = (prix_de_cession_total / valeur_portefeuille_restante)
        partie_du_portefeuille_aquisition_affectee_cession = (total_bought_eur - total_sold_eur) * proportion_du_portefeuille_vendue
        plus_value_imposable = (prix_de_cession_total - partie_du_portefeuille_aquisition_affectee_cession)

        st.subheader("📄 Récapitulatif fiscal")

        st.markdown(f"- **Ligne 212 - Valeur estimée du portefeuille restant** : {valeur_portefeuille_restante:.2f} €")
        st.markdown(f"- **Ligne 213 - Total vendu au cours de l'année** : {prix_de_cession_total:.2f} €")
        st.markdown(f"- **Ligne 220 - Prix total d'acquisition** : {prix_total_acquisition:.2f} €")
        st.markdown(f"- **Ligne 224 - Plus-value imposable** : {plus_value_imposable:.2f} €")

        st.markdown(f"- **Prix moyen du BTC lors des ventes** : {prix_moyen_vente:.2f} €")
        st.markdown(f"- **Gain brut** : {gain_brut_total:.2f} €")
    
        st.subheader("📊 Barème progressif personnalisable (ex : barème 2025)")
        # Saisie des autres revenus (ex. salaire)
        autres_revenus = st.number_input("Autres revenus imposables (ex : salaires)", min_value=0, value=21000)
        deductions_niches = st.number_input("Déductions et niches fiscales (ex : frais kilométriques)", min_value=0, value=8000)

        # Barème standard personnalisable
        default_bareme = [
            {"Plafond": 11497, "Taux": 0},
            {"Plafond": 29315, "Taux": 11},
            {"Plafond": 83823, "Taux": 30},
            {"Plafond": 180294, "Taux": 41},
            {"Plafond": float("inf"), "Taux": 45}
        ]

        bareme = st.data_editor(
            default_bareme,
            key="bareme_editor",
            num_rows="dynamic",
            use_container_width=True
        )

        def calcul_impot_progressif(gain, autres_revenus, deductions_niches, bareme):
            impots = 0.0
            revenu_total = gain + autres_revenus - deductions_niches
            precedent_Plafond = 0.0
            reste = revenu_total
            Taux_marginal = 0.0

            for tranche in bareme:
                Plafond = float(tranche['Plafond'])
                Taux = float(tranche['Taux']) / 100
                if revenu_total > precedent_Plafond:
                    taxable = min(Plafond - precedent_Plafond, reste)
                    impots += taxable * Taux
                    reste -= taxable
                    precedent_Plafond = Plafond
                    Taux_marginal = Taux
                if reste <= 0:
                    break

            proportion_crypto = gain / revenu_total if revenu_total > 0 else 0
            impot_crypto = impots * proportion_crypto

            return impot_crypto, impots, Taux_marginal * 100

        impot_crypto, montant_impot_progressif, Taux_marginal = calcul_impot_progressif(plus_value_imposable, autres_revenus, deductions_niches, bareme)

        st.markdown(f"- **Taux marginal d’imposition atteint** : {Taux_marginal:.1f} %")
        st.markdown(f"- **Impôt total estimé (tous revenus)** : {montant_impot_progressif:.2f} €")

        # Export CSV avec format français
        df_export = df_filtered.copy()
        for col in ['Quantité', 'Prix de cession', "Prix d'acquisition", 'Gain net']:
            df_export[col] = df_export[col].map(lambda x: f"{x:.2f}".replace('.', ','))

        csv_export = df_export.to_csv(index=False, sep=';', encoding='utf-8').encode('utf-8')
        st.download_button("📤 Télécharger le récap en CSV", csv_export, file_name=f"plusvalues_fifo_{asset}_{year}.csv")

        with st.expander("ℹ️ Comment fonctionne ce calcul FIFO ?"):
            st.markdown("""
            - 📅 **Achats** : chaque achat est enregistré avec sa date, son montant, et son prix total.
            - 📤 **Ventes** : à chaque vente, la quantité vendue est associée aux **achats les plus anciens** (FIFO).
            - 🧾 Le **coût d'acquisition total** de chaque vente est ainsi déterminé.
            - 📈 La **plus-value** correspond à : `Prix de vente - Prix d'achat FIFO`
            - 💶 Seules les cessions (ventes) sont imposables, pas les achats ni les conversions crypto/crypto.
            """)
with tab2:
    st.title("Code source")

    st.markdown("""
    ### 🔍 Le projet : `Le Déclarateur d'Impôt 3000`

    Bienvenue dans les entrailles du DI-3000.  
    Ce projet est open source et conçu pour fonctionner en local, sans transfert de données.
                
    N'hésites pas à proposer des pistes d'améliorations!

    - **Technos utilisées** : Python, Pandas, Streamlit.
    - **Méthode de calcul** : FIFO (First In, First Out) + Formulaire 2086.
    - **Fonctions principales** :
        - Lecture et filtrage des transactions crypto en .csv.
        - Appariement automatique des ventes aux achats les plus anciens (FIFO proof).
        - Simulation d’imposition selon le barème français.
    
    📂 Le dépôt est disponible ici :
    👉 [https://github.com/domopen/application_diverses](https://github.com/domopen/application_diverses)

    Tu peux utiliser, modifier et redistribuer ce code à ta guise, dans le respect de la licence associée.
    """)

# 🏦 Bank Marketing Campaign: Precision Targeting Strategy

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange?style=for-the-badge&logo=scikit-learn)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-blue?style=for-the-badge&logo=tableau)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-red?style=for-the-badge&logo=streamlit)

## 📌 Project Overview
This project focuses on optimizing bank telemarketing campaigns. Using historical data, we built a Machine Learning model to predict which customers are most likely to subscribe to a term deposit.

Main Objective: Shift your marketing strategy from blind calling to data-driven targeting to improve efficiency and ROI.

---

## 📉 Business Problem Statement
* **Low Efficiency: Approximately 88% of contacted customers reject the offer, wasting time and resources.
* **Customer Fatigue: Repeatedly contacting uninterested customers damages the bank's reputation.
* **Wasteful Costs: High operational costs for a very low hit rate.

## 🎯 Goals
1. **Increase Conversion Rate** by identifying potential customer profiles.
2. **Cost Optimization** by reducing the number of calls to customers predicted to reject.
3. **Data-Driven Insights** provide tactical recommendations for the marketing team.

---

## 📊 Tableau Dashboard & Insights
Interactive visual analytics have been created to map customer behavior in depth.

> [!TIP]
> **[CLICK HERE TO VIEW THE INTERACTIVE DASHBOARD]([YOUR_TABLEAU_PUBLIC_URL](https://public.tableau.com/app/profile/lieftha.hasaz/viz/Bank-Marketing-CampaignFinProLiefthaFaris/Dashboard1))**
>## 📊 Streamlit App & Start Predict!!!
Interactive visual analytics have been created to map customer behavior in depth.

> [!TIP]
> **[CLICK HERE TO START PREDICT]([YOUR_TABLEAU_STREAMLIT_URL](https://bank-marketing-analysis-ml-5djseixlcmfn9qh84nkjxn.streamlit.app/))**


![Tableau Preview](assets/tableau_preview.png)
*(Replace this image with a screenshot of your dashboard in the assets folder)*

---

## 🤖 Modeling & Performance
We tested several algorithms with **Stratified 5-Fold CV + SMOTE** to handle imbalanced data.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **LightGBM** | 0.8928 | 0.5326 | 0.4009 | **0.4574** | **0.7940** |
| **XGBoost** | 0.8947 | 0.5493 ​​| ​​0.3667 | 0.4397 | 0.7840 |
| **LogReg** | 0.8144 | 0.3314 | 0.6361 | 0.4357 | 0.7903 |

**Selected Model: LightGBM**
This model was chosen because it had the best balance (F1-Score & ROC-AUC) for distinguishing potential customers while maintaining high precision.

---

## 💡 Strategic Recommendations

### 👔 For Business Leaders
* **Precision Targeting:** Implement the LightGBM model to filter your list of potential customers. This has the potential to increase campaign efficiency by up to **4x**.
* **Resource Allocation:** Allocate call center staff only to customers with a conversion probability of >50% to reduce operational costs.

### 📣 For Marketing Team
* **Profile Focus:** Prioritize customers with a stable previous contact duration and an economic profile that aligns with the model's key feature analysis results.
* **Smart Application:** Use the **Streamlit Web App** to make instant predictions before making calls to determine daily priorities.

---

## 📂 Repository Structure
```text
├── data/ # Raw & Processed Dataset
├── notebooks/ # Full Analysis (EDA, Preprocessing, Modeling)
├── models/ # Saved Model (.pkl)
├── app/ # Streamlit Application Code
├── reports/ # Tableau Documentation
└── README.md # Project Documentation

# 🏦 Bank Marketing Campaign: Precision Targeting Strategy

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange?style=for-the-badge&logo=scikit-learn)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-blue?style=for-the-badge&logo=tableau)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-red?style=for-the-badge&logo=streamlit)

## 📌 Project Overview
This project optimizes bank telemarketing campaigns by shifting from "blind calling" to data-driven targeting. By analyzing historical customer data, we developed a Machine Learning model that identifies individuals most likely to subscribe to a term deposit, significantly improving ROI and resource allocation.

---

## 🔗 Live Project Links
| Service | Link |
| :--- | :--- |
| **🚀 Live Prediction App** | [**Access Streamlit App**](https://bank-marketing-analysis-ml-5djseixlcmfn9qh84nkjxn.streamlit.app/) |
| **📊 Interactive Dashboard** | [**View Tableau Public**](https://public.tableau.com/app/profile/lieftha.hasaz/viz/Bank-Marketing-CampaignFinProLiefthaFaris/Dashboard1) |

---

## 📉 Business Problem Statement
*   **Low Efficiency:** Approximately 88% of contacted customers reject the offer, leading to wasted labor.
*   **Customer Fatigue:** Repeatedly contacting uninterested prospects damages the bank's reputation.
*   **High Operational Costs:** Low "hit rates" result in high costs per acquisition.

## 🎯 Project Goals
1.  **Increase Conversion Rate:** Focus on high-probability customer profiles.
2.  **Cost Optimization:** Reduce calls to customers predicted to reject the offer.
3.  **Actionable Insights:** Provide the marketing team with data-backed tactical recommendations.

---

## 📊 Deployment & Analytics

### 1. Interactive Tableau Dashboard
Explore deep-dive analytics on customer demographics, economic indicators, and previous campaign success. Use this to understand *why* certain segments perform better.

> **[👉 View Full Dashboard Here](https://public.tableau.com/app/profile/lieftha.hasaz/viz/Bank-Marketing-CampaignFinProLiefthaFaris/Dashboard1)**

### 2. Streamlit ML Predictor
A ready-to-use tool for the sales team. Input customer details (job, age, balance, etc.) to get an instant prediction of their subscription likelihood.

> **[👉 Try the Prediction Tool](https://bank-marketing-analysis-ml-5djseixlcmfn9qh84nkjxn.streamlit.app/)**

---

## 🤖 Modeling & Performance
We addressed data imbalance using **Stratified 5-Fold Cross-Validation + SMOTE**. 

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **🏆 LightGBM** | **0.8928** | **0.5326** | **0.4009** | **0.4574** | **0.7940** |
| **XGBoost** | 0.8947 | 0.5493 | 0.3667 | 0.4397 | 0.7840 |
| **LogReg** | 0.8144 | 0.3314 | 0.6361 | 0.4357 | 0.7903 |

**Selected Model:** `LightGBM`  
*Why?* It offers the best balance between Precision and Recall (F1-Score), ensuring we don't miss potential customers while keeping "false alarm" calls low.

---

## 💡 Strategic Recommendations

### 👔 For Business Leaders
*   **Precision Targeting:** Implementing the LightGBM model can potentially increase campaign efficiency by up to **4x** by filtering out low-probability leads.
*   **Optimized Resource Allocation:** Direct call center efforts toward leads with a predicted conversion probability of >50%.

### 📣 For Marketing Team
*   **Key Profiles:** Prioritize customers based on call duration stability and specific economic profiles identified in the EDA.
*   **Daily Workflow:** Integrate the **Streamlit Web App** into the daily routine to prioritize call lists every morning.

---

## 📂 Repository Structure
```text
├── data/           # Raw & Processed Dataset
├── notebooks/      # Full Analysis (EDA, Preprocessing, Modeling)
├── models/         # Saved Model (.pkl)
├── app/            # Streamlit Application Code
├── assets/         # Images & Screenshots
└── README.md       # Project Documentation
```

---
**Author:** *Lieftha & Faris*  
**Contact:** [Your LinkedIn/Email Here] | [Partner LinkedIn/Email Here]

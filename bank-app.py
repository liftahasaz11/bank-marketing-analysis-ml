import streamlit as st
import pandas as pd
import joblib
import numpy as np


@st.cache_resource
def load_model():
    return joblib.load('lf_lgbm_bank_marketing_final.pkl')

model = load_model()

# 2. Mapping Dictionaries
edu_map = {
    'illiterate': 0, 'basic.4y': 1, 'basic.6y': 2, 'basic.9y': 3, 
    'high.school': 4, 'professional.course': 5, 'university.degree': 6, 'unknown': 7
}
age_map = {
    'Student_Age': 0, 'Young_Adult': 1, 'Adult': 2, 'Senior': 3
}

# --- UI SETUP ---
st.set_page_config(page_title="Bank Marketing Prediction", layout="wide")
st.title("🏦 Bank Marketing Campaign Prediction")

with st.form("main_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("👤 Profile")
        education_raw = st.selectbox("Education", list(edu_map.keys()))
        age_raw = st.selectbox("Age Group", list(age_map.keys()))
        job = st.selectbox("Job", ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'])
        is_married = st.selectbox("Is Married?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

    with col2:
        st.subheader("📞 Campaign")
        contact = st.selectbox("Contact", ['cellular', 'telephone'])
        month = st.selectbox("Month", ['mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        day = st.selectbox("Day", ['mon', 'tue', 'wed', 'thu', 'fri'])
        poutcome = st.selectbox("P-Outcome", ['nonexistent', 'failure', 'success'])
        intensity = st.selectbox("Intensity", ['low', 'medium', 'high'])
        campaign = st.number_input("Campaign Count", min_value=1, value=1)
        previous = st.number_input("Previous Count", min_value=0, value=0)

    with col3:
        st.subheader("📉 Economic")
        cp_idx = st.number_input("Cons Price Idx", value=93.0, format="%.3f")
        cc_idx = st.number_input("Cons Conf Idx", value=-40.0, format="%.1f")
        e3m = st.number_input("Euribor 3M", value=3.5, format="%.3f")
        pc_idx = st.number_input("Price Conf Idx", value=0.0, format="%.2f")
        
        default = st.selectbox("Default", ['no', 'unknown', 'yes'])
        housing = st.selectbox("Housing", ['no', 'yes', 'unknown'])
        loan = st.selectbox("Loan", ['no', 'yes', 'unknown'])
        never_con = st.selectbox("Never Contacted?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        eco_grow = st.selectbox("Eco Growing?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

    submitted = st.form_submit_button("Predict Subscription")

if submitted:
    # Ordinal Mapping Process
    edu_mapped = edu_map[education_raw]
    age_mapped = age_map[age_raw]

    
    input_data = {
        'default': str(default),
        'housing': str(housing),
        'loan': str(loan),
        'contact': str(contact),
        'month': str(month),
        'day_of_week': str(day),
        'campaign': float(campaign),
        'previous': float(previous),
        'poutcome': str(poutcome),
        'cons.price.idx': float(cp_idx),
        'cons.conf.idx': float(cc_idx),
        'euribor3m': float(e3m),
        'job_category': str(job),
        'education_level': float(edu_mapped), 
        'is_married': float(is_married),      
        'age_bin': float(age_mapped),         
        'never_contacted': float(never_con),
        'campaign_intensity': str(intensity),
        'price_conf_index': float(pc_idx),
        'economy_growing': float(eco_grow)
    }

    df_input = pd.DataFrame([input_data])

    feature_order = [
        'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 
        'campaign', 'previous', 'poutcome', 'cons.price.idx', 
        'cons.conf.idx', 'euribor3m', 'job_category', 'education_level', 
        'is_married', 'age_bin', 'never_contacted', 'campaign_intensity', 
        'price_conf_index', 'economy_growing'
    ]
    df_input = df_input[feature_order]

    nominal_features = ['job_category', 'default', 'housing', 'loan', 'contact', 'month', 'campaign_intensity','day_of_week', 'poutcome']
    for col in nominal_features:
        df_input[col] = df_input[col].astype(str)

    numeric_and_others = [c for c in feature_order if c not in nominal_features]
    for col in numeric_and_others:
        df_input[col] = pd.to_numeric(df_input[col], errors='coerce').fillna(0).astype(float)


    try:
        prediction = model.predict(df_input)
        probability = model.predict_proba(df_input)[0][1]

        st.divider()
        if prediction[0] == 1:
            st.success(f"🎯 **YES!** Customers will most likely subscribe. (Probability: {probability:.2%})")
        else:
            st.error(f"❌ **NO.** Customers will most likely not subscribe. (Probability: {probability:.2%})")
            
    except Exception as e:
        st.error(f"Terjadi Kesalahan: {e}")
        st.write("Debug - Data sent to the model:")
        st.dataframe(df_input)
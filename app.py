import streamlit as st
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

st.set_page_config(page_title="A/B Experimentation Decision Engine", layout="wide")
st.title("E-Commerce A/B Testing & Experimentation Decision Engine")
st.markdown("**Author:** Ugochukwu Henry Emenike | [SIA Benics Digital Solutions](https://benicsdigitalsolutions.com)")

uploaded = st.file_uploader("Upload Experiment CSV (requires 'group' and 'converted' columns)", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    if 'landing_page' in df.columns:
        df = df[((df['group'] == 'control') & (df['landing_page'] == 'old_page')) |
                ((df['group'] == 'treatment') & (df['landing_page'] == 'new_page'))].drop_duplicates('user_id')

    res = df.groupby('group')['converted'].agg(Users='count', Conversions='sum', Conv_Rate='mean')
    ci_low, ci_high = proportion_confint(res['Conversions'], res['Users'], alpha=0.05)
    res['95% CI Low'] = ci_low
    res['95% CI High'] = ci_high

    st.subheader("Experiment Group Performance")
    st.dataframe(res.style.format({'Conv_Rate': '{:.2%}', '95% CI Low': '{:.2%}', '95% CI High': '{:.2%}'}))

    z_stat, p_val = proportions_ztest(res['Conversions'], res['Users'])
    lift = (res.loc['treatment', 'Conv_Rate'] - res.loc['control', 'Conv_Rate']) / res.loc['control', 'Conv_Rate']

    col1, col2, col3 = st.columns(3)
    col1.metric("Relative Conversion Lift", f"{lift:+.2%}")
    col2.metric("P-Value", f"{p_val:.4f}")
    col3.metric("Ship Decision", "SHIP (Significant)" if p_val < 0.05 else "DO NOT SHIP")
else:
    st.info("Upload `ab_data.csv` to compute conversion lift, 95% confidence intervals, and statistical significance.")
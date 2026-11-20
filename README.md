# E-Commerce A/B Testing & Experimentation Decision Engine

## 1. Business Objective
Evaluate whether a newly designed e-commerce checkout landing page (`treatment` / `new_page`) generates a statistically significant lift in user conversion rate compared to the existing page (`control` / `old_page`), and deploy a self-service **Streamlit** decision app so product teams can evaluate future experiments without manual scripting.

## 2. Repository Contents
* **`ab_testing_analysis.ipynb`**: End-to-end Google Colab notebook covering experiment data quality validation, duplicate user deduplication, two-proportion Z-test, 95% confidence interval estimation, and visualization.
* **`app.py`**: Interactive Streamlit web application enabling product managers to upload experiment CSV logs and instantly calculate conversion rates, relative lift, 95% confidence intervals, $p$-values, and ship/no-ship recommendations.
* **`requirements.txt`**: Python dependencies (`streamlit`, `pandas`, `statsmodels`) for one-click deployment on Streamlit Community Cloud.
* **`ab_test_results_summary.csv`**: Aggregated experiment performance table across control and treatment cohorts.
* **`ab_test_conversion_chart.png`**: Conversion rate comparison chart with 95% confidence interval error bars.

## 3. Data Quality & Key Findings
* **Data Quality QA:** Filtered out `3,893` mismatched assignment records (where control users saw `new_page` or treatment users saw `old_page`) and deduplicated repeat user IDs, yielding **290,584 clean unique users** (`145,274` control vs. `145,310` treatment).
* **Conversion Performance:**
  * **Control (`old_page`):** `12.04%` conversion rate (`17,489` conversions)
  * **Treatment (`new_page`):** `11.88%` conversion rate (`17,264` conversions)
  * **Relative Lift:** `-1.31%`
* **Statistical Significance & Product Decision:** Two-proportion Z-test returned **$Z = 1.311$** and **$p = 0.1899$** ($p \ge 0.05$). **Decision: DO NOT SHIP** — the new checkout page failed to outperform the control page, preventing a rollout that would have slightly degraded conversion.

## 4. Tech Stack & Dataset
* **Tools:** Python (`pandas`, `statsmodels`, `matplotlib`), Google Colab, Streamlit
* **Dataset:** [E-Commerce A/B Testing Dataset (`ab_data.csv` — Kaggle)](https://www.kaggle.com/datasets/zhangluyuan/ab-testing)

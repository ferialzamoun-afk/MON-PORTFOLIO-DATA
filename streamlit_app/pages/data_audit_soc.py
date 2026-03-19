import streamlit as st
import pandas as pd

# Configuration page
st.set_page_config(page_title="SOC Monitoring - Data Audit", layout="wide")

st.title("🛡️ SOC Monitoring Dashboard")
st.subheader("Data Anomaly Detection & Risk Classification")

# =========================
# INCIDENT METRICS
# =========================

st.markdown("## 🚨 Incident Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🔴 Critical Incidents", 5)
col2.metric("🟠 High Priority", 100)
col3.metric("🟡 Medium Priority", 90)
col4.metric("✅ Data Matching Rate", "89%")

st.divider()

# =========================
# INCIDENT DETAILS
# =========================

st.markdown("## 📋 Incident Breakdown")

incident_data = {
    "Incident Type": [
        "Negative Prices",
        "Negative Stocks",
        "Negative Margins",
        "Stock Status Inconsistency",
        "Orphan Products"
    ],
    "Count": [3, 2, 7, 2, 91],
    "Severity": [
        "🔴 Critical",
        "🔴 Critical",
        "🟠 High",
        "🟠 High",
        "🟠 High"
    ]
}

df_incidents = pd.DataFrame(incident_data)

st.dataframe(df_incidents, use_container_width=True)

st.divider()

# =========================
# RISK ANALYSIS
# =========================

st.markdown("## 📊 Risk Distribution")

risk_data = pd.DataFrame({
    "Severity": ["Critical", "High", "Medium"],
    "Count": [5, 100, 90]
})

st.bar_chart(risk_data.set_index("Severity"))

st.divider()

# =========================
# ANALYST NOTES
# =========================

st.markdown("## 🧠 Analyst Assessment")

st.info("""
This dashboard simulates a Security Operations Center (SOC) approach applied to data quality monitoring.

Key observations:
- Critical anomalies detected (impossible values)
- Business logic inconsistencies identified
- Data integrity risks classified by severity
- Immediate remediation recommended for critical cases

The anomaly detection logic mirrors cybersecurity monitoring:
- Impossible values → Intrusion indicators
- System inconsistencies → Integrity breach signals
- Orphan records → Unauthorized objects/accounts
""")

st.success("✅ Monitoring Active - No new critical escalation detected")
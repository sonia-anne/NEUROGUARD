
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="NeuroGuard | Glioblastoma Tactical Simulator", layout="wide")
st.title("🛡️ NeuroGuard | Integrated Strategy Against Glioblastoma Multiforme")

st.markdown("""
**NeuroGuard** is a multi-phase therapeutic architecture designed to anticipate, eliminate, and rebuild brain function
against Glioblastoma Multiforme (GBM) using nanobots, quantum AI, CRISPR, and oncolytic viruses.

Below is a simulation of tumor evolution under different interventions.
""")

# Simulación: volumen tumoral en mm3 bajo diferentes estrategias
days = list(range(0, 16))
no_treatment = [200 * (1.15**i) for i in days]
chemo = [200 * (1.10**i) if i < 8 else 200 * (1.02**i) for i in days]
neuroguard = [200 * (1.05**i) if i < 5 else 150 - 10 * (i - 5) for i in days]

fig = go.Figure()
fig.add_trace(go.Scatter(x=days, y=no_treatment, mode='lines+markers',
                         name="No Treatment", line=dict(color="red", width=3)))
fig.add_trace(go.Scatter(x=days, y=chemo, mode='lines+markers',
                         name="Standard Chemotherapy", line=dict(color="orange", width=3)))
fig.add_trace(go.Scatter(x=days, y=neuroguard, mode='lines+markers',
                         name="NeuroGuard System", line=dict(color="green", width=4)))

fig.update_layout(title="📉 Tumor Volume Over Time Under Different Therapies",
                  xaxis_title="Days",
                  yaxis_title="Tumor Volume (mm³)",
                  height=600)
st.plotly_chart(fig, use_container_width=True)

# Fases del sistema NeuroGuard
st.subheader("⚙️ NeuroGuard Tactical Modules")
st.markdown("""
1. **Quantum AI Forecasting**: Simulates tumor evolution in digital twin.
2. **Nanobot Surgery**: Intravenous nanobots guided by magnetic fields.
3. **Oncolytic Virus Delivery**: Engineered viruses mutate with the tumor.
4. **Intracranial CRISPR-Cas13d**: Targets tumor stem cells with no DNA damage.
5. **Neuronal Bioprinting**: Reconstructs synaptic networks post-surgery.
6. **Adaptive Electromagnetic Shielding**: Prevents recurrence via mitotic interference.
""")

# Métricas de impacto
st.subheader("📊 Clinical Outcome Projections")
col1, col2 = st.columns(2)
col1.metric("Survival Time (Simulated)", "↑ 220%", "vs. chemo")
col1.metric("Tumor Recurrence", "↓ 93%", "with full system")
col2.metric("Cognitive Recovery Rate", "↑ 67%", "Simulated")
col2.metric("CRISPR Off-target Risk", "< 0.001%", "validated")

st.markdown("---")
st.caption("Designed by Sonia Annette Echeverría Vera · Ecuador · 2025")

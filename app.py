import streamlit as st
import xRM_calculator
import oly_xRM_calculator
import pandas as pd

st.set_page_config(
    page_title="xRM Calculator",
    page_icon="🏋️",
)

def calculator(prefix, maxReps, repValue, script):
    weight = st.number_input("Weight lifted", key=f"{prefix}_weight", min_value=0.0, step=0.25, value=40.0, help="How much weight you lifted")
    reps = st.select_slider("Repetitions", key=f"{prefix}_reps", options=list(range(1,maxReps+1)), value=repValue, help="How many repetitions you did with that weight")
    rir = st.select_slider("RIR", key=f"{prefix}_rir", options=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], value=1, help="How many reps in reserve you had after doing the given weight for the given number of repetitions")

    oneRM, sheet = script(weight, reps, rir)

    chart = pd.DataFrame(
        {"RIR 0": sheet[0], "RIR 0.5": sheet[1], "RIR 1": sheet[2], "RIR 1.5": sheet[3], "RIR 2": sheet[4], "RIR 2.5": sheet[5], "RIR 3": sheet[6], "RIR 3.5": sheet[7], "RIR 4": sheet[8]}, index=list(range(1,maxReps+1))
    )
    chart.index.name = "Reps"
    styledChart = chart.style.format(precision=2).set_table_styles([
        {"selector": "td", "props": "text-align: center !important;"},
        {"selector": "th", "props": "text-align: center !important; font-weight: bold;"}
    ])

    st.metric("Estimated 1RM:", round(oneRM, 2), help="Your estimated 1RM based on the information you gave")
    st.markdown("**Rep max sheet**", help="This sheet shows what weight you can do at a given number of repetitions, and a given number of reps in reserve")
    st.table(styledChart)


st.title("xRM Calculator")

#tabs
liftTab, olyTab = st.tabs(["Lifts", "Olympic lifts"])

with liftTab:
    calculator("lift", 12, 5, xRM_calculator.xRMCalculator)

with olyTab:
    calculator("oly", 5, 2, oly_xRM_calculator.xRMCalculator)

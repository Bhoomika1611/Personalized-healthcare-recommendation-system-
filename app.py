import streamlit as st
import pandas as pd

# ------------------ Load Data ------------------
@st.cache_data
def load_data():
    symptoms_df = pd.read_csv("Symptom-severity.csv")
    training_df = pd.read_csv("Training.csv")
    desc_df = pd.read_csv("description.csv")
    diets_df = pd.read_csv("diets.csv")
    meds_df = pd.read_csv("medications.csv")
    prec_df = pd.read_csv("precautions_df.csv")
    workout_df = pd.read_csv("workout_df.csv")
    return symptoms_df, training_df, desc_df, diets_df, meds_df, prec_df, workout_df

symptoms_df, training_df, desc_df, diets_df, meds_df, prec_df, workout_df = load_data()


# ------------------ UI ------------------
st.set_page_config(page_title="Healthcare Recommendation System", layout="centered")
st.title("🩺 Personalized Healthcare Recommendation System")

st.write("Select your symptoms to get disease prediction and health recommendations.")

# ------------------ Symptoms List ------------------
symptom_list = sorted(symptoms_df["Symptom"].str.replace("_", " ").unique())

selected_symptoms = st.multiselect(
    "Select Symptoms:",
    symptom_list
)

if st.button("Predict Disease"):
    if len(selected_symptoms) == 0:
        st.warning("⚠ Please select at least one symptom.")
    else:
        selected_symptoms = [s.replace(" ", "_") for s in selected_symptoms]

        max_match = 0
        predicted_disease = None

        for _, row in training_df.iterrows():
            match_count = 0
            for symptom in selected_symptoms:
                if symptom in training_df.columns and row[symptom] == 1:
                    match_count += 1

            if match_count > max_match:
                max_match = match_count
                predicted_disease = row["prognosis"]

        if predicted_disease is None or max_match == 0:
            st.error("❌ No disease found for the selected symptoms.")
        else:
            disease = predicted_disease   # ✅ FIX HERE

            st.success(f"✅ Predicted Disease: **{disease}**")
            st.info(f"Matched Symptoms: {max_match} / {len(selected_symptoms)}")

            # -------- Description --------
            desc = desc_df[desc_df["Disease"] == disease]["Description"]
            if not desc.empty:
                st.subheader("📌 Description")
                st.write(desc.values[0])

            # -------- Diet --------
            diet = diets_df[diets_df["Disease"] == disease]["Diet"]
            if not diet.empty:
                st.subheader("🥗 Recommended Diet")
                st.write(diet.values[0])

            # -------- Workout --------
            workout = workout_df[workout_df["disease"] == disease]["workout"]
            if not workout.empty:
                st.subheader("🏃 Recommended Workout")
                st.write(workout.values[0])

            # -------- Medication --------
            meds = meds_df[meds_df["Disease"] == disease]["Medication"]
            if not meds.empty:
                st.subheader("💊 Medications")
                st.write(meds.values[0])

            # -------- Precautions --------
            prec_row = prec_df[prec_df["Disease"] == disease]

            if not prec_row.empty:
                st.subheader("⚠ Precautions")
                precautions = prec_row[
                    ["Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"]
                ].values[0]

                for p in precautions:
                    st.write("•", p)


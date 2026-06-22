# Personalized Healthcare Recommendation System

## Overview

This project is a Streamlit-based healthcare recommendation system that predicts a likely disease based on selected symptoms and provides personalized recommendations including disease description, diet guidance, workout advice, medications, and precautions.

The application uses a symptoms dataset and a training dataset to match user-selected symptoms against known disease profiles.

## Features

- Symptom-based disease prediction
- Disease description lookup
- Recommended diet plan
- Recommended workout guidance
- Medication suggestions
- Health precautions display
- Clean and interactive Streamlit interface

## Tech Stack

- Python
- Streamlit
- Pandas

## Getting Started

### Prerequisites

- Python 3.8 or newer
- pip package manager

### Installation

1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Install required packages:

```bash
pip install streamlit pandas
```

### Run the App

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal (usually `http://localhost:8501`).

## Project Structure

- `app.py` - Main Streamlit app interface and prediction logic
- `Datasets/` - CSV files used to support disease prediction and recommendations
- `Medicine recommendation system.ipynb` - Notebook containing exploratory analysis or development notes
- `model.pkl` - Serialized model artifact (if used for future extension)

## Dataset Files

- `Datasets/Symptom-severity.csv` - Symptom list and severity information
- `Datasets/Training.csv` - Disease training set used for matching symptoms to prognosis
- `Datasets/description.csv` - Disease descriptions
- `Datasets/diets.csv` - Diet recommendations by disease
- `Datasets/medications.csv` - Medication guidance by disease
- `Datasets/precautions_df.csv` - Precaution recommendations by disease
- `Datasets/workout_df.csv` - Workout suggestions by disease

## Usage

1. Open the app in your browser.
2. Select one or more symptoms from the symptom picker.
3. Click `Predict Disease` to view the most likely disease along with recommendations.

## Notes

- The prediction logic is based on symptom matching from the training dataset.
- The app displays recommendations only when a disease match is found.
- The datasets drive the content shown for disease description, diet, medications, workouts, and precautions.

## License

This project is provided as-is for educational and demonstration purposes.

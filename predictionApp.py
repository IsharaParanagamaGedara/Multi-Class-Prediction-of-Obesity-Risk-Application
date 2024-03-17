import streamlit as st
import pickle

def load_model(model_path):
    return pickle.load(open(model_path, 'rb'))

def main():
    st.title("Obesity Risk Prediction App")
    st.write("This app predicts the risk of obesity based on various input features.")

    # Load the model
    model_path = "best_model.pk"  
    model = load_model(model_path)

    # Feature explanations
    st.sidebar.markdown("### Feature Explanations:")
    st.sidebar.write("- Family history with overweight: Yes or No")
    st.sidebar.write("- Age: Age of the individual")
    st.sidebar.write("- Consumption of food between meals: No, Sometimes, Frequently, Always")
    st.sidebar.write("- Consumption of water daily: Amount of water consumed daily")
    st.sidebar.write("- Calories consumption monitoring: Yes or No")
    st.sidebar.write("- Number of main meals: Low, Medium, High")
    st.sidebar.write("- Consumption of alcohol: NO, Sometimes, Frequently, Always")
    st.sidebar.write("- Frequent consumption of high caloric food: Yes or No")
    st.sidebar.write("- Height: Height of the individual (in cm)")
    st.sidebar.write("- Frequency of consumption of vegetables: How often vegetables are consumed")
    st.sidebar.write("- Weight: Weight of the individual (in kg)")
    st.sidebar.write("- Gender: Male or Female")

    # Gather user input using Streamlit widgets
    family_history_with_overweight = st.selectbox("Family history with overweight", ["No", "Yes"])
    Age = st.slider("Age", min_value=0, max_value=100)
    CAEC = st.selectbox("Consumption of food between meals", ["No", "Sometimes", "Frequently", "Always"])
    CH2O = st.slider("Consumption of water daily", min_value=0.0, max_value=10.0)
    SCC = st.selectbox("Calories consumption monitoring", ["No", "Yes"])
    NCP = st.selectbox("Number of main meals", ["Low", "Medium", "High"])
    CALC = st.selectbox("Consumption of alcohol", ["No", "Sometimes", "Frequently", "Always"])
    FAVC = st.selectbox("Frequent consumption of high caloric food", ["No", "Yes"])
    Height = st.number_input("Height (in cm)", min_value=50.0, max_value=250.0)
    FCVC = st.slider("Frequency of consumption of vegetables", min_value=0.0, max_value=10.0)
    Weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=500.0)
    Gender = st.radio("Gender", ["Female", "Male"])

    # Buttons for actions
    predict_button = st.button("Predict")
    clear_button = st.button("Clear Results")

    if predict_button:
        # Map categorical values
        family_history_with_overweight = 1 if family_history_with_overweight.lower() == 'yes' else 0
        CAEC_mapping = {'no': 0, 'sometimes': 1, 'frequently': 2, 'always': 3}
        CAEC = CAEC_mapping.get(CAEC.lower(), -1)
        SCC = 1 if SCC.lower() == 'yes' else 0
        NCP_mapping = {'low': 0, 'medium': 1, 'high': 2}
        NCP = NCP_mapping.get(NCP.lower(), -1)
        CALC_mapping = {'no': 0, 'sometimes': 1, 'frequently': 2, 'always': 3}
        CALC = CALC_mapping.get(CALC.lower(), -1)
        FAVC = 1 if FAVC.lower() == 'yes' else 0
        Gender = 1 if Gender.lower() == 'male' else 0

        # Make a prediction
        pred = model.predict([[family_history_with_overweight, Age, CAEC, CH2O, SCC, NCP, CALC, FAVC, Height, FCVC, Weight, Gender]])

        # Interpret the prediction
        prediction_label = get_prediction_label(pred[0])

        # Display the prediction
        st.write(f"The predicted class is: {prediction_label}")

    if clear_button:
        st.text("")  # Clear the result area

def get_prediction_label(prediction):
    labels = [
        'Insufficient_Weight',
        'Normal_Weight',
        'Obesity_Type_I',
        'Obesity_Type_II',
        'Obesity_Type_III',
        'Overweight_Level_I',
        'Overweight_Level_II'
    ]
    return labels[prediction]

if __name__ == "__main__":
    main()

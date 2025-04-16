import streamlit as st 

st.title("BMI Calculator")
st.write("Enter your height and weight to calculate your BMI")


height = st.number_input ("Height (in meters)",min_value= 0.5 ,max_value=3.0, value= 1.75)
weight = st.number_input ("Weight (in kilograms)",min_value= 10, max_value=150, value=80)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height **2)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi <= 18.5:
            st.warning("You're underweight")
        elif bmi <= 24.9:
            catagory=("You have a normal body weight")
        elif bmi <= 29.9:
            st.warning("You're overweight")
        else :
            st.error("You're Obese")


    else:
        st.warning("Please enter valid height and weight values")
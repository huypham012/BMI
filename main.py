import streamlit as st
st.header('Welcome to BMI Caculator')
weight = st.number_input('Enter your weight(in kilograms)')
height_unit = st.radio('Select your height format' , options=['Centimeters','Decimeters','Meters'])
st.write(f'Write your height in {str(height_unit)}(bigger than 0)')
height = st.number_input('')
BMI = 0
if height_unit == 'Centimeters':
    BMI = weight / (height * height) * 10000
elif height_unit == 'Decimeters':
    BMI = weight / (height * height) * 100
else:
    BMI= weight / (height * height)
def Caculate():
    st.write(f'Your BMI Index is {BMI}')
    if BMI < 18.5:
        st.info('Light weight')
    if 18.4 < BMI < 25:
        st.success('Normal weight')
    if 24.9 < BMI < 30:
        st.warning('Overweight')
    if 29.9 < BMI < 35:
        st.error('Grade 1 obesity')
    if 34.9 < BMI:
        st.exception('Obesity grade 2 or higher')
if st.button('Caculate BMI'):
    Caculate()
st.image('BMI.png')

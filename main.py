import streamlit as st
st.header('Welcome to BMI Caculator')
can = st.number_input('Enter your weight(in kilograms)')
don_vi = st.radio('Select your height format' , options=['Centimeters','Decimeters','Meters'])
st.write(f'Write your height in {str(don_vi)}(bigger than 0)')
chieu_cao = st.number_input('')
BMI = 0
if don_vi == 'Centimeters':
    BMI = can / chieu_cao / chieu_cao * 10000
elif don_vi == 'Decimeters':
    BMI = can / chieu_cao / chieu_cao * 100
else:
    BMI= can / chieu_cao / chieu_cao
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

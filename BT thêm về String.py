import streamlit as st
#Bài 1
Ten = str(st.text_input('Hãy nhập tên của bạn:'))
KQ = 0
for i in range(len(Ten)-1):
    CH_C = Ten[i]
    if CH_C == ' ':
        KQ += 1
if KQ > 0:
    st.write(f'Có {KQ+1} từ trong tiếng đó')
elif KQ == 0 and len(Ten) > 0:
    st.write('Có 1 từ trong tiếng đó')
else:
    st.write('Có 0 từ trong tiếng đó')
#Bài 2
so_chung_minh = st.text_input('Hãy nhập số chứng minh nhân dân của bạn:')
if so_chung_minh.isdigit() and 8 < len(so_chung_minh) < 12:
    st.write('Số chứng minh nhân dân của bạn nhập đúng!')
else:
    st.write('Số chứng minh nhân dân của bạn nhập sai!')
#Bài 3
email = st.text_input("Hãy nhập địa chỉ email của bạn: ")
if email.count("@") == 1 and email.endswith(".com") and " " not in email:
    st.write("Địa chỉ email bạn nhập hợp lệ")
else:
    st.write("Địa chỉ email bạn nhập không hợp lệ không hợp lệ")
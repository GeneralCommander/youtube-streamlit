import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバー表示')
# ’Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itetation {i+1}')
    bar.progress(i + 1)
    time.sleep(1)

# 'Done!!!!!'

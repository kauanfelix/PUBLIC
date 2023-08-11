import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner  

qr_code = qrcode_scanner(key='qrcode_scanner')  
qr_code
if qr_code:
  st.write(qr_code) 





import streamlit as st
import streamlit.components.v1 as components

html_string = '''
<form>
  <label for="telefone">Número de celular:</label><br>
  <input type="tel" id="telefone" name="telefone" pattern="[0-9]{2}-[0-9]{5}-[0-9]{4}" required><br>
  <small>Formato: 99-99999-9999</small><br><br>
  <input type="submit">
</form>

'''

components.html(html_string)  # JavaScript works

st.markdown(html_string, unsafe_allow_html=True)

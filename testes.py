import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner 
from PIL import Image
from pyzbar.pyzbar import decode
from pillow_heif import register_heif_opener

funcao = st.selectbox(label='Importar chavde de acesso por:', options=["CÓDDIGO BARRAS UPLOAD", "CÓDDIGO BARRAS CAMERA", "QRCODE"])
if funcao == 'CÓDDIGO BARRAS UPLOAD':
  from PIL import Image
  from pyzbar.pyzbar import decode
  from pillow_heif import register_heif_opener
  im_UPLOAD = st.file_uploader("Upload photo here", label_visibility='hidden', type=['png', 'jpeg', 'jpg'])

  if im_UPLOAD is not None:
    im_OPEN = Image.open(im_UPLOAD)
    im_RGB = im_OPEN.convert('RGB')
    st.image(im_OPEN)
    barcodes = decode(im_RGB)
    for barcode in barcodes:
        st.code(barcode.data.decode())
    if not barcodes:
        st.warning("CODIGO BARRAS ILEGIVEL")

if funcao == 'CÓDDIGO BARRAS CAMERA':
  code_128 = qrcode_scanner(key='CODE_128')  
  if code_128:
    st.code(code_128)

if funcao == 'QRCODE':
  qr_code = qrcode_scanner(key='qr_code')  
  if qr_code:
    st.code(qr_code) 

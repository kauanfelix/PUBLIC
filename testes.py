import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner 

# from PIL import Image
# from pyzbar.pyzbar import decode
# from pillow_heif import register_heif_opener

tab1, tab2 = st.tabs(["CÓDDIGO BARRAS TESTES", "CÓDDIGO BARRAS "])
# with tab1:
#   register_heif_opener()
#   image = st.file_uploader(label="Upload photo here", label_visibility='hidden')
#   if image is not None:
#       imagem_aberta = Image.open(image)
#       imagem_RGB = imagem_aberta.convert('RGB')  # Convert to greyscale to enforce HEIC data
#       barcodes = decode(imagem_RGB)
#       for codigo_barras in barcodes:
#           st.code(codigo_barras)
#       if not barcodes:
#           st.warning("CÓDIGOS BARRAS NÃO ENCONTRADO")

with tab2:
  qr_code = qrcode_scanner(key='CODE_128')  
  qr_code
  if qr_code:
    st.code(qr_code) 


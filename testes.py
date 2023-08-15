import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner 

# from PIL import Image
# from pyzbar.pyzbar import decode
# from pillow_heif import register_heif_opener

tab1, tab2, tab3 = st.tabs(["CÓDDIGO BARRAS UPLOAD", "CÓDDIGO BARRAS CAMERA", "QRCODE"])
with tab1:
  from PIL import Image
  from pyzbar.pyzbar import decode
  from pillow_heif import register_heif_opener
  image = st.file_uploader("Upload photo here", label_visibility='hidden')
  def display_links(barcode):
    st.header(f"Barcode: {barcode}")
    if image is not None:
    im = Image.open(image)
    im_greyscale = im.convert('RGB')  # Convert to greyscale to enforce HEIC data
    barcodes = decode(im_greyscale)
    for barcode in barcodes:
        display_links(barcode.data.decode())
    if not barcodes:
        st.warning("ERRO.")

with tab2:
  qr_code = qrcode_scanner(key='CODE_128')  
  if qr_code:
    st.code(qr_code) 
with tab3:
  qr_code = qrcode_scanner(key='qr_code')  
  if qr_code:
    st.code(qr_code) 


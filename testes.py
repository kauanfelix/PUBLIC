# import streamlit as st 
# from streamlit_qrcode_scanner import qrcode_scanner 
# from PIL import Image
# from pyzbar.pyzbar import decode
# from pillow_heif import register_heif_opener

# funcao = st.selectbox(label='Importar chave de acesso por:', options=["CÓDIGO BARRAS UPLOAD", "CÓDIGO BARRAS CAMERA", "QRCODE"])
# if funcao == 'CÓDDIGO BARRAS UPLOAD':
#   im_UPLOAD = st.file_uploader("Upload photo here", label_visibility='hidden', type=['png', 'jpeg', 'jpg'])
#   if im_UPLOAD is not None:
#     im_OPEN = Image.open(im_UPLOAD)
#     im_RGB = im_OPEN.convert('RGB')
#     st.image(im_OPEN)
#     barcodes = decode(im_RGB)
#     for barcode in barcodes:
#         st.text_input(label='Código Barras:',value=barcode.data.decode())
#     if not barcodes:
#         st.warning("CODIGO BARRAS ILEGIVEL")

# if funcao == 'CÓDIGO BARRAS CAMERA':
#   code_128 = qrcode_scanner(key='CODE_128')  
#   if code_128:
#     st.text_input(label='Código Barras:',value=code_128)

# if funcao == 'QRCODE':
#   qr_code = qrcode_scanner(key='qr_code')  
#   if qr_code:
#     st.text_input(label='Código Barras:',value=qr_code) 

import streamlit as st
from streamlit.components.v1 import html


html("""
<!DOCTYPE html>
    <html>
    <head>
      <title>CPF</title>
      <style>
        input {padding: 10px; font-size: 12px;}
      </style>
    </head>
    <body>
      <label for="cpf">CPF:</label>
      <input type="text" id="cpf" maxlength="14" oninput="formatarCPF(this)" placeholder="000.000.000-00">

      <script>
        function formatarCPF(campo) {
          let cpf = campo.value;

          cpf = cpf.replace(/\D/g, '');
          cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
          cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
          cpf = cpf.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

          campo.value = cpf;
        }
      </script>
    </body>
    </html>
""")

if "stValue" in st.session_state:
    st.write("Valor digitado: " + st.session_state.stValue)


html("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Leitor de Código de Barras Code 128</title>
    <script src="https://cdn.rawgit.com/lindell/JsQR/master/dist/jsQR.js"></script>
    <script src="https://cdn.rawgit.com/lindell/JsQR/master/dist/locator.js"></script>
    <script src="https://cdn.rawgit.com/lindell/JsQR/master/dist/init.js"></script>
</head>
<body>
    <h1>Leitor de Código de Barras Code 128</h1>
    <canvas id="barcodeCanvas"></canvas>
    <input type="text" id="decodedBarcode" readonly>
    
    <script>
        function generateBarcode(code) {
            JsBarcode("#barcodeCanvas", code, { format: "CODE128" });
        }

        function decodeBarcodeFromCanvas() {
            const canvas = document.getElementById("barcodeCanvas");
            const context = canvas.getContext("2d");
            const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
            const code = jsQR(imageData.data, imageData.width, imageData.height);

            if (code) {
                const decodedBarcode = code.data;
                document.getElementById("decodedBarcode").value = decodedBarcode;
            } else {
                alert("Código de barras não detectado.");
            }
        }

        // Exemplo de uso:
        generateBarcode("123456789"); // Gere um código de barras Code 128
        decodeBarcodeFromCanvas(); // Decodifique o código de barras gerado
    </script>
</body>
</html>

""")


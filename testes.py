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
    <title>Leitor de Código de Barras</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/quagga/0.12.1/quagga.min.js"></script>
</head>
<body>
    <h1>Leitor de Código de Barras</h1>
    <div id="interactive" class="viewport"></div>

    <script>
        Quagga.init({
            inputStream: {
                name: "Live",
                type: "LiveStream",
                target: document.querySelector('#interactive'),
                constraints: {
                    width: 640,
                    height: 480,
                    facingMode: "environment"
                },
            },
            decoder: {
                readers: ["ean_reader"]
            }
        }, function (err) {
            if (err) {
                console.error(err);
                return;
            }
            console.log("QuaggaJS inicializado com sucesso.");
            Quagga.start();
        });

        Quagga.onDetected(function (result) {
            console.log("Código de barras detectado: " + result.codeResult.code);
            // Faça o que desejar com o código de barras detectado aqui
            alert("Código de barras detectado: " + result.codeResult.code);
        });
    </script>
</body>
</html>
""")


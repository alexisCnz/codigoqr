import qrcode #importamos la libreria que ocuparemos

filename = "qr_code_alexis.png" #nombre del archivo que vamos a generar
url = "https://www.linkedin.com/in/alexis-constanzo-pino-14a241261/"

#toda este codigo esta en la pagina de la libreria 
#esta funcion genera un codigo qr y lo guarda en el archivo que le pasemos como parametro
def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=6,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
#llamamos a la funcion 
generate_qr_code(url, filename)





import PyPDF2
pdfpass = PyPDF2.PdfReader('luis.pdf')

# Para limpiar los caracteres no utf8 ( en linux ) del rockyou.txt:  iconv -f utf-8 -t utf-8 -c rockyou.txt > rockyou2.txt
# -f es formato original
# -t formato destino
# -c salta cualquier secuencia no válida

with open('rockyou2.txt', 'r', encoding='utf8') as f:
    # with open('kaonashi.txt', 'r') as f:
    for line in f:
        password = line.strip()
        if pdfpass.decrypt(password) != 0:
            print(f'contraseña encontrada {password}')
            break

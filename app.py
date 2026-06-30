import sys
from core.manager import Manager 

if len(sys.argv) < 2:
    print("Uso: python extraer_costos.py archivo.pdf")
    sys.exit()

pdf_path = sys.argv[1]

print(f"[APP] archivo recibido: {pdf_path}");

if (Manager.process(pdf_path) == 1):
    print("PDF extraído correctamente")

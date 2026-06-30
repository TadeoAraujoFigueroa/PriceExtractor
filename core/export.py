from pathlib import Path
import pandas as pd
class Export:

    @classmethod
    def export_to_excel(cls, dataToExport, pdf_path):
        nombre_salida = Path(pdf_path).stem + "_costos.xlsx";
        df = pd.DataFrame(dataToExport);
        df.to_excel(nombre_salida, index = False);
        print(f"[EXPORT] Archivo generado: {nombre_salida}")
        return 1;
    
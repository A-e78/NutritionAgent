import pandas as pd
import os

def excel_to_csv(excel_file, csv_file):
    """
    Convierte archivo Excel a CSV manteniendo la estructura
    """
    try:
        # Leer el archivo Excel
        df = pd.read_excel(excel_file)
        
        print(f"📊 Leyendo: {excel_file}")
        print(f"📋 Columnas encontradas: {list(df.columns)}")
        print(f"📝 Número de filas: {len(df)}")
        
        # Mostrar primeras filas para verificar
        print("\n🔍 Primeras 5 filas:")
        print(df.head())
        
        # Guardar como CSV
        df.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"\n✅ Convertido: {excel_file} → {csv_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error convirtiendo: {e}")
        return False

# Buscar archivos Excel en el proyecto
excel_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.xlsx', '.xls')):
            excel_files.append(os.path.join(root, file))

if excel_files:
    print("📁 Archivos Excel encontrados:")
    for i, file in enumerate(excel_files):
        print(f"  {i+1}. {file}")
    
    # Convertir el primer archivo encontrado
    excel_file = excel_files[0]
    csv_file = "data/Canasta.csv"
    
    # Asegurar que existe la carpeta data
    os.makedirs("data", exist_ok=True)
    
    excel_to_csv(excel_file, csv_file)
else:
    print("❌ No se encontraron archivos Excel (.xlsx, .xls)")
    print("📂 Archivos en el proyecto:")
    for root, dirs, files in os.walk('.'):
        for file in files[:10]:  # Mostrar primeros 10 archivos
            print(f"  - {os.path.join(root, file)}")

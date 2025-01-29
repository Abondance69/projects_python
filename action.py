import os
import pandas as pd
import PyPDF2

files = [
    "data/airlines.json",
    "data/flights.xlsx",
    "data/airports.xlsx",
    "data/weather.pdf",
    "data/planes.html"
]

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

def file_to_svg() :
    for file in files:
        filename, extension = os.path.splitext(os.path.basename(file))
        extension = extension[1:].lower()

        if extension == "json":
            df = pd.read_json(file)
        elif extension in ["xls", "xlsx"]:
            df = pd.read_excel(file)

            df = df.apply(lambda col: col.map(lambda x: x.strip('"') if isinstance(x, str) else x))
        elif extension == "html":
            tables = pd.read_html(file)
            df = tables[0] if tables else pd.DataFrame()
        elif extension == "pdf":
            text = ""

            with open(file, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages:
                    if page.extract_text():
                        text += page.extract_text() + "\n"

            lines = [line.split(",") for line in text.split("\n") if line.strip()]
            df = pd.DataFrame(lines)

        else:
            print(f"⚠ Format non supporté : {file}")
            continue

        df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

        csv_file_path = os.path.join(output_dir, f"{filename}.csv")
        df.to_csv(csv_file_path, index=False, header=False, encoding="utf-8")
        print(f"✅ Fichier CSV créé : {csv_file_path}")
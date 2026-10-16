"""Coach App - versão em Python (Flask) + HTML da folha DATA BASE.
Correr:  pip install -r requirements.txt  &&  python app.py   ->  http://localhost:5000
Os dados ficam guardados em data.json (ao lado deste ficheiro)."""
import json, os
from flask import Flask, jsonify, request, send_from_directory

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, "data.json")
app = Flask(__name__, static_folder=os.path.join(BASE, "static"))

# nome | unidade | proteína | gordura | hidratos  (valores por unidade indicada, como na folha BASE DADOS DIETA)
FOODS = """Carne de vaca 5% gordura|100g|25|6|0
Claras de ovo|100g|10|0.3|0
Peito de frango|100g|28|3.5|0
Whey|100g|86|0.3|1.2
Whey Isolada|100g|90|1|2.4
Salmão|100g|24|7.6|0.5
Bife de atum|100g|23|0.9|0
Ovo (M/L)|unid|7|6|0.6
Iogurte proteico|100g|7.3|0|4
Yopro|100g|8.3|0.5|5.3
Peito de perú|100g|29|3|0
Pescada|100g|20|3.5|0
Camarão cozido|100g|19|1|0
Iogurte grego ligeiro|100g|8|2|5.5
Seitan|100g|21|3.2|4
Tofu|100g|13|7|2.5
Lata de atum 85gr|unid|20|0.6|0
Iogurte Natural|100g|0|3.4|3
Manteiga Amendoim|100g|30|46|12
Azeite|100g|0|99|0
Abacate|100g|2|15|1.5
Nozes|100g|15|65|14
Chocolate negro 85% cacau|100g|12|46|7
Caju|100g|18|43|32
Arroz cozido|100g|2.5|0.2|28
Massa cozida|100g|6|0.6|29
Aveia|100g|13|6|62
Batata cozida|100g|1.6|0|17
Banana|100g|0|0|23
Maçã|100g|0|0|12
Cuscus|100g|12|2|67
Abacaxi|100g|0.5|0|12
Manga|100g|0.8|0.4|13
Mirtilos|100g|1|0|7
Laranja|100g|0.9|0.1|12
Pera|100g|0.4|0.1|15.5
Pão integral|unid|9|5|42
Quinoa cozida|100g|5|2|24
Morangos|100g|0.7|0.3|6
Bolachas de arroz|unid|0|0|5
Lentilhas|100g|6|0.7|8
Feijão preto cozido|100g|5|0.6|10
Grão de bico cozido|100g|4.95|1.1|22.6
Mel|100g|0|0|80
Vegetais à escolha|100g|0|0|0
Melancia|100g|0|0|7
Fatia de pão integral|unid|1.9|0.7|11
Pudim proteico|unid|20|3|10
Leite magro|100g|3|0|5
Queijo fresco magro|100g|12|1|6
Dourada|100g|19|0.7|0
Cavala|100g|19|9|0
Chia|100g|16|30|6
Soja texturizada|100g|52|7.6|11
Tempeh|100g|14.4|7.2|2
Peça de fruta à escolha|unid|0|0|16
Linhaça moída|100g|18|42|29
Arroz (pesado a Cru)|100g|6.8|1.1|78
Peito de Frango Cru|100g|23|1.2|0
Pescada Crua|100g|17|1.4|0
Carne vaca 5% gordura crua|100g|20.8|4.5|0
Esparguete (pesado a cru)|100g|13|1.5|76
Pão bijou|unid|3|2|21
Bagel|unid|9|1|44
Wrap|unid|3.76|2.92|22
Fatia pão de forma branco|unid|2.82|0.57|14.7
Leite proteico (mimosa)|100ml|10|0.4|4.9
Leite Meio gordo|100g|3.4|1.6|4.9
EAAs|100g|100|0|0
Dextrina Ciclica|100g|0|0|100"""

def parse_foods():
    out = []
    for line in FOODS.splitlines():
        n, u, p, f, h = line.split("|")
        out.append({"name": n, "unit": u, "p": float(p), "f": float(f), "h": float(h)})
    return out

@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.get("/api/foods")
def foods():
    return jsonify(parse_foods())

@app.get("/api/data")
def get_data():
    if os.path.exists(DB):
        with open(DB, encoding="utf-8") as fh:
            return jsonify(json.load(fh))
    return jsonify({})

@app.post("/api/data")
def save_data():
    with open(DB, "w", encoding="utf-8") as fh:
        json.dump(request.get_json(force=True), fh, ensure_ascii=False, indent=1)
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

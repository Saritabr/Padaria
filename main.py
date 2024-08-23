from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/getall', methods=['GET'])
def get_all_products():
    products = [
      {"nome": "Pão Francês", "descricao": "Descrição do produto 1", "preco": 1.99},
      {"nome": "Pão na chapa", "descricao": "Descrição do produto 2", "preco": 2.99},
      {"nome": "Pão de milho", "descricao": "Descrição do produto 3", "preco": 3.99},
      {"nome": "Pão Caseiro", "descricao": "Descrição do produto 4", "preco": 4.99},
      {"nome": "Pão de calabresa", "descricao": "Descrição do produto 5", "preco": 5.99},
      {"nome": "Pão Doce", "descricao": "Descrição do produto 6", "preco": 6.99},
      {"nome": "Suco de laranja", "descricao": "Descrição do produto 7", "preco": 7.99},
      {"nome": "Suco de morango", "descricao": "Descrição do produto 8", "preco": 8.99},
      {"nome": "Suco de maracujá", "descricao": "Descrição do produto 9", "preco": 9.99},
      {"nome": "Misto Quente", "descricao": "Descrição do produto 10", "preco": 1.99},
      {"nome": "Pastel", "descricao": "Descrição do produto 11", "preco": 11.99},
      {"nome": "Coxinha", "descricao": "Descrição do produto 12", "preco": 12.99}
       
    ]
    return jsonify(products)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)

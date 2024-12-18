from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    'dbname': 'a82451',    
    'user': 'a82451',     
    'password': 'a82451',   
    'host': '193.136.227.136',  
    'port': 8080               
}

@app.route('/api/arvores', methods=['POST'])
def add_tree():
    data = request.json
    print(data)
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = f"INSERT INTO Tb_Tree (nome, especie, altura, longitude, latitude) VALUES ('{data['nome']}', '{data['especie']}',{data['altura']}, {data['longitude']}, {data['latitude']})" #, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326)%((, data['especie'], data['altura'], data['longitude'], data['latitude']))
        print(query)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"data": {"message": "The tree has been sucessfuly added!", "tree": data}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/arvores', methods=['GET'])
def get_arvores():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_tree")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{"id": row[0], "nome": row[1], "especie": row[2], "altura": row[3], "longitude": row[4], "latitude": row[5]} for row in rows])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

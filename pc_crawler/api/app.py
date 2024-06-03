from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def query_db(query, args=(), one=False):
    con = sqlite3.connect('products.db')
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/computers', methods=['GET'])
def get_computers():
    processor = request.args.get('processor', '')
    gpu = request.args.get('gpu', '')
    motherboard = request.args.get('motherboard', '')
    ram = request.args.get('ram', '')

    query = 'SELECT * FROM products WHERE 1=1'
    params = []

    if processor:
        query += ' AND processor=?'
        params.append(processor)
    if gpu:
        query += ' AND gpu=?'
        params.append(gpu)
    if motherboard:
        query += ' AND motherboard=?'
        params.append(motherboard)
    if ram:
        query += ' AND ram=?'
        params.append(ram)

    products = query_db(query, params)
    return jsonify([dict(id=row[0], processor=row[1], gpu=row[2], motherboard=row[3], ram=row[4]) for row in products])


if __name__ == '__main__':
    app.run(debug=True)

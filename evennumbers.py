from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate_even_numbers/<int:n>')
def generate_even_numbers(n):
    numbers = [i for i in range(2, 2*n + 1, 2)]
    return jsonify(numbers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

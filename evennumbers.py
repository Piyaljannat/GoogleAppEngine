from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def generate_even_numbers(n):
    numbers = [i for i in range(2, 2*n + 1, 2)]
    return jsonify(numbers)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
    
    

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generateEvenNumbers', methods=['GET', 'POST'])
def generateEvenNumbers():
    #numbers = [i for i in range(2, 2*n + 1, 2)]
    #return jsonify(numbers)
    if request.method == 'POST':
        form_data = request.form
        return render_template('result.html',form_data = form_data)
 
    return render_template("form.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
    
    

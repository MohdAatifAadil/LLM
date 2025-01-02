from flask import Flask, request, jsonify
import sympy as sp

app = Flask(__name__)

def evaluate_math(expression):
    try:

        result = sp.sympify(expression)
        return result
    except Exception as e:
        return f"Error in expression: {str(e)}"

@app.route('/evaluate', methods=['GET'])
def evaluate():
    expression = request.args.get('expression')

    if not expression:
        return jsonify({"error": "No expression provided"}), 400


    result = evaluate_math(expression)

    return  jsonify({"expression": expression, "result": str(result)})

if __name__ == '__main__':
    app.run(debug=True)


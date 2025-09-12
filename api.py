from flask import Flask, render_template, redirect, url_for, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
# api = Api(app)
# GET -- what i want from the browser when visiting

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        answer = request.form.get('numbers')
        return redirect(url_for('calculate', calculator_input=answer))
    else:
        return render_template("index.html")

# PUT -- what i want to input to browser

@app.route('/calculate')
def calculate():
    calculator_input = request.args.get('calculator_input')
    try:
        final = eval(calculator_input)

    except Exception:
        final = "Please type numbers only."
    
    
    return render_template("result.html",final=final) 


if __name__ == "__main__":
    app.run(debug=True) 
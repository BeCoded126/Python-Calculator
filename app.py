# import statistics

# def return_distinct(x,y,z):
#     numbers = [x,y,z]
#     if (x+y+z) > 15:
#         return max(numbers)
#     elif (x+y+z) < 10:
#         return min(numbers)
#     elif (x+y+z) >= 10 or sum(x,y,z) <= 15:
#         return statistics.median(numbers)
    


# print(return_distinct(1,6,2))



# def function(name):
#     updated = sorted(name)

#     return updated

# print(function('california'))




# def function(*args):
#     for n in range(len(args)-1): 
#         if 0 == args[n] and 0 == args[n+1]:
#             return True
#     else:
#         return False

# print(function(4,0,0,2,0,4,2))



# def count_primes(*args):
#     numbers = []  # store primes here
    
#     for n in args:
#         if n > 1:  # primes are > 1
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     break
#             else:  # no divisors found = prime
#                 numbers.append(n)
    
#     if numbers:
#         print(f"There are {len(numbers)} prime numbers: {numbers}")
#     else:
#         print("No prime numbers")


# print(count_primes(391, 459, 4, 22, 23, 31))



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
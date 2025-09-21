from flask import Flask, redirect, url_for, render_template, request



app = Flask(__name__)

app.route('/', Method = ['GET','POST'])
def home():
    if request.method == 'POST':
       type_input = request.form.get('numbers')
       redirect('calculate', calculator_input=type_input)
    else:
        render_template('index_html')


app.route('/calculate', Method=['POST'])
def calculate():
    calculator_input = request.args.get("calculator_input")
    try:
        final =  eval(calculator_input)
        
    except Exception:
        final = "Please type numbers only"

    return render_template('result.html', final = final)



if __name__ == "__main__":
    app.run(debug=True)
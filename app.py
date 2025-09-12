#Calculator Logic
calculator_input = []

def calculate(calculator_input):
   
    try:
        calculator_input = eval(input('type here: '))

    except Exception as e:
        print (f"Please type numbers only: ")
        calculator_input = eval(input())
    

    answer = calculator_input 
    return answer


print(calculate(calculator_input))
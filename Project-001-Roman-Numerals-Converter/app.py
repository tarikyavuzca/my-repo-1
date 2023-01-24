from flask import Flask, render_template, request

app = Flask(__name__)

# convert function to convert decimal number to Roman numeral
def convert(decimal_num):
    # defining the number based on requirement
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    # assigning a variable to store result
    num_to_roman = ''
    # looping through the input number
    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i)
        decimal_num %= i
    return num_to_roman

# get request to render index.html
@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', developer_name='YTD', not_valid=False)

# post request to calculate the number and render the result page
@app.route('/', methods=['POST'])
def main_post():
    input1 = request.form['number']
    if not input1.isdecimal():
        return render_template('index.html', developer_name='YTD', not_valid=True)

    number = int(input1)
    if not 0 < number < 4000:
        return render_template('index.html', developer_name='YTD', not_valid=True)

    return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='YTD')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
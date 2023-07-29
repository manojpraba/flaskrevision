from flask import Flask, request,render_template,url_for,jsonify

app =Flask(__name__)

@app.route('/')
def welcome():
    return render_template('calculate.html')

@app.route('/cal',methods=['POST'])
def mathoperation():
    
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]

    if operation=="add":
        result =num1+num2
    elif operation =="multiply":
        result=num1*num2
    elif operation=="division":
        result=num1/num2
    else:
        result=num1-num2
    return jsonify (result)

@app.route('/calculate',methods=['POST'])
def mathoperation2():
   
    operation=str(request.form["operation"])
    num1=int(request.form["num1"])
    num2=int(request.form["num2"])

    if operation=="add":
        result =num1+num2
    elif operation =="multiply":
        result=num1*num2
    elif operation=="division":
        result=num1/num2
    else:
        result=num1-num2
    return render_template ('results.html',value=result)

if __name__ == '__main__':
    #app.run(ssl_context='adhoc')
    app.run(debug=True)
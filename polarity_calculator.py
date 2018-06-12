



from flask import Flask,render_template,request
from textblob import TextBlob
app = Flask(__name__)




@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/second',methods=["POST"])
def index():
    text=request.form['text']
    Rview = TextBlob(text)
    x = Rview.sentiment.polarity * 100
    if x>0:
        y = x * 2.5 - 125
    else:
        x=x*-1
        y = x * 2.5 - 125
        print(y)
        x=x*-1
    dict = {'review': x,'convert':y}
    print(x)

    return render_template('index2.html',result=dict)

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 5000)

from flask import Flask, render_template, request
from pythoncode import flipkart, ebay, croma, amazon, olx

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    name = request.form['name']
    flipkart_result = flipkart(name)
    ebay_result = ebay(name)
    croma_result = croma(name)
    amazon_result = amazon(name)
    olx_result = olx(name)
    return render_template('index.html', flipkart_result=flipkart_result, ebay_result=ebay_result, croma_result=croma_result, amazon_result=amazon_result, olx_result=olx_result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,render_template
from Spider import Spider
app = Flask(__name__)
spider=Spider()

@app.route('/')
def hello_world():
    return render_template('index.html',xiaohualist=spider.xiaohualist)

@app.route('/refresh')
def home():
    spider.refresh()
    return render_template('index.html',xiaohualist=spider.xiaohualist)

if __name__ == '__main__':
    app.run(debug=True)

#Hello,world

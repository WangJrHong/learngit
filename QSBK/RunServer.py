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


#第四次变更结果:我加了一行字
#第五次修改,我又加了一行字,并删除了world

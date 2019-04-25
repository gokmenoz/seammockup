from flask import Flask,render_template,request
   

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index_lulu():
    return render_template('tabs.html')

@app.route('/district101.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district101.html')

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

if __name__ == "__main__":
    app.debug=False
    app.run(host='0.0.0.0')

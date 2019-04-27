from flask import Flask,render_template,request
   

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index_lulu():
    return render_template('index.html')

@app.route('/tabs',methods=['GET','POST'])
def tabs_lulu():
    return render_template('tabs.html')
    

@app.route('/district101.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district101.html')

@app.route('/district102.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district102.html')

@app.route('/district103.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district103.html')
@app.route('/district104.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district104.html')
@app.route('/district105.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district105.html')
@app.route('/district106.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district106.html')
@app.route('/district107.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district107.html')
@app.route('/district108.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district108.html')
@app.route('/district109.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district109.html')
@app.route('/district110.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district110.html')
@app.route('/district111.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district111.html')
@app.route('/district112.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district112.html')
@app.route('/district201.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district201.html')
@app.route('/district202.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district202.html')
@app.route('/district203.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district203.html')
@app.route('/district204.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district204.html')
@app.route('/district205.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district205.html')
@app.route('/district206.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district206.html')
@app.route('/district207.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district207.html')
@app.route('/district208.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district208.html')
@app.route('/district209.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district209.html')
@app.route('/district210.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district210.html')
@app.route('/district211.html',methods=['GET','POST'])
def dist_lulu():
    return render_template('district211.html')





@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

if __name__ == "__main__":
    app.run(debug=False)

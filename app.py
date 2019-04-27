from flask import Flask,render_template,request
   

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index_lulu():
    return render_template('index.html')

@app.route('/tabs',methods=['GET','POST'])
def tabs_lulu():
    return render_template('tabs.html')
    

@app.route('/district101.html',methods=['GET','POST'])
def dist_lulu_101():
    return render_template('district101.html')

@app.route('/district102.html',methods=['GET','POST'])
def dist_lulu_102():
    return render_template('district102.html')

@app.route('/district103.html',methods=['GET','POST'])
def dist_lulu_103():
    return render_template('district103.html')
@app.route('/district104.html',methods=['GET','POST'])
def dist_lulu_104():
    return render_template('district104.html')
@app.route('/district105.html',methods=['GET','POST'])
def dist_lulu_105():
    return render_template('district105.html')
@app.route('/district106.html',methods=['GET','POST'])
def dist_lulu_106():
    return render_template('district106.html')
@app.route('/district107.html',methods=['GET','POST'])
def dist_lulu_107():
    return render_template('district107.html')
@app.route('/district108.html',methods=['GET','POST'])
def dist_lulu_108():
    return render_template('district108.html')
@app.route('/district109.html',methods=['GET','POST'])
def dist_lulu_109():
    return render_template('district109.html')
@app.route('/district110.html',methods=['GET','POST'])
def dist_lulu_110():
    return render_template('district110.html')
@app.route('/district111.html',methods=['GET','POST'])
def dist_lulu_111():
    return render_template('district111.html')
@app.route('/district112.html',methods=['GET','POST'])
def dist_lulu_112():
    return render_template('district112.html')
@app.route('/district201.html',methods=['GET','POST'])
def dist_lulu_201():
    return render_template('district201.html')
@app.route('/district202.html',methods=['GET','POST'])
def dist_lulu_202():
    return render_template('district202.html')
@app.route('/district203.html',methods=['GET','POST'])
def dist_lulu_203():
    return render_template('district203.html')
@app.route('/district204.html',methods=['GET','POST'])
def dist_lulu_204():
    return render_template('district204.html')
@app.route('/district205.html',methods=['GET','POST'])
def dist_lulu_205():
    return render_template('district205.html')
@app.route('/district206.html',methods=['GET','POST'])
def dist_lulu_206():
    return render_template('district206.html')
@app.route('/district207.html',methods=['GET','POST'])
def dist_lulu_207():
    return render_template('district207.html')
@app.route('/district208.html',methods=['GET','POST'])
def dist_lulu_208():
    return render_template('district208.html')
@app.route('/district209.html',methods=['GET','POST'])
def dist_lulu_209():
    return render_template('district209.html')
@app.route('/district210.html',methods=['GET','POST'])
def dist_lulu_210():
    return render_template('district210.html')
@app.route('/district211.html',methods=['GET','POST'])
def dist_lulu_211():
    return render_template('district211.html')
@app.route('/district301.html',methods=['GET','POST'])
def dist_lulu_301():
    return render_template('district301.html')
@app.route('/district302.html',methods=['GET','POST'])
def dist_lulu_302():
    return render_template('district302.html')
@app.route('/district303.html',methods=['GET','POST'])
def dist_lulu_303():
    return render_template('district303.html')
@app.route('/district307.html',methods=['GET','POST'])
def dist_lulu_307():
    return render_template('district307.html')
@app.route('/district308.html',methods=['GET','POST'])
def dist_lulu_308():
    return render_template('district308.html')
@app.route('/district309.html',methods=['GET','POST'])
def dist_lulu_309():
    return render_template('district309.html')
@app.route('/district310.html',methods=['GET','POST'])
def dist_lulu_310():
    return render_template('district310.html')
@app.route('/district311.html',methods=['GET','POST'])
def dist_lulu_311():
    return render_template('district311.html')
@app.route('/district312.html',methods=['GET','POST'])
def dist_lulu_312():
    return render_template('district312.html')
@app.route('/district313.html',methods=['GET','POST'])
def dist_lulu_313():
    return render_template('district313.html')
@app.route('/district314.html',methods=['GET','POST'])
def dist_lulu_314():
    return render_template('district314.html')
@app.route('/district315.html',methods=['GET','POST'])
def dist_lulu_315():
    return render_template('district315.html')
@app.route('/district316.html',methods=['GET','POST'])
def dist_lulu_316():
    return render_template('district316.html')
@app.route('/district317.html',methods=['GET','POST'])
def dist_lulu_317():
    return render_template('district317.html')
@app.route('/district318.html',methods=['GET','POST'])
def dist_lulu_318():
    return render_template('district318.html')
@app.route('/district401.html',methods=['GET','POST'])
def dist_lulu_401():
    return render_template('district401.html')
@app.route('/district402.html',methods=['GET','POST'])
def dist_lulu_402():
    return render_template('district402.html')
@app.route('/district403.html',methods=['GET','POST'])
def dist_lulu_403():
    return render_template('district403.html')
@app.route('/district404.html',methods=['GET','POST'])
def dist_lulu_404():
    return render_template('district404.html')
@app.route('/district405.html',methods=['GET','POST'])
def dist_lulu_405():
    return render_template('district405.html')
@app.route('/district406.html',methods=['GET','POST'])
def dist_lulu_406():
    return render_template('district406.html')
@app.route('/district407.html',methods=['GET','POST'])
def dist_lulu_407():
    return render_template('district407.html')
@app.route('/district408.html',methods=['GET','POST'])
def dist_lulu_408():
    return render_template('district408.html')
@app.route('/district409.html',methods=['GET','POST'])
def dist_lulu_409():
    return render_template('district409.html')
@app.route('/district410.html',methods=['GET','POST'])
def dist_lulu_410():
    return render_template('district410.html')
@app.route('/district411.html',methods=['GET','POST'])
def dist_lulu_411():
    return render_template('district411.html')
@app.route('/district412.html',methods=['GET','POST'])
def dist_lulu_412():
    return render_template('district412.html')
@app.route('/district413.html',methods=['GET','POST'])
def dist_lulu_413():
    return render_template('district413.html')
@app.route('/district414.html',methods=['GET','POST'])
def dist_lulu_414():
    return render_template('district414.html')
@app.route('/district501.html',methods=['GET','POST'])
def dist_lulu_501():
    return render_template('district501.html')
@app.route('/district502.html',methods=['GET','POST'])
def dist_lulu_502():
    return render_template('district502.html')
@app.route('/district503.html',methods=['GET','POST'])
def dist_lulu_503():
    return render_template('district503.html')






@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

if __name__ == "__main__":
    app.run(debug=False)

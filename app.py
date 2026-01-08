from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

#{{url_for()

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db= SQLAlchemy(app)

class Bill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    month=db.Column(db.String(100),nullable=False)
    pre=db.Column(db.Integer,nullable=False)
    pre2=db.Column(db.Integer,nullable=False)
    pre3=db.Column(db.Integer,nullable=False,default=0)
    cur=db.Column(db.Integer,nullable=False)
    cur2=db.Column(db.Integer,nullable=False)
    cur3=db.Column(db.Integer,nullable=False,default=0)
    diff=db.Column(db.Integer,nullable=False)
    diff2=db.Column(db.Integer,nullable=False)
    diff3=db.Column(db.Integer,nullable=False,default=0)
    am=db.Column(db.Integer,nullable=False)
    am2=db.Column(db.Integer,nullable=False)
    am3=db.Column(db.Integer,nullable=False)
    am4=db.Column(db.Integer,nullable=False,default=0)
    total=db.Column(db.Integer,nullable=False)
    remark1=db.Column(db.String(500),nullable=True)
    remark2=db.Column(db.String(500),nullable=True)
    remark3=db.Column(db.String(500),nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Task {self.id}"
        
    

@app.route("/", methods=["POST","GET"])
def index():
    #for now only add 
    if request.method=='POST':
        name=request.form['name']
        month=request.form.get('month')
        pre=request.form['pre']
        pre2=request.form['pre2']
        pre3=request.form['pre3']
        cur=request.form['cur']
        cur2=request.form['cur2']
        cur3=request.form['cur3']
        diff=int(pre)-int(cur)
        diff2=int(pre2)-int(cur3)
        diff3=int(pre2)-int(cur3)
        # diff2=request.form['diff2']
        # diff3=request.form['diff3']
        # am=request.form['am']
        # am2=request.form['am2']
        # am3=request.form['am3']
        am4=request.form['am4']
        am=int(diff)*10
        am2=int(diff2)*10
        am3=int(diff3)*10
        total=int(am)+int(am2)+int(am3)+int(am3)
        # total=request.form['total']
        remark1=request.form['rem']
        remark2=request.form['rem2']
        remark3=request.form['rem3']
        new_bill=Bill(name=name,month=month,pre=pre,pre2=pre2,pre3=pre3,cur=cur,cur2=cur2,cur3=cur3,diff=diff,diff2=diff2,diff3=diff3,am=am,am2=am2,am3=am3,am4=am4,total=total,remark1=remark1,remark2=remark2,remark3=remark3)
        
        try:
            db.session.add(new_bill)
            db.session.commit()
            # savetoexcel()
            return redirect("/")
        except Exception as e:
            print(f"ERORR:{e}")
            return f"ERORR:{e}"
    
    else:    
        return render_template('index.html')
    

# def savetoexcel():
#     url="templates\index.html"
#     table=pd.read_html(url)[0]
#     table.to_excel("data.xlsx")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
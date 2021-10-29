from .utility import sendSMS
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Update, User
from . import db
import time, requests
from .uidaiAdapter import ekycAddr, ekycName,genUidaiOtp


views = Blueprint('views',__name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@views.route('/gen_vid', methods=['GET','POST'])
def genVid():
    if(request.method == 'POST'):
        URL = "https://stage1.uidai.gov.in/vidwrapper/generate"
        response = requests.post(URL, json=request.form)
        return response.json()
    return render_template('genvid.html')

@views.route('/get_vid', methods=['GET','POST'])
def getVid():
    if(request.method == 'POST'):
        URL = "https://stage1.uidai.gov.in/vidwrapper/retrieve"
        response = requests.post(URL, json=request.form)
        return response.json()
    return render_template('getvid.html')

@views.route('/approve_addr/<int:id>', methods=['GET','POST'])
def approveAddr(id:int):
    update = Update.query.get(id)
    if not update:
        flash("Update id not found.", category='error')
        return redirect(url_for('views.approveAddrRender'))
    if update.open == False and update.lapproved==False: 
        flash(f"Dear, {update.name} the update request is rejected by landlord.", category='error')
        flash(f"Reason : {update.status}", category='error')
        return redirect(url_for('views.approveAddrRender'))
    if update.open == False:
        flash(f"Dear, {update.name} the update request is approved by landlord.", category='success')
        return redirect(url_for('views.approveAddrRender'))

    if request.method == 'POST':
        if request.form.get('uvid') != str(update.luvid):
            print(request.form.get('uvid'))
            print(str(update.luvid))
            print(request.form.get('uvid').strip() == str(update.luvid).strip())
            return {'result':'n','txnId':'','err':'UID mismatch'}
        elif request.form.get('type') == '1':
            res = genUidaiOtp(request.form.get('uvid'))
            if res['result'] == 'n':
                return res
            res['address'] = update.new_address
            return res
        elif request.form.get('type') == '2':
            uvid = request.form.get('uvid')
            txnId = request.form.get('txnId')
            otp = request.form.get('otp')
            res = ekycAddr(uvid,txnId,otp)
            if(res['status'] == 'n'):
                return "fail"
            
            if request.form.get('perm') == 'n':
                update.uvid =  generate_password_hash(str(update.uvid), method='sha256')
                update.luvid =  generate_password_hash(str(update.luvid), method='sha256')
                update.lmo = ''
                update.lapproved = False
                update.open = False
                update.status = request.form.get('status')
                db.session.commit()
                return "success"
            else:
                update.lapproved = True
                update.open = False
                update.laddress = res['address']
                db.session.commit()
                return "success"
    uid = str(update.uvid)
    luid = str(update.luvid)
    return render_template('approveaddr.html',name=update.name,uid= 'X'*(len(uid)-4) + uid[-4:], luid= 'X'*(len(luid)-4) + luid[-4:])

@views.route('/approve_addr', methods=['GET'])
def approveAddrRender():
    return render_template('approveaddr1.html')



@views.route('/update_addr', methods=['GET','POST'])
def updateAddr():
    if(request.method == 'POST'):
        if(request.form.get('type') == '2'):
            uvid = request.form.get('uvid')
            txnId = request.form.get('txnId')
            otp = request.form.get('otp')
            res = ekycName(uvid,txnId,otp)
            if(res['status'] == 'n'):
                return {'result':'n', 'err':'Invalid otp'}
            new_user = User(uvid=uvid, name=res['name'], txnId=txnId, otp=otp)
            db.session.add(new_user)
            db.session.commit()
            return {'result':'y', 'err':'null'}
        elif(request.form.get('type') == '3'):
            # print(request.form)
            uvid = str(request.form.get('uvid'))
            # print(uvid)
            txnId = request.form.get('txnId')
            otp = str(request.form.get('otp'))
            user = User.query.filter_by(uvid=uvid).first()
            if user:
                if str(user.uvid)== uvid and str(user.otp)==otp and user.txnId == txnId and int(time.time())<= (user.time+ 20*60):
                    new_update = Update(name=user.name, uvid=uvid,luvid=request.form.get('luvid') , lmo=request.form.get('lmo') ,new_address= request.form.get('address'))
                    msg = f"{user.name} has requested for address verification. Click on the link https://calculators.ml/approve_addr/"
                    db.session.add(new_update)
                    db.session.delete(user)
                    db.session.commit()
                    msg += f"{new_update.id} for approving or rejecting address update."
                    try:
                        sendSMS(request.form.get('lmo'),msg)
                    except:
                        pass
                    finally:
                        pass
                    flash("Update request submited.", category='success')
                    flash(f'Your update request id is "{new_update.id}". Save it for future use.', category='success')
                    flash(f'Sms notification to landlord has been sent .', category='success')
                    return redirect(url_for('views.approveAddrRender'))
                else:
                    user = User.query.filter_by(uvid=uvid).delete()
                    
                    db.session.commit()
                    flash("Request timeout. Try again", category='error')
                    return redirect(url_for('views.updateAddr'))
            else:
                flash("Invalid request.", category='error')
                return redirect(url_for('views.home'))
       
    return render_template('updateaddr.html')


@views.route('/status', methods=['GET'])
def statusRender():
    return render_template('status1.html')

@views.route('/status/<int:id>', methods=['GET','POST'])
def status(id:int):
    update = Update.query.get(id)
    if not update:
        return redirect(url_for('views.statusRender'))
    if request.method == 'POST':
        uid = str(request.form.get('uid'))
        if str(update.uvid) == uid or check_password_hash(str(update.uvid), uid):
            return {'result':'y', 'err':'','open':update.open,'lapproved':update.lapproved, 'name':update.name ,'status':update.status}
        else:
            return {'result':'n', 'err':'invalid UID','status':''}
    return render_template('status.html',id=id)

@views.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')


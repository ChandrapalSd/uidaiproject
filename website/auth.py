from flask import Blueprint, json, request, Response
import requests
from .uidaiAdapter import genUidaiOtp

auth = Blueprint('auth',__name__)

@auth.route('/send_otp',methods=['POST'])
def sendOtp():
    return genUidaiOtp(request.form.get('uvid'))

@auth.route('/gen_vid_otp',methods=['POST'])
def genVidOtp():
    URL = "https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/generate/aadhaar/otp"
    response = requests.post(URL, json=request.form)
    return response.json()

@auth.route('/get_vid_captcha',methods=['POST'])
def getVidCaptcha():
    URL = "https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/get/captcha"
    body = {
            "langCode": "en",
            "captchaLength": "3",
            "captchaType": "2"
            }
    response = requests.post(URL, json=body)

    if response.status_code != 200:
        return Response({}, status=404, mimetype='application/json')

    data = response.json()
    r = {
        "txnId" : data.get('captchaTxnId'),
        "captchaString" : data.get('captchaBase64String')
        }
    return json.jsonify(r)

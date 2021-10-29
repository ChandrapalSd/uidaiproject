const image = document.getElementById('captcha-img');
const txnId = document.getElementById('txn-id');
const btn = document.getElementById("submit-btn");
const uid = document.getElementById('uid');
const captcha = document.getElementById('captcha');
const otp = document.getElementById('otp');
const mobile = document.getElementById('mobile');
var state = 1;
var otpTxnId;


function loadCaptcha(){

    const xhr = new XMLHttpRequest();
    xhr.open("POST","get_vid_captcha",true);
    xhr.responseType = 'json'

    xhr.onload = function() {
        if(xhr.status === 200){
            image.src = `data:image/png;base64,${xhr.response.captchaString}`;
            txnId.value = xhr.response.txnId;
        }
        else{
            console.log("Error.....,");
        }
    };

    xhr.send();
}



window.onload = loadCaptcha;
image.addEventListener("click",()=>{
    image.src = '';
    loadCaptcha();
});

btn.addEventListener('click', function(){
    if (!validateInput(uid,'Aadhar no.') || !validateInput(captcha,'captcha')) {
        return;
    }
    // send otp request
    if (state == 1) {

        const xhr = new XMLHttpRequest();
        xhr.open("POST","gen_vid_otp",true);
        xhr.responseType = 'json';
    
        xhr.onload = function() {
            if(xhr.status === 200){
                if(xhr.response.status === 'Success' ){
                    otp.hidden = false;
                    document.getElementById('otplabel').hidden = false;
                    mobile.hidden = false;
                    document.getElementById('mobilelabel').hidden = false;
                    otpTxnId = xhr.response.txnId;
                    state = 2;
                }
                else{
                    alert(xhr.response.message);
                }
            }
            else{
                alert("Error. Unable to connect server.");
            }
        };
    
        let FD = new FormData();
        FD.append('uidNumber', uid.value);
        FD.append('captchaTxnId', txnId.value);
        FD.append('captchaValue', captcha.value);
        FD.append('transactionId', `$MYAADHAAR:{crypto.randomUUID()}`);
    
        xhr.send(FD);
    
    }
    // Send otp for verification
    else if(state == 2){
        if (!validateInput(mobile,'mobile no.') || !validateInput(otp,'otp')) {
            return;
        }
        const xhr = new XMLHttpRequest();
        xhr.open("POST","get_vid",true);
        xhr.responseType = 'json';
    
        xhr.onload = function() {
            if(xhr.status === 200){
                if(xhr.response.status === 'Success' ){
                    alert(`Your VID is ${xhr.response.vid}`);
                    document.getElementById('vid-display').innerText = `Your VID is ${xhr.response.vid}`;
                    otp.hidden = true;
                    document.getElementById('otplabel').hidden = true;
                    mobile.hidden = true;
                    document.getElementById('mobilelabel').hidden = true;
                    state = 1;
                    image.src = '';
                    loadCaptcha();
                }
                else{
                    alert(xhr.response.message);
                }
            }
            else{
                alert("Error. Unable to connect server.");
            }
        };
    
        let FD = new FormData();
        FD.append('uid', uid.value);
        FD.append('mobile', mobile.value);
        FD.append('otp', otp.value);
        FD.append('otpTxnId', otpTxnId);
    
        xhr.send(FD);
    }

  
});

function validateInput(inputE, text = ''){
    var regex = new RegExp(inputE.pattern);
    let res = regex.test(inputE.value);
    if (res) {
        return true;
    }
    if (text.length >0) {
        alert(`Enter valid data in ${text} * field.`);
    }
    else{
        alert(`Enter valid data in Required * fields.`);
    }
    return false;
}
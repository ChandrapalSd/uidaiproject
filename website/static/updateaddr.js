var submitBtn = document.getElementById("submit-btn");
var uvid = document.getElementById("uvid");
var otp = document.getElementById("otp");
var otplabel = document.getElementById("otplabel");
var luvid = document.getElementById("luvid");
var luvidlabel = document.getElementById("luvidlabel");
var lmo = document.getElementById("lmo");
var lmolabel = document.getElementById("lmolabel");
var address = document.getElementById("address");
var addresslabel = document.getElementById("addresslabel");
var message = document.getElementById('message-div');
var txnID = document.getElementById('txnId');
// Type 1: send otp ; Type 2: Send/verify Otp value
var requestType = document.getElementById('type');

document.getElementById('submit-btn').addEventListener("click",function(e) {
    
    // Send data . [Otp already verified]
    if (requestType.value == '3') {
        return;
    }
    // Send request for send otp to mobile
    else if (requestType.value == '1') {
        e.preventDefault();
        if(!validateInput(uvid)){
            return;
        }
        if(!document.getElementById("ekycPerm").checked){
            alert("EKyc permission is required");
            return;
        }
        document.getElementById("ekycPerm").disabled = true;
        message.innerHTML = "<p>Please wait. Sending Otp....</p>";

        var xhr = new XMLHttpRequest();

        xhr.open('POST',"/send_otp",true);
        xhr.responseType = 'json';

        xhr.onload = function(){
            if(xhr.status === 200){
                r = xhr.response;
                if (r.result == 'n') {
                    message.innerHTML = `<p class="text-danger">Error . Please check the aadhar number</p>`;
                    return;
                }

                message.innerHTML = `<p class="text-success">Otp Sent to mobile. Please enter the Otp</p>`;
                requestType.value = '2';
                otp.hidden = false;
                otp.required = true;
                otplabel.hidden = false;
                txnID.value = r.txnId;
                submitBtn.innerText = "Verify Otp";
                uvid.readOnly = true;
            }
            else{
                message.innerHTML = `<p class="text-danger">Error : can't connect to server . Check your connection</p>`;
            }
        }
        let FD  = new FormData();
        FD.append('uvid',uvid.value);
        xhr.send(FD);
    }
    // Send otp for verification 
    // TODO Incomplete , will complete after getting staging uid
    else if (requestType.value == '2') {
        e.preventDefault();
        if(!validateInput(otp)){
            return;
        }
        message.innerHTML = "<p>Please wait. Checking Otp....</p>";

        var xhr = new XMLHttpRequest();

        xhr.open('POST',"/update_addr",true);
        xhr.responseType = 'json';

        xhr.onload = function(){

            if(xhr.status === 200){
                r = xhr.response

                if(r.result == 'n'){
                    message.innerHTML = `<p class="text-danger">Error . OTP verification failed</p>`;
                    return;
                }

                message.innerHTML = `<p class="text-success">Otp verification Successfull.</p>`;
                requestType.value = '3'
                otp.hidden = true;
                otplabel.hidden = true;
                luvid.hidden = false;
                luvid.required = true;
                luvidlabel.hidden = false;
                lmo.hidden = false;
                lmo.required = true;
                lmolabel.hidden = false;
                address.hidden = false;
                address.required = true;
                addresslabel.hidden = false;
                submitBtn.innerText = "Submit"

                document.getElementById('address-hint').hidden = false;
            }
            else{
                message.innerHTML = `<p class="text-danger">Error : can't connect to server . Check your connection</p>`;
            }
                

        }

        let FD  = new FormData();
        FD.append('uvid',uvid.value);
        FD.append('txnId', txnID.value);
        FD.append('otp', otp.value);
        FD.append('type', requestType.value);
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
var requestType = document.getElementById('type');
var submitBtn = document.getElementById('submit-btn');
var uvid = document.getElementById('uvid');
var otp = document.getElementById('otp');
var otplabel = document.getElementById('otplabel');
var message = document.getElementById('message-div');
var txnID = document.getElementById('txnId');
var approve_div = document.getElementById('approve-div');
var Status = document.getElementById('status');

submitBtn.addEventListener('click',function(e){
    if (requestType.value == '1'){
        e.preventDefault();
        if(!document.getElementById("ekycPerm").checked){
            alert("EKyc permission is required");
            return;
        }
        if (validateInput(uvid.value,"UID")) {
            
        }
        document.getElementById("ekycPerm").disabled = true;
        message.innerHTML = "<p>Please wait. Sending Otp....</p>";

        var xhr = new XMLHttpRequest();

        xhr.open('POST',window.location.href,true);
        xhr.responseType = 'json';

        xhr.onload = function(){

            if(xhr.status === 200){
                r = xhr.response;
                if (r.result == 'n') {
                    message.innerHTML = `<p class="text-danger">Error . Please check the aadhar number</p>`;
                    alert(r.err)
                    return;
                }
                message.innerHTML = `<p class="text-success">Otp Sent to mobile. Please enter the Otp</p>`;
                requestType.value = '2';
                document.getElementById("new_address").innerText = xhr.response.address;
                otp.hidden = false;
                otp.required = true;
                otplabel.hidden = false;
                txnID.value = r.txnId;
                submitBtn.innerText = "Verify Otp";
                uvid.readOnly = true;
                approve_div.hidden = false;
            }
            else{
                message.innerHTML = `<p class="text-danger">Error : can't connect to server . Check your connection</p>`;
            }

        }

        let FD  = new FormData();
        FD.append('uvid',uvid.value);
        FD.append('type',1);
        xhr.send(FD);
        
    }
    else if (requestType.value == '2'){
        e.preventDefault();
        if(!validateInput(otp,"OTP")){
            return;
        }
        let yes = document.getElementById('yes');
        let no = document.getElementById('no');
        if(!yes.checked && !no.checked){
            alert("Accept or reject approval");
            return;
        }
        if (no.checked) {
            var regex = new RegExp(Status.pattern);
            let res = regex.test(Status.value);
            if (!res) {
                alert("Please give reason for rejection in more than 10 words.")
                return;
            }
        }
        message.innerHTML = "<p>Please wait. Verifying otp....</p>";

        var xhr = new XMLHttpRequest();

        xhr.open('POST',window.location.href,true);
        xhr.responseType = 'text';

        xhr.onload = function(){
            if (xhr.status === 200) {
                if(xhr.response == 'success'){
                    let message = "You have successfully "+( yes.checked ? 'approved' : 'rejected' ) + " the address update request";
                    alert(message);
                    window.location.href = "/";
                }
                else{
                    alert("OTP verification failed");
                    message.innerHTML = `<p class="text-danger">Error . OTP verification failed</p>`;
                }
            }
            else{
                message.innerHTML = `<p class="text-danger">Error : can't connect to server . Check your connection</p>`;
            }
        }

        let FD  = new FormData();
        FD.append('uvid',uvid.value);
        FD.append('txnId',txnID.value);
        FD.append('otp',otp.value);
        FD.append('type',type.value);
        FD.append('status', Status.value);
        FD.append('perm', yes.checked ? 'y' : 'n');
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
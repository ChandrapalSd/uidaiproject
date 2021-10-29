var submitBtn = document.getElementById('submitBtn');
var regex = new RegExp("^([0-9]{12}|[0-9]{16})$" );
var uid = document.getElementById('uid');
var disp = document.getElementById('data-display');

submitBtn.addEventListener('click', function(e){
    e.preventDefault();
    let res = regex.test(uid.value);
    if (!res) {
        alert('Enter valid UID or VID');
        return ;
    }

    var xhr = new XMLHttpRequest();
    uid.readOnly = true;
    submitBtn.readOnly = true;

    xhr.open('POST',window.location.href,true);
    xhr.responseType = 'json';

    xhr.onload = function(){
        if(xhr.status === 200){
            r = xhr.response;
            if (r.result == 'y') {
                document.getElementById('form-div').hidden = true;

                let id = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
                document.getElementById('form-div').remove();

                if(r.open){
                    document.getElementById('disp2').remove();
                    document.getElementById('disp3').remove();
                    document.getElementById('disp1').hidden = false;

                    document.getElementById('name').innerText = r.name;


                }
                else if(r.lapproved){
                    document.getElementById('disp1').remove();
                    document.getElementById('disp2').remove();
                    document.getElementById('disp3').hidden = false;

                    document.getElementById('name').innerText = r.name;
                }
                else{
                    document.getElementById('disp3').remove();
                    document.getElementById('disp1').remove();
                    document.getElementById('disp2').hidden = false;
                    
                    document.getElementById('name').innerText = r.name;
                    document.getElementById('reason').innerText = r.status;
                }
                
            }
            else{
                alert("UID didn't match");
                uid.readOnly = false;
                submitBtn.readOnly = false;
            }
        }
        else{
            alert("can't connect to server . Check your connection");
            uid.readOnly = false;
            submitBtn.readOnly = false;
        }
    }

    let FD  = new FormData();
    FD.append('uid',uid.value);
    xhr.send(FD);
});

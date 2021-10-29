var regex = new RegExp("^[0-9]*$");
var Id = document.getElementById('Id');
document.getElementById('submit').addEventListener('click', function(e){
    e.preventDefault();
    let id = Id.value;
    let res = regex.test(id);
    if (id && id!=0 && res) {
        window.location.href =  `/approve_addr/${id}`;

    }
    else{
        alert(`Id must be integer and greater than 0`);
    }
});

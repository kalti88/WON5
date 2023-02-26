function valid_user() {
    let x = document.forms["sign_in_form"]["name"].value;
    if (x == "") {
        alert(" Username must be filled out");
        return false;
    }
    else {
        if (x.length < 4) {
             alert (" Username must be at least 4 characters.");
             return false;
        }
        else {
            if  (x.length > 10) {
                alert (" Username must be less then 10 characters.");
                return false;
            }
        }
    }
    return true;
}

function valid_text() {
    let x = document.forms["sign_in_form"]["text"].value;
    if (x == "") {
        alert(" Text must be filled out");
        return false;
    }
    return true;
}


function valid_check() {
    if (document.forms["sign_in_form"]["check"].checked == false) {
        alert("Please agree to all the terms and conditions before create an account.");
        return false;
    }
    return true;
}

function validation() {
    let controll=true;
    if (!valid_user()) {
        controll=false;
    };
    if (!valid_text()) {
        controll=false;
    };
    if (!valid_check()) {
        controll=false;
    };
    if (controll==true) {
        return true
    } else {
        return false
    }
}


function valid_user() {
    let x = document.forms["sign_in_form"]["name"].value;
    const elem = document.getElementById('answer_user')
    if (x == "") {
        elem.innerHTML =" Username must be filled out";
        return false;
    }
    else {
        if (x.length < 4) {
             elem.innerHTML =" Username must be at least 4 characters.";
             return false;
        }
        else {
            if  (x.length > 10) {
                elem.innerHTML =" Username must be less then 10 characters.";
                return false;
            } else {
                elem.innerHTML ="";
            }
        }
    }
    return true;
}

function valid_password() {
    let x = document.forms["sign_in_form"]["pass"].value;
    const elem2 = document.getElementById('answer_pass')
    if (x == "") {
        elem2.innerHTML =" Password must be filled out";
        return false;
    }
    else {
        if (x.length < 8) {
             elem2.innerHTML =" Password must be at least 8 characters.";
             return false;
        }
        else {
            if  (x.length > 20) {
                elem2.innerHTML ="Password must be less then 20 characters.";
                return false;
            }else {
                elem2.innerHTML ="";
            }
        }
    }
    return true;
}

function valid_repeat_pass() {
    let x = document.forms["sign_in_form"]["pass"].value;
    let y = document.forms["sign_in_form"]["pass_repeat"].value;
    const elem3 = document.getElementById('answer_pass_repeat');
    if (y != x) {
        elem3.innerHTML ="<span class='color-red'>* The password confirmation does not match.";
        return false;
    }else {
        elem3.innerHTML ="";
    }
    return true;
}

function valid_check() {
    const elem4 = document.getElementById('answer_check');
    if (document.forms["sign_in_form"]["check"].checked == false) {
        elem4.innerHTML ="<span class='color-red'>* Please agree to all the terms and conditions before create an account.";
        return false;
    } else {
        elem4.innerHTML ="";
    }
    return true;
}

function validation() {
    let controll=true;
    if (!valid_user()) {
        controll=false;
    };
    if (!valid_password()) {
        controll=false;
    };
    if (!valid_repeat_pass()) {
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


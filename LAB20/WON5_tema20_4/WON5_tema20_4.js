function valid_user() {
    let x = document.forms["sign_in_form"]["name"].value;
    if (x == "") {
        document.getElementById('answer_user').innerHTML ="<span class='color-red'>* Username must be filled out";
        return false;
    }
    else {
        if (x.length < 4) {
             document.getElementById('answer_user').innerHTML ="<span class='color-red'>* Username must be at least 4 characters.";
             return false;
        }
        else {
            if  (x.length > 10) {
                document.getElementById('answer_user').innerHTML ="<span class='color-red'>* Username must be less then 10 characters.";
                return false;
            }
        }
    }
}

function valid_password() {
    let x = document.forms["sign_in_form"]["pass"].value;
    if (x == "") {
        document.getElementById('answer_pass').innerHTML ="<span class='color-red'>* Password must be filled out";
        return false;
    }
    else {
        if (x.length < 8) {
             document.getElementById('answer_pass').innerHTML ="<span class='color-red'>* Password must be at least 8 characters.";
             return false;
        }
        else {
            if  (x.length > 20) {
                document.getElementById('answer_pass').innerHTML ="<span class='color-red'>* Password must be less then 20 characters.";
                return false;
            }
        }
    }
}

function valid_repeat_pass() {
    let x = document.forms["sign_in_form"]["pass"].value;
    let y = document.forms["sign_in_form"]["pass_repeat"].value;
    if (y != x) {
        document.getElementById('answer_pass_repeat').innerHTML ="<span class='color-red'>* The password confirmation does not match.";
        return false;
    }
}

function valid_check() {
    if (document.forms["sign_in_form"]["check"].checked == false) {
        document.getElementById('answer_check').innerHTML ="<span class='color-red'>* Please agree to all the terms and conditions before create an account.";
    }
}

function validation() {
    valid_user();
    valid_password();
    valid_repeat_pass();
    valid_check();
}


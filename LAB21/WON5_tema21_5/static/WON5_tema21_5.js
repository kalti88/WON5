function valid_user() {
    let x = document.forms["sign_in_form"]["name"].value;
    if (x == "") {
        alert("  Numele trebuie completat");
        return false;
    }
    else {
        if (x.length < 4) {
             alert (" Numele trebuie sa aiba minimum 4 caractere");
             return false;
        }
        else {
            if  (x.length > 20) {
                alert (" Numele trebuie sa aiba maximum 20 caractere");
                return false;
            }
        }
    }
    return true;
}

function valid_text() {
    let x = document.forms["sign_in_form"]["text"].value;
    if (x == "") {
        alert(" Scrie mesajul tau!");
        return false;
    }
    return true;
}


function valid_check() {
    if (document.forms["sign_in_form"]["check"].checked == false) {
        alert("Trebuie sa accepti termenii si conditiile de utilizare");
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


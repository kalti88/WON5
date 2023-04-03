function ValidateEmail(input) {
    if (input.includes("@", ".")) {
        return true;
    } else {
        return false;
    }
}

function valid_supplier() {
    let x = document.forms["supp_form"]["supplier"].value;
    const elem = document.getElementById('answer_supplier');
    if (x == "") {
        elem.innerHTML = "Numele furnizorului trebuie completat";
        return false;
    }
    else {
        elem.innerHTML = "";
    }
    return true;
}

function valid_address() {
    let x = document.forms["supp_form"]["address"].value;
    const elem = document.getElementById('answer_address')
    if (x == "") {
        elem.innerHTML = " Adresa furnizorului trebuie completata";
        return false;
    }
    else {
        elem.innerHTML = "";
    }
    return true;
}

function valid_email() {
    let x = document.forms["supp_form"]["email"].value;
    const elem = document.getElementById('answer_email')
    if (x == "") {
        elem.innerHTML = " Adresa de e-mail a furnizorului trebuie completata";
        return false;
        }
        else {
            if (ValidateEmail(x)) {
            elem.innerHTML = "";
            return true
            } else {
            elem.innerHTML = "Adresa de e-mail introdusa nu este valida!"
            return false
            }
        }
}

function valid_phone() {
    let x = document.forms["supp_form"]["phone"].value;
    const elem = document.getElementById('answer_phone')
    if (x == "") {
        elem.innerHTML = " Numarul de telefon al furnizorului trebuie completat";
        return false;
    }
    else {
        elem.innerHTML = "";
    }
    return true;
}

function validation() {
    let controll=true;
    if (!valid_supplier()) {
        controll=false;
    };
    if (!valid_address()) {
        controll=false;
    };
    if (!valid_email()) {
        controll=false;
    };
    if (!valid_phone()) {
        controll=false;
    };
    if (controll==true) {
        return true
    } else {
        return false
    }
}

function valid_cod_acc() {
    let x = document.forms["acc_form"]["cod_acc"].value;
    const elem = document.getElementById('answer_cod_acc');
    if (x == "") {
        elem.innerHTML = "Codul acessoriului trebuie completat";
        return false;
    }
    else {
        elem.innerHTML = "";
    }
    return true;
}

function valid_cod_supp() {
    let x = document.forms["acc_form"]["cod_supp"].value;
    const elem = document.getElementById('answer_cod_supp')
    if (x == "") {
        elem.innerHTML = " Adresa furnizorului trebuie completata";
        return false;
    }
    else {
        elem.innerHTML = "";
    }
    return true;
}

function valid_description() {
    let x = document.forms["acc_form"]["description"].value;
    const elem = document.getElementById('answer_description')
    if (x == "") {
        elem.innerHTML = " Descrierea accesoriului trebuie completata";
        return false;
    }
    else {
        elem.innerHTML = "";
    }
    return true;
}

function valid_supp() {
    let x = document.forms["acc_form"]["select_supp"].value;
    const elem = document.getElementById('answer_select_supp')
    if (x == "") {
        elem.innerHTML = " Trebuie  selectat un furnizor";
        return false;
    }
    else {
        elem.innerHTML = "";
    }
    return true;
}

function validation2() {
    let controll2=true;
    if (!valid_cod_acc()) {
        controll2=false;
    };
    if (!valid_cod_supp()) {
        controll2=false;
    };
    if (!valid_description()) {
        controll2=false;
    };
    if (!valid_supp()) {
        controll2=false;
    };
    if (controll2==true) {
        return true
    } else {
        return false
    }
}



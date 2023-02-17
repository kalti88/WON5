function factorial(n) {
    if (n != 0) {
        let fact = 1;
        for (let i=1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    } else {
        return 0;
    }
}

function check_number () {
    let nb = document.getElementById('num').value;
    let n = parseInt(nb);
    if (isNaN(n)){
        document.getElementById('answer').innerHTML ="<span class='color-red'>Nu se poate calcula factorialul.";
        }
        else{
            let fact = factorial(n);
            document.getElementById('answer').innerHTML ="<span class='color-green'>Factorialul numarului introdus este:" + fact;
        }

}
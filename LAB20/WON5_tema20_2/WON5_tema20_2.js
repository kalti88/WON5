function check_number () {
    let nb = document.getElementById('num').value;
    let n = parseFloat(nb);
    if (isNaN(n)){
        document.getElementById('answer').innerHTML ="Valoarea introdusa nu poate fi convertita la un numar.";
        }
        else {
            document.getElementById('answer').innerHTML ="Valoarea numerica extrasa este:" + n;
        }

}
$(document).ready(function() {

        var max = 20;
        var x = 1;
        $("#add").click(function(){
            if(x <= max){
                $("#table_field").append(cod_html);
                x++;
            }
        })

        $("#table_field").on('click', '#remove', function() {
            $(this).closest('tr').remove();
            x--;
            document.getElementById('x_hide').value = x;
            console.log(x);
        })

        $('#tab1').on('keydown', function(e){
            if(e.keyCode == 9){
                if(x <= max) {
                    $("#table_field").append(cod_html);
                    x++
                }
            }
        })

        $("#table_field").on('keydown', '#tab2', function(e) {
            if(e.keyCode == 9){
                if (x <= max){
                    $("#table_field").append(cod_html)
                    x++
                }
            }
        })
    })

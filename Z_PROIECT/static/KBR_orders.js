 $(document).ready(function() {

            var html = '<tr><td><input class="btn btn-danger" id="remove" type="button" name="remove" value="Remove" tabindex="-1"></td><td><input class="form-control" type="text" name="name[]" required></td><td><input class="form-control" type="file" id="tab2" name="logo[]" required></td></tr>';

            var max = 10;

            var x = 1;

            $("#add").click(function(){

                if(x <= max){

                    $("#table_field").append(html);

                    x++;

                }

            })



            $("#table_field").on('click', '#remove', function() {

                $(this).closest('tr').remove();

                x--;

            })



            $('#tab1').on('keydown', function(e){

                if(e.keyCode == 9){

                    if(x <= max) {

                        $("#table_field").append(html);

                        x++

                    }

                }

            })



            $("#table_field").on('keydown', '#tab2', function(e) {

                if(e.keyCode == 9){

                    if (x <= max){

                        $("#table_field").append(html)

                        x++

                    }

                }

            })

        })

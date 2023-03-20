 $(document).ready(function() {
            var html = '<tr>'+
                         '{% if def_supplier %}'+
                            '<td><select class="acc_list" name="accessories[]" required>'+
                                '<option> Selecteaza accesoriul </option>'+
                                '{% for i in accessories %}'+
                                    '<option>{{i[0]}}</option>'+
                                '{% endfor %}'+
                            '</select></td>'+
                            '<td><input type="text" class="form-control" name="qty[]" required></td>'+
                            '<td><input class="btn btn-danger" name="remove" id="remove" value="Sterge" type="button"></td>'+
                        '{% else %}'+
                            '<td><input type="text" class="form-control" name="name[]" required></td>'+
                            '<td><input type="text" class="form-control" name="qty[]" required></td>'+
                            '<td><input class="btn btn-danger" name="remove" id="remove" value="Sterge" type="button"></td>'+
                        '{% endif %}'+
                        '</tr>';
            var max = 20;
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

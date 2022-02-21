<!DOCTYPE html>
<html>
    <head>
        <title>Conversão Combustível</title>
        <meta charset="UTF-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">&nbsp;</div>

<?php

    if(!empty($_GET) && $_SERVER['REQUEST_METHOD'] == 'GET'){
        
        $precoetanol = str_replace(',', '.', $_GET['etanol']);
        $precogasolina = str_replace(',', '.', $_GET['gasolina']);

        $result = number_format(($precoetanol / $precogasolina), 2, '.','');

            if ($result <= 0.73){
                //echo ($result." - Alcool melhor");
                echo ("
                <div class='row text-center'>
                    <div class='alert alert-primary' role='alert'>".$result." - Alcool melhor</div>
                </div>
                ");

            }else{
                //echo ($result." - Gasolina Melhor");
                echo ("
                <div class='row text-center'>
                    <div class='alert alert-primary' role='alert'>".$result." - Gasolina melhor</div>
                </div>
                ");
            }
    }
?>
            <div class="row">
                <div class="col-4"></div>
                <div class="col-4 text-center">
                        <form action="#" class="needs-validation">
                            <label for="etanol" class="form-label">Preço do Etanol:</label><br />
                            <input type="text" class="form-control-lg" name="etanol" required onkeypress="return event.charCode >= 48 && event.charCode <= 57 || event.charCode <= 188 || event.charCode <= 190" /><br />
                            <label for="gasolina" class="form-label">Preço da Gasolina:</label><br />
                            <input type="text" class="form-control-lg" name="gasolina" required  onkeypress="return event.charCode >= 48 && event.charCode <= 57 || event.charCode <= 188 || event.charCode <= 190" /><br /><br />
                            <input type="submit" class="btn btn-success" value="Calcular"/>
                        </form>
                </div>
                <div class="col-4"></div>
            </div>
        </div>
    </body>
</html>
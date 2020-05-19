$(document).ready(function() {
    $( "#seleccion_especialidad" ).change(function() {
        var sel = $("#seleccion_especialidad option:selected").text();
        $("#link_buscar").attr("href", "/medicos/"+sel)
    });
});

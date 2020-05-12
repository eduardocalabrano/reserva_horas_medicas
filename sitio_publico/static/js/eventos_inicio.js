$(document).ready(function() {
    $( "#seleccion_especialidad" ).change(function() {
        // var sel = $( "select#seleccion_especialidad" ).val();
        var sel = $("#seleccion_especialidad option:selected").text();
        // alert(sel);
        // link_buscar
        $("#link_buscar").attr("href", "/medicos/"+sel)
    });
});

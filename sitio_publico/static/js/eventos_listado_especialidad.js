$(document).ready(function() {
  $(".solhora").click(function() {
    console.log($(this).attr('data-med'));
    var full_ident = $("#card_title_med_"+$(this).attr('data-med')).html();
    $("#span_medico").html(full_ident);
    $.ajax({
        url: '/ajax/retorna_horasdisponibles/',
        data: {
          'id': $(this).attr('data-med')
        },
        dataType: 'json',
        success: function (data) {
          console.log(data);
          // $("#auto_year_1").html(data.year_car);
          // $("#auto_velmax_1").html(data.speed_car);
          // $("#auto_asientos_1").html(data.asientos_car);
          // $("#auto_cc_1").html(data.cc_car);
          // $("#auto_hp_1").html(data.hp_car);
          // $("#imagen_auto_1").attr("src","/media/"+data.photo_car);
        }
      });
  });
});

$(".bot_confirma_reserva").click(function() {
  console.log('La reserva se confirma');
});

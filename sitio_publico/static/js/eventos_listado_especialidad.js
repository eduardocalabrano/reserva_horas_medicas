$(document).ready(function() {
  $('.alerta_formulario_reserva').hide();
  $('#footer_respuesta_ok').hide();
  $('#footer_respuesta_error').hide();

  let id_medico = '';
  $(".solhora").click(function() {
    //Se abrió el modal con el formulario para solicitar una hora médica
    var full_ident = $("#card_title_med_"+$(this).attr('data-med')).html();
    $("#span_medico").html(full_ident); //Se muestra el nombre del médico al inicio del modal
    id_medico = $(this).attr('data-med');
    $.ajax({ //Carga de fechas disponibles para el médico seleccionado
        url: '/ajax/fechas_disponibles/',
        data: {
          'id': $(this).attr('data-med')
        },
        dataType: 'json',
        success: function (data) {
          const dias_sigla = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
          data.forEach(el => {
            let fecha = new Date(el['fecha_cita']);
            let mes = '';
            fecha.setDate(fecha.getDate() + 1);
            const dayName = dias_sigla[fecha.getDay()];
            if(fecha.getMonth() < 10){
              mes = '0'+(fecha.getMonth() + 1); //Se agrega el 0 para números de 1 solo dígito. ¿Existe una forma más automática?
            }else{
              mes = (fecha.getMonth() + 1);
            }
            let fecha_bonita = dayName+" "+fecha.getDate()+"/"+mes;
            $('#select_fecha_medico').append(new Option(fecha_bonita, el['fecha_cita']))
          });
        }
      });//Fin llamada AJAX para obtener fechas disponibles para el médico seleccionado
  });

  $( "#select_fecha_medico" ).change(function() {
  //Evento que se activa cuando se consulta las horas disponibles para una fecha seleccionada
      $('#select_hora_medico').empty().append('<option value="0" selected disabled>-- : --</option>');
      // console.log('medico: '+id_medico);
      let sel = $("#select_fecha_medico option:selected").val();
      $.ajax({ //Cada vez que se cambia la fecha seleccionada se consultan las horas disponibles.
          url: '/ajax/horas_disponibles/',
          data: {
            'fecha_buscar': sel,
            'id_medico': id_medico
          },
          dataType: 'json',
          success: function (data) {
            data.forEach(el => {
              //Por el momento usaré un split para eliminar los segundos de las hora de inicio y término.
              let inicio_descompuesta = el['hora_inicio_cita'].split(":");
              let fin_descompuesta = el['hora_fin_cita'].split(":");
              // TODO: En lo posible reemplazar esos split por algo mejor
              let horario_texto = (inicio_descompuesta[0]+":"+inicio_descompuesta[1])+" - "+(fin_descompuesta[0]+":"+fin_descompuesta[1]);
              $('#select_hora_medico').append(new Option(horario_texto, el['id']))
            });
          }
      });
  });

  $(".bot_confirma_reserva").click(function() {
    validar_datos_form_reserva().then(function(result) {
      //La validación de los datos está correcta por lo que se procede a generar la reserva
      $(".dato_paciente").prop( "disabled", true );
      $(".btn_modal").prop( "disabled", true );
      $(".bot_confirma_reserva").html('<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span> Espere...')

      let hor = $("#select_hora_medico option:selected").val();
      let rut = $("#rut_paciente").val();
      let nom = $("#nombre_paciente").val();
      let ape = $("#apellidos_paciente").val();
      let fon = $("#telefono_paciente").val();
      let ema = $("#email_paciente").val();

      $.ajax({
          url: '/ajax/ingresa_paciente/',
          data: {
            'id_hora': hor,
            'rut': rut,
            'nom': nom,
            'ape': ape,
            'fon': fon,
            'ema': ema
          },
          dataType: 'json',
          success: function (data) {
            // Reserva registrada correctamente
            $('#footer_botones').hide();
            $('#footer_respuesta_ok').show();
          },
          error: function(){
            $('#footer_botones').hide();
            $('#footer_respuesta_error').show();
          }
      });
    }, function(err) {
      //El proceso de validación alertó de uno o mas campos con error.

    });
  });

});

$("#cierre_modal, #cancelar_modal, .btn_cierre_modal").click(function() {
  //Acciones necesarias para limpiar el formulario del modal.
  // 1.- Ocultar mensajes de respuesta y volver a mostrar botones.
  $('#footer_respuesta_ok').hide();
  $('#footer_respuesta_error').hide();
  $('#footer_botones').show();
  // 2.- Quitar el mensaje de "Espere..."
  $(".bot_confirma_reserva").html('Confirmar Reserva');
  // 3.- Habilitar campos y botones de acción
  $(".dato_paciente").prop( "disabled", false );
  $(".btn_modal").prop( "disabled", false );
  // 4.- Dejar inputs vacíos
  $(".dato_paciente").val('');
  // 5.- Eliminar opciones de fecha y hora de médico consultado
  $('#select_fecha_medico').empty().append('<option selected="selected" value="0" disabled>Seleccione Fecha</option>');
  $('#select_hora_medico').empty().append('<option value="0" selected disabled>-- : --</option>');
  // 6.- Ocultar mensajes de alertas de los campos mal ingresados o con datos faltantes
  $('.alerta_formulario_reserva').hide();
  // 7.- Eliminar ID de médico consultado previamente
  id_medico = '';
});

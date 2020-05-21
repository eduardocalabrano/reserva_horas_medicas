function validar_datos_form_reserva(evento){
    return new Promise((resolve, reject) =>{
      let hor = $("#select_hora_medico option:selected").val();
      flag_rechazar = 0;

      flag_rechazar += check_input('nombre', 3)
      flag_rechazar += check_input('apellidos', 3)
      flag_rechazar += check_input('telefono', 12)
      flag_rechazar += check_input('email', 6)
      flag_rechazar += check_input('rut', 9)
      if($("#select_hora_medico option:selected").val() === '0'){
        flag_rechazar += 1;
        $("#select_hora_medico").focus();
        $("#alerta_select_hora").show();
      }
      if($("#select_fecha_medico option:selected").val() === '0'){
        flag_rechazar += 1;
        $("#select_fecha_medico").focus();
        $("#alerta_select_fecha").show();
      }
      if(flag_rechazar > 0){ //Mientras exista un campo rechazado por validación, el promise será reject
        reject()
      }else{
        resolve()
      }
    });
}

function check_input(campo, largo_minimo){
  //Función que revisa un input y evalua el tamaño del texto ingresado.
  if(($("#"+campo+"_paciente").val()).length < largo_minimo){
    $("#"+campo+"_paciente").focus();
    $("#alerta_"+campo).show();
    return 1
  }else{
    return 0
  }
}

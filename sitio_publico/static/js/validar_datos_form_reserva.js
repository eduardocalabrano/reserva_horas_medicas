function validar_datos_form_reserva(evento){
    return new Promise((resolve, reject) =>{
      let hor = $("#select_hora_medico option:selected").val();
      flag_rechazar = 0;
      flag_rechazar += check_input('email', 6)
      flag_rechazar += check_input('telefono', 12)
      flag_rechazar += check_input('apellidos', 3)
      flag_rechazar += check_input('nombre', 3)
      flag_rechazar += check_input('rut', 9)
      if($("#select_hora_medico option:selected").val() === '0'){
        flag_rechazar += 1;
        $("#select_hora_medico").focus();
        $("#alerta_select_hora").show();
      }else{
        $("#alerta_select_hora").hide();
      }
      if($("#select_fecha_medico option:selected").val() === '0'){
        flag_rechazar += 1;
        $("#select_fecha_medico").focus();
        $("#alerta_select_fecha").show();
      }else{
        $("#alerta_select_fecha").hide();
      }
      if(flag_rechazar > 0){ //Mientras exista un campo rechazado por validación, el promise será reject
        reject()
      }else{
        if(email_formato()){
          resolve()
        }else{
          reject()
        }
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
    $("#alerta_"+campo).hide();
    return 0
  }
}

function email_formato(){
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    // console.log(re.test(String(correo).toLowerCase()));
    if (re.test(String($("#email_paciente").val()).toLowerCase()) == true) {
      return true
    } else {
      $("#email_paciente").focus();
      $("#alerta_email").show();
      return false
    }
}

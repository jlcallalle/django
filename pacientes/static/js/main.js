// Main

var MyApp = {

  getEdadCrear : function () {
      console.log('page crear usuario');
      var inputFecha = document.getElementById("id_fecha");
      inputFecha.addEventListener("blur", myBlurFunction, true);
      function myBlurFunction() {
          var valorFecha = inputFecha.value;
          console.log(valorFecha);

          //pasar datos a input
          var inputEdad = document.getElementById('inputEdad');
          var anio = inputFecha.value.substring(0, 4);
          var edadFinal = 2019 - anio;
          inputEdad.value = edadFinal;
      }
  },
  getEdadEditar : function () {
      console.log('page editar usuario');
      var inputFecha = document.getElementById("id_fecha");
      var valorFecha = inputFecha.value;

    //pasar datos a input
      var inputEdad = document.getElementById('inputEdad');
      var anio = inputFecha.value.substring(0, 4);
      var edadFinal = 2019 - anio;
      inputEdad.value = edadFinal;
  }
}

$(function () {

  if ($('.page-crear-paciente').length) {
      MyApp.getEdadCrear();
  }
  if ($('.section-editar').length) {
      MyApp.getEdadEditar();
  }

});

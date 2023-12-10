/*
  --------------------------------------------------------------------------------------------------------------------------------------------------
  Funções 
  --------------------------------------------------------------------------------------------------------------------------------------------------
*/

// -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
$(document).ready(function(){
  console.log("carregou js_index.js");

  $.ajax({
    url: "http://127.0.0.1:5001/pacientes",
    type: "GET",
    success: function(result){
      $.each(result['pacientes'], function(i, values){
        tr_sample = $(".sample_row").clone().removeClass("sample_row").addClass("row_paciente");
        tr_sample.find(".div_name").text(values["name"]);
        tr_sample.addClass("row_name_"+values["name"]);

        if(values["outcome"] == "0"){
          console.log("entrou no if");
          resultado = "<span style='color:#ce0d00;'> Negativo </span>"
        }else{
          resultado = "<span style='color:#1d8c3c;'> Pegativo </span>"
        }
        tr_sample.find(".div_output").html(resultado);
        tr_sample.show();

        $("#table_pacientes").find("tbody").prepend(tr_sample);        
      });
    },
    complete: function(){
    }, 
    beforeSend: function(){
      $(".row_paciente").remove();
    },
    error: function(xhr, status, error) {
      console.error("Error occurred: " + status + "\nError: " + error);
    }
  });

});

//__________________________________________________________________________________________________________________________________________________
//funções com listen --------------------------------------------------------------------------------------------------------------------------------

$(document).on("click", '.btn_diagnosticar', function(e){
  console.log("btn_diagnosticar");
  e.preventDefault();

  const formDiagnostico = new FormData();
  formDiagnostico.append('name', $(".input_name").val());
  formDiagnostico.append('age', $(".input_age").val());
  formDiagnostico.append('sex', $(".input_sex").val());
  formDiagnostico.append('chest_pain_type', $(".input_chest_pain_type").val());
  formDiagnostico.append('resting_BP', $(".input_resting_BP").val());
  formDiagnostico.append('cholesterol', $(".input_cholesterol").val());
  formDiagnostico.append('fasting_BS', $(".input_fasting_BS").val());
  formDiagnostico.append('resting_ECG', $(".input_resting_ECG").val());
  formDiagnostico.append('max_HR', $(".input_max_HR").val());
  formDiagnostico.append('exercise_Angina', $(".input_exercise_Angina").val());
  formDiagnostico.append('oldpeak', $(".input_oldpeak").val());
  formDiagnostico.append('st_Slope', $(".input_st_Slope").val());

  console.log("formDiagnostico", formDiagnostico);
  console.log($(".input_name").val(),$(".input_age").val(), $(".input_sex").val(),$(".input_chest_pain_type").val(),$(".input_resting_BP").val(),$(".input_cholesterol").val(),$(".input_fasting_BS").val(),$(".input_resting_ECG").val(),$(".input_max_HR").val(),$(".input_exercise_Angina").val(),$(".input_oldpeak").val(),$(".input_st_Slope").val());
  
  $.ajax({
    url: "http://127.0.0.1:5001/paciente_predict",
    type: "POST",
    data: formDiagnostico,
    processData: false,
    contentType: false,

    success: function(result){
      console.log(result);
      tr_sample = $(".sample_row").clone().removeClass("sample_row").addClass("row_paciente");
      tr_sample.find(".div_name").text(result["name"]);
      tr_sample.addClass("row_name_"+result["name"]);

      if(result["outcome"] == "0"){
        console.log("entrou no if");
        resultado = "<span style='color:#ce0d00;'> Negativo </span>"
      }else{
        resultado = "<span style='color:#1d8c3c;'> Positivo </span>"
      }
      tr_sample.find(".div_output").html(resultado);
      tr_sample.show();
      $("#table_pacientes").find("tbody").prepend(tr_sample);        
    },
    error: function(xhr, status, error) {
      console.error("Error occurred: " + status + "\nError: " + error);
    }
  });
});

$(document).on("click", '.delete_paciente', function(e){
  e.preventDefault();
  console.log("clicou");
  name_paciente = $(this).closest("tr").find(".div_name").text();
  $.ajax({
    url: "http://127.0.0.1:5001/paciente?name="+name_paciente,
    type: "DELETE",
    success: function(result){
      console.log(result);
      $(".row_name_"+name_paciente).remove();
    },
    complete: function(){
    }, 
    error: function(xhr, status, error) {
      console.error("Error occurred: " + status + "\nError: " + error);
    }
  });
});

$(document).on("click",'.nav-link', function(e){
  e.preventDefault();
    name_class = $(this).data('div_scroll')
    var target = $("."+name_class)
    
    if (target.length) {
      var container = $(".div_principal")
      var scrollTo = target.offset().top - container.offset().top + container.scrollTop();

      container.animate({
        scrollTop: scrollTo
      }, 1000); 

    }
})
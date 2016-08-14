/**
 * Created by H4 on 14/08/2016.
 */
var App = App || {};

App.FormularioController = {
  listen: function () {
      var date = new Date();
      $( ".datepicker" ).datepicker({
      changeMonth: true,
      changeYear: true,
          yearRange: 'c-130:c'
    });
  }
};
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (response) {
      const name = response.name;
      $('DIV#character').text(name);
    },
    error: function (error) {
      console.log(error);
    }
  });
});

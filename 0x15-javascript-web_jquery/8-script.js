$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (response) {
      const data = response.results;
      for (const args of data) {
        $('UL#list_movies').append(`<li>${args.title}</li>`);
      }
    },
    error: function (error) {
      console.log(error);
    }
  });
});

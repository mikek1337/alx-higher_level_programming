$(document).ready(() => {
  const response = $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    async: false
  }).responseJSON;
  for (const result of response.results) {
    $('#list_movies').append('<li>' + result.title + '</li>');
  }
});

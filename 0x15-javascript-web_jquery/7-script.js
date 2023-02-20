$(document).ready(() => {
  const res = $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    dataType: 'json',
    method: 'GET',
    async: false
  }).responseJSON;
  $('#character').text(res.name);
});

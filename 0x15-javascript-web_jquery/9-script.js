$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (res) => {
    $('#hello').text(res.hello);
  });
});

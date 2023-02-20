$(document).ready(() => {
  $('#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').on('click', () => {
    $('ul.my_list li').last().remove();
  });
  $('#clear_list').on('click', () => {
    $('ul.my_list').html('');
  });
});

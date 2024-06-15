// 3. Add a click event to the tag DIV#red_header

document.querySelector('DIV#red_header').addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});

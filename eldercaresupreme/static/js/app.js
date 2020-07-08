document.addEventListener("DOMContentLoaded", () => {
    M.AutoInit(); /* Can't pass in options with M.AutoInit(), only use default values */
    let elemsDatepicker = document.querySelectorAll(".datepicker");
    let instanceDatepicker = M.Datepicker.init(elemsDatepicker, {
        yearRange: 3,
        format: 'yyyy-mm-dd'
    });
});

// Call time picker
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.timepicker');
  var instances = M.Timepicker.init(elems, {
    // 24h required for db
    twelveHour: false,
  });
});

// Tool tips
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.tooltipped');
  var instances = M.Tooltip.init(elems);
});
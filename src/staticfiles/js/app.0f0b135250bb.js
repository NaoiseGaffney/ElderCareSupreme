document.addEventListener("DOMContentLoaded", () => {
    M.AutoInit(); /* Can't pass in options with M.AutoInit(), only use default values */
    let elemsDatepicker = document.querySelectorAll(".datepicker");
    let instanceDatepicker = M.Datepicker.init(elemsDatepicker, {
        yearRange: 3,
        format: 'yyyy-mm-dd'
    });
    /* let elemsSidenav = document.querySelectorAll(".sidenav");
    let instancesSidenav = M.Sidenav.init(elemsSidenav); // Remove "options" from (elems, options)
    let elemsMaterialboxed = document.querySelectorAll(".materialboxed");
    let instancesMaterialboxed = M.Materialbox.init(elemsMaterialboxed); // Remove "options" from (elems, options)
    let elemsParallax = document.querySelectorAll(".parallax");
    let instancesParallax = M.Parallax.init(elemsParallax); // Remove "options" from (elems, options)
    let elemsTabs = document.querySelectorAll(".tabs");
    let instanceTabs = M.Tabs.init(elemsTabs);
    let elemsTooltip = document.querySelectorAll(".tooltipped");
    let instanceTooltip = M.Tooltip.init(elemsTooltip);
    let elemsScrollspy = document.querySelectorAll(".scrollspy");
    let instanceScrollspy = M.ScrollSpy.init(elemsScrollspy, {
        throttle: 10
    });
    let elemsDatepicker = document.querySelectorAll(".datepicker");
    let instanceDatepicker = M.Datepicker.init(elemsDatepicker, {
        disableWeekends: true,
        yearRange: 3
    });
    let elemsModal = document.querySelectorAll(".modal");
    let instancesModal = M.Modal.init(elemsModal, {
        dismissible: false,
        inDuration: "200"
    }); */
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
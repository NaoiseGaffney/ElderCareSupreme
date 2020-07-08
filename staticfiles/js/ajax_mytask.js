$(".done-btn").click(function (e) {
  e.preventDefault();
  var this_ = $(this)
  var doneUrl = this_.attr("data-href")
  $.ajax({
    url: doneUrl,
    method: "GET",
    data: {},
    success: function (data) {
      jQuery(document).ready(function ($) {
        if (data.is_done) {
          this_[0].style.backgroundColor = "#f06292";
        } else {
          this_[0].style.backgroundColor = "#cecece";
        }
      });
    }, error: function (error) {
      console.log(error)
      console.log("error")
    }
  })
})
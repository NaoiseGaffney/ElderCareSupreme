$(".add-aider-btn").click(function(e){
  e.preventDefault();
  var this_ = $(this)
  var aiderUrl = this_.attr("data-href")
  var aiderName = this_.siblings(".assigned-aider");
  var aiderIcon = this_.siblings(".aider-icon");
  console.log("*****");
  console.log(aiderName);
  console.log("*****");
  $.ajax({
    url: aiderUrl,
    method: "GET",
    data:{},
    success: function(data) {
      jQuery( document ).ready(function( $ ) {
        if(data.aider != null && data.aider != "aider_assigned"){
          aiderName[0].innerHTML = `<b>Assigned aider - ${data.aider}</b>`;
          aiderName[0].classList.add("pinkish");
          aiderIcon[0].classList.add("pinkish");
          aiderName[0].classList.remove("slide-in-elliptic-left-fwd");
          aiderIcon[0].classList.remove("slide-in-elliptic-left-fwd");
          void aiderName[0].offsetWidth;
          void aiderIcon[0].offsetWidth;
          aiderName[0].classList.add("slide-in-elliptic-left-fwd");
          aiderIcon[0].classList.add("slide-in-elliptic-left-fwd");
        } else if(data.aider == "aider_assigned") {
            $("#fixed-message").show().delay(5000).fadeOut();
        } else {
          aiderName[0].innerHTML = "<b>No Assigned Aider</b>";
          aiderName[0].classList.remove("pinkish");
          aiderIcon[0].classList.remove("pinkish");
        }
      });
    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
})

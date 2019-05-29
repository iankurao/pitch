$(document).ready(function () {
  $("#update").click(function(){
    Swal.fire({
    type: 'success',
    title: 'Success',
    text: 'Profile Updated ',
    timer:2000,
    showConfirmButton:false
  })
  })
  // $("#submit").click(function () {
  //   Swal.fire({
  //   type: 'success',
  //   title: 'Success',
  //   timer:2000,
  //   showConfirmButton:false
  // })
  //
  // })

  $(".title").mouseover(function(){
    $("span").show()

  })
  $("#login").click(function(){
    Swal.fire({
    type: 'warning',
    title: 'Login Required',
    text: 'Please Login to Post your Idea',
    html:'<a class="btn default-color" href="/authenticate/login">Sign in</a>',
    showConfirmButton:false
  })
  $(".profile").hide()
  $("#change").show()
  })

  /*business logig*/

  $("#aii").click(function(){
    $("#AI").show()
    $("#D").hide()
    $("#R").hide()
    $("#IoT").hide()

  })
  $("#robot").click(function(){
    $("#AI").hide()
    $("#D").hide()
    $("#R").show()
    $("#IoT").hide()

  })
  $("#ot").click(function(){
    $("#AI").hide()
    $("#D").hide()
    $("#R").hide()
    $("#IoT").show()

  })
  $("#dro").click(function(){
    $("#AI").hide()
    $("#D").show()
    $("#R").hide()
    $("#IoT").hide()

  })
  $("#change").click(function(){
    $(".profile").show()
    $("#change").hide()
  })
  like=0;

  function likes(){
    like++
  }
  dislikes=0;
  function dislike(){
    dislikes--
  }
  $("#like").click(function(){
    likes()
    $("#p").text(like)
  })
  $("#dislike").click(function(){
    dislike()
    $("#p1").text(dislikes)
  })

  $("#love").click(function(){
    $("#spinner").show();
    totalScore=0
    var startCount=60;
    function beginLoop() {
      setTimeout(function(){
        startCount--;

        if(startCount>=totalScore){
          if(startCount==0){
            $("#spinner").hide();
            $("#sho").text(60)
          }
          $("#sho").text(startCount)

          beginLoop();
        }

      }, 800)

    }
    beginLoop();

  })


  ///



})

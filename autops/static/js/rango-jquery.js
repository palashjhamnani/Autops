/**
 * Created by SESA384685 on 19-Dec-15.
 */



//For getting CSRF token
function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
         var cookie = jQuery.trim(cookies[i]);
         // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) == (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
          }
     }
 }
 return cookieValue;
}


//For doing AJAX post
 $("#submit").click(function(e) {

 e.preventDefault();

 var csrftoken = getCookie('csrftoken');

 //var email = $('#inputEmail').val();

 //var password = $('#inputPassword').val();

//This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post

 $.ajax({
         url : 'rango/hom/', // the endpoint,commonly same url
         type : "POST", // http method
         data : { csrfmiddlewaretoken : csrftoken
         //email : email,
         //password : password
 }, // data sent with the post request

 // handle a successful response
 success : function(json) {
      console.log(json); // another sanity check
      //On success show the data posted to server as a message
     $('#result').append( 'ServerResponse:' + json.Status);
      //alert('Hi '+json['email'] +'!.' + ' You have entered password:'+json['password']);


 },

 // handle a non-successful response
 error : function(xhr,errmsg,err) {
 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
 }
 });
});








$(document).ready(function() {

        // JQuery code to be added in here.

});
$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
});

$(document).ready(function() {
            $("#button").click(function() {
                    var input_string = $("#forminput").val();
                    $.ajax({
                        url : "rango/ajaxexample_json",
                        type : "POST",
                        dataType: "json",
                        data : {
                            client_response : input_string,
                            },
                        success : function(json) {
                            $('#result').append( 'ServerResponse:' + json.server_response);
                        },
                        error : function(xhr,errmsg,err) {
                            alert(xhr.status + ": " + xhr.responseText);
                        }
                    });
                    return false;
            });
        });
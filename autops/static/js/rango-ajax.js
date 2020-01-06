/**
 * Created by SESA384685 on 19-Dec-15.
 */
/**$('#likes').click(function(){
    $.get('/rango/stopservice/'
});
*/
$(function(){
    $("#service").click(function(){
        $.post(
         url : "/rango/stopservice/",
         dataType:"html",
         success: function(data, status, xhr){
            //do something with your data
        }
        );
        return false;
    });
});


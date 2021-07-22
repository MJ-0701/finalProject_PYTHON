$(document).ready(function(){
    $('.login-info-box').fadeOut();
    $('.login-show').addClass('show-log-panel');
    });
    $('.login-reg-panel input[type="radio"]').on('change', function() {
    if($('#log-login-show').is(':checked')) {
        $('.register-info-box').fadeOut();
        $('.login-info-box').fadeIn();

        $('.white-panel').addClass('right-log');
        $('.register-show').addClass('show-log-panel');
        $('.login-show').removeClass('show-log-panel');
    }
    else if($('#log-reg-show').is(':checked')) {
        $('.register-info-box').fadeIn();
        $('.login-info-box').fadeOut();

        $('.white-panel').removeClass('right-log');

        $('.login-show').addClass('show-log-panel');
        $('.register-show').removeClass('show-log-panel');
    }
});
  $(document).ready(function(){
    $('#tab-2').click(function(){
      $(".login-html").css("height","770px")
   });
   $('#tab-1').click(function(){
      $(".login-html").css("height","510px")
   });
});
$(function(){
  $("#idCheck").hide();
})
if($("#session").val()!=""){
      var button = '<input onClick=\"location.href=\'home\'\" type=\"button\" class=\"button\" value=\"이미 로그인되어있습니다.\">'
      $(".login-html").html(button)
}
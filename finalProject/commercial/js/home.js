
 $("#clicck").click(function(){$.ajax({
    url: "product",
    success:function(d){
        $("#product").html(d)
    }
  })
 })
if ($("#session").val()!=""){
      $("#login").attr("id", "logout").attr("href","logout").html("<h6> 로그아웃 <h6>")
}

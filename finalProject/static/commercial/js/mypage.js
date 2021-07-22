$(document).ready(function(){
    var jsonStr = $("#session").val();
    var jsonObj = JSON.parse(jsonStr);
    var anum_data = jsonObj.ANUM["0"] ;
    $("#userNUM").val(anum_data);
    $("#myinfor").click(function(){
        $("#user_action").attr("action","mypage_info").submit();
        });
    });
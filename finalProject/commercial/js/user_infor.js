$(document).ready(function(){
    var jsonStr = $("#session").val();
    var jsonObj = JSON.parse(jsonStr);

    var anum_data = jsonObj.ANUM["0"] ;

    var jsonstr1 = $("#user_jsonstr").val();
    var jsonObj1 = JSON.parse(jsonstr1);
        console.log(jsonObj1);

    $("#aid").val(jsonObj1.AID["0"]);
    $("#apwd").val(jsonObj1.APWD["0"]);
    $("#ainday").val(jsonObj1.AINDAY["0"]);
    $("#achgday").val(jsonObj1.ACHGDAY["0"]);
    $("#agubun").val(jsonObj1.AGUBUN["0"]);
    $("#adivision").val(jsonObj1.ADIVISION["0"]);

    $("#dname").val(jsonObj1.DNAME["0"]);
    $("#dbirth").val(jsonObj1.DBIRTH["0"]);
    $("#dgender").val(jsonObj1.DGENDER["0"]);
    $("#dtel").val(jsonObj1.DTEL["0"]);

    $("#psdate").val(jsonObj1.PSDATE["0"]);
    $("#pedate").val(jsonObj1.PEDATE["0"]);
    $("#ppay").val(jsonObj1.PPAY["0"]);
    $("#pway").val(jsonObj1.PWAY["0"]);
    $("#pgubun").val(jsonObj1.PGUBUN["0"]);
    $("#monthnum").val(jsonObj1.MONTHNUM["0"]);
    $("#kinds").val(jsonObj1.KINDS["0"]);
    $("#mentnum").val(jsonObj1.MENTNUM["0"]);
    $("#inment").val(jsonObj1.INMENT["0"]);


    $('.tab_menu_btn').on('click',function(){
     //버튼 색 제거,추가
     $('.tab_menu_btn').removeClass('on');
     $(this).addClass('on')

     //컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
     var idx = $('.tab_menu_btn').index(this);

    $('.tab_box').hide();
    $('.tab_box').eq(idx).show();
    });

    //$("#myinfor").click(function(){
    //    $("#user_action").attr("action","mypage_info").submit();
     //   });


    });
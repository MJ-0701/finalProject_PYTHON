function sleep (delay) {
   var start = new Date().getTime();
   while (new Date().getTime() < start + delay);
}

$.ajax({
    url:"getCardDataForGuName",
    success:function(d){
        $("#guName").html(d);
    },error:function(e){
        console.log(e);
    }
})

 $.ajax({
        url:"getCardDataForDongName?guName=강남구",
        success:function(d){
            $("#dongName").html(d);
        },error:function(e){
            console.log(e);
     }
 })
 $.ajax({
        url:"getApartName?guName=강남구&dongName=개포동",
        success:function(d){
             $("#apartName").html(d);
        },error:function(e){
            console.log(e);
     }
 })
 $.ajax({
        url:"getExclusiveArea?guName=강남구&dongName=개포동&aptName=개포2차현대아파트(220)",
        success:function(d){
             $("#exclusive_use_area").html(d);
        },error:function(e){
            console.log(e);
     }
 })

$("#guName").change(function(){
    $.ajax({
        url:"getCardDataForDongName?guName="+$(this).val(),
        success:function(d){
            $("#dongName").html(d);
        },error:function(e){
            console.log(e);
        }
    })
})
$("#dongName").change(function(){
    $.ajax({
        url:"getApartName?guName="+$("#guName").val() +"&dongName="+$(this).val(),
        success:function(d){
            $("#apartName").html(d);
        },error:function(e){
            console.log(e);
        }
    })
})
$("#apartName").change(function(){
    $.ajax({
        url:"getExclusiveArea?guName="+$("#guName").val() +"&dongName="+$("#dongName").val()+"&aptName="+$(this).val(),
        success:function(d){
            $("#exclusive_use_area").html(d);
        },error:function(e){
            console.log(e);
        }
    })
})
$("#moreInfoAdd").change(function(){
    var add = "<a class='btn btn-3 btn-sep icon-heart info'>"+$(this).val() +"</a>"
    var adddata = "<input type='hidden' name='selectedChart[]' id='"+$(this).val()+"' value='"+ $(this).val()+"'>"
    console.log(adddata)
    if($(this).val()=='선택하세요'){

    }else{
        $("#select_list").append(add)
        $("#select_list").append(adddata)
        removeA()
    }
})

function removeA(){
$("a").click(function(){
        var tagName = "#"+$(this).text()
        $(this).remove();
        $(tagName).remove();
    })
}
$.ajaxPrefilter('json', function(options, orig, jqXHR){
		return 'jsonp';
});
$("#pyung").on("input",function(){
    var key = $(this).val()
    if(isNaN(key) == true){

    }else{
        key = parseInt(key) * 3.305785;
        console.log(key)
        $("#exclusive_use_area").val(key)
    }
})


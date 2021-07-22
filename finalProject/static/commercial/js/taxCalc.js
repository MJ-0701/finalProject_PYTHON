
$(".tab-2").click(function(){
    $(".tab-2").css("z-index",1)
    $(this).css("z-index",99)
})

$("#calc").click(function(){
    var value = $("#getPrice").val()
    var regex = /[^0-9]/gi;
    if($("#getPrice").val() == ''){
        alert("값을 입력해주세요")
    }else if(value.match(regex)){
        alert("숫자만 입력해 주세요.")
    }
    else{
    $.ajax({
        url:"getPriceCalc?getPrice="+$("#getPrice").val(),
        success:function(result){
            $("#getValue").html(result)
        }
    })
    }
})

$("#recalc").click(function(){
    location.href ="goCalc";
    $(".tab-2:nth-child(1)").attr("checked","true")
})
$("#recalc2").click(function(){
    var elm = document.querySelector('input[id="tab2-2"]:checked');
    location.href ="goCalc?"+elm.value;
})
$("#recalc3").click(function(){
    var elm = document.querySelector('input[id="tab2-3"]:checked');
    location.href ="goCalc?"+elm.value;
})

$("#calc2").click(function(){
    var value = $("#inheritPrice").val()
    var regex = /[^0-9]/gi;
    if($("#inheritPrice").val() == ''){
        alert("값을 입력해주세요")
    }else if(value.match(regex)){
        alert("숫자만 입력해 주세요.")
    }
    else{
    $.ajax({
        url:"inheritTaxCalc?getPrice="+$("#inheritPrice").val(),
        success:function(result){
            $("#getValue2").html(result)
        }
    })
    }
})

$("#calc3").click(function(){
    var value = $("#givePrice").val()
    var regex = /[^0-9]/gi;
    if($("#givePrice").val() == ''){
        alert("값을 입력해주세요")
    }else if(value.match(regex)){
        alert("숫자만 입력해 주세요.")
    }
    else{
    $.ajax({
        url:"inheritTaxCalc?getPrice="+$("#givePrice").val(),
        success:function(result){
            $("#getValue3").html(result)
        }
    })
    }
})
$("#givePrice2").on("input",function(){
    var givePrice = Number(this.value)
    var getPrice = Number($("#getPrice2").val())
    var cost = Number($("#cost").val())
    result = givePrice - getPrice - cost
    $("#benefit").text(result+'만원');
})

$("#getPrice2").on("input",function(){
    var givePrice = $("#givePrice2").val()
    var getPrice = Number(this.value)
    var getPrice = Number($("#getPrice2").val())
    var cost = Number($("#cost").val())
    result = givePrice - getPrice - cost
    $("#benefit").text(result+'만원');
})

$("#cost").on("input",function(){
    var givePrice = $("#givePrice2").val()
    var getPrice = Number($("#getPrice2").val())
    var cost = Number(this.value)
    result = givePrice - getPrice - cost
    $("#benefit").text(result+'만원');
})

$("#year").on("input",function(){
    var year = Number(this.value)
    console.log(year)
    var taxRatio;
    if(year < 3){
        taxRatio = 0;
    }else if(year <  4){
        taxRatio = 0.06;
    }else if(year <  5){
        taxRatio = 0.08;
    }else if(year <  6){
        taxRatio = 0.10;
    }else if(year <  7){
        taxRatio = 0.12;
    }else if(year <  8){
        taxRatio = 0.14;
    }else if(year <  9){
        taxRatio = 0.16;
    }else if(year <  10){
        taxRatio = 0.18;
    }else if(year <  11){
        taxRatio = 0.20;
    }else if(year <  12){
        taxRatio = 0.22;
    }else if(year <  13){
        taxRatio = 0.24;
    }else if(year <  14){
        taxRatio = 0.26;
    }else if(year <  15){
        taxRatio = 0.28;
    }else{
        taxRatio = 0.30;
    }
    console.log(taxRatio)
    var benefit = Number($("#benefit").text().substr(0,$("#benefit").text().indexOf('만')))
    console.log(benefit)
    var longtime = benefit * taxRatio
    var result = benefit - longtime
    var result2 = result-250
    $("#longtime").text(longtime+"만원")
    $("#incomePrice").text(result+"만원")
    $("#standardTax").text(result2  +"만원")
    if(result2 <= 1200 ){
        taxRatio = 0.06
    }else if(result2 <= 4600){
        taxRatio = 0.15
        gonggae = 108
    }else if(result2 <= 8800){
        taxRatio = 0.24
        gonggae = 522
    }else if(result2 <= 15000){
        taxRatio = 0.35
        gonggae = 1490
    }else if(result2 <= 30000){
        taxRatio = 0.38
        gonggae = 1940
    }else if(result2 <= 50000 ){
        taxRatio = 0.40
        gonggae = 2540
    }else{
        taxRatio = 0.42
        gonggae = 3540
    }
    var result3 = result2 * taxRatio - gonggae
    $("#taxRatio").text(taxRatio*100+"%")
    $("#cumulate").text(gonggae +"만원")
    $("#result").text(result3+"만원")
})
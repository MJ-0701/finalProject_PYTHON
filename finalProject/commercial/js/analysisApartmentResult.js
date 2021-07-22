function getDepositInterestRate(){	$.ajax({
		url         : 'http://ecos.bok.or.kr/api/StatisticSearch/IP2ZMMJQDFGT54G1RFJ3/json/kr/1/10/028Y001/MM/202001/202007/BEEA220/',
		type        : 'GET',
		dataType    : 'json',
		success     : function (result) {
			makeDepositInterestRate(result);
		},
		error       : function (result) {
			console.log("error >> " + $(result).text());
		}
	});}
	function makeDepositInterestRate(jsonData) {
		var rows = jsonData.StatisticSearch.row;
		var datas = new Array();
		var xColumn = new Array();
		xColumn.push('x')
		datas.push(rows[0].ITEM_NAME1);
		for (var row in rows) {
			xColumn.push(rows[row].TIME);
			datas.push(rows[row].DATA_VALUE);
		}
		var chart = c3.generate({
			bindto: '#chartDepositInterestRate',
			data : {
				type : 'line',
				x : 'x',
				columns : [
				    xColumn,
					datas
				]
			},
			bar : {
				width : {
					radio : 0.5
				}
			}
		});
}
function getKODEX3YearChart(){	$.ajax({
		url         : 'http://ecos.bok.or.kr/api/StatisticSearch/IP2ZMMJQDFGT54G1RFJ3/json/kr/1/10/028Y001/MM/202001/202007/BEEA42/',
		type        : 'GET',
		dataType    : 'json',
		success     : function (result) {
			makeKODEX3YChart(result);
		},
		error       : function (result) {
			console.log("error >> " + $(result).text());
		}
	});}
	function makeKODEX3YChart(jsonData) {
		var rows = jsonData.StatisticSearch.row;
		var datas = new Array();
		var xColumn = new Array();
		xColumn.push('x')
		datas.push(rows[0].ITEM_NAME1);
		for (var row in rows) {
			xColumn.push(rows[row].TIME);
			datas.push(rows[row].DATA_VALUE);
		}
		var chart = c3.generate({
			bindto: '#chartKODEX3Y',
			data : {
				type : 'line',
				x : 'x',
				columns : [
				    xColumn,
					datas
				]
			},
			bar : {
				width : {
					radio : 0.5
				}
			}
		});
}
function getCDChart(){	$.ajax({
		url         : 'http://ecos.bok.or.kr/api/StatisticSearch/IP2ZMMJQDFGT54G1RFJ3/json/kr/1/10/028Y001/MM/202001/202007/BEEA21/',
		type        : 'GET',
		dataType    : 'json',
		success     : function (result) {
			makeBarChart(result);
		},
		error       : function (result) {
			console.log("error >> " + $(result).text());
		}
	});}
	function makeBarChart(jsonData) {
		var rows = jsonData.StatisticSearch.row;
		var datas = new Array();
		var xColumn = new Array();
		xColumn.push('x')
		datas.push(rows[0].ITEM_NAME1);
		for (var row in rows) {
			xColumn.push(rows[row].TIME);
			datas.push(rows[row].DATA_VALUE);
		}
		var chart = c3.generate({
			bindto: '#chartCD',
			data : {
				type : 'line',
				x : 'x',
				columns : [
				    xColumn,
					datas
				]
			},
			bar : {
				width : {
					radio : 0.5
				}
			}
		});
}
function getCDChart(){	$.ajax({
		url         : 'http://ecos.bok.or.kr/api/StatisticSearch/IP2ZMMJQDFGT54G1RFJ3/json/kr/1/10/028Y001/MM/202001/202007/BEEA21/',
		type        : 'GET',
		dataType    : 'json',
		success     : function (result) {
			makeBarChart(result);
		},
		error       : function (result) {
			console.log("error >> " + $(result).text());
		}
	});
}
	function makeBarChart(jsonData) {
		var rows = jsonData.StatisticSearch.row;
		var datas = new Array();
		var xColumn = new Array();
		xColumn.push('x')
		datas.push(rows[0].ITEM_NAME1);
		for (var row in rows) {
			xColumn.push(rows[row].TIME);
			datas.push(rows[row].DATA_VALUE);
		}
		var chart = c3.generate({
			bindto: '#chartCD',
			data : {
				type : 'line',
				x : 'x',
				columns : [
				    xColumn,
					datas
				]
			},
			bar : {
				width : {
					radio : 0.5
				}
			}
		});
}
var selectedChart = $("#selectedChart").val()
selectedChart = selectedChart.replace("[", "").replace("]","")
selectedChart = selectedChart.split(",")

for (i in selectedChart){
    if(selectedChart[i] == "'정기예금금리'"){
        getDepositInterestRate()
    }else if(selectedChart[i] == " '국고채(3년)'"){
        getKODEX3YearChart()
    }else if(selectedChart[i] == " 'CD'"){
        getCDChart()
    }
}
$.ajax({
    url:"getRealDealPrice?guName="+$("#guName").val()+"&dongName="+$("#dongName").val()+"&aptName="+$("#aptName").val(),
    success:function(d){
        $("#realdealpricetable").html(d)
    }
})

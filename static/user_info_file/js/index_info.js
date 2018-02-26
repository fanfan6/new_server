$(document).ready(function () {
    $.getJSON("/user_info/sex", function(data){
        $('#user_info').append(
            '<tr>' +
            '<td>时间</td>' +
            '<td>' + data.res_day[0].data[0].option[0] + '</td>' +
            '<td>' + data.res_day[0].data[0].option[1] + '</td>' +
            '</tr>'
        );
        $(data.res_day).each(function(i, value){
            $('#user_info').append(
            '<tr>' +
            '<td>' + value.time + '</td>' +
            '<td>' + value.data[0].count[0] + '</td>' +
            '<td>' + value.data[0].count[1] + '</td>' +
            '</tr>')
        });
        var myChart2 = echarts.init(document.getElementById('main2'));
        option = {
            tooltip : {
                trigger: 'axis',
                axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                    type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                }
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            yAxis:  {
                type: 'value'
            },
            xAxis: {
                type: 'category',
                data: [
                    data.res_day[11].time,
                    data.res_day[10].time,
                    data.res_day[9].time,
                    data.res_day[8].time,
                    data.res_day[7].time,
                    data.res_day[6].time,
                    data.res_day[5].time,
                    data.res_day[4].time,
                    data.res_day[3].time,
                    data.res_day[2].time,
                    data.res_day[1].time,
                    data.res_day[0].time
                ]
            },
            series: [
                {
                    name: '女',
                    type: 'bar',
                    stack: '总量1',
                    barWidth: 50,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: [
                        data.list_day_1[11],
                        data.list_day_1[10],
                        data.list_day_1[9],
                        data.list_day_1[8],
                        data.list_day_1[7],
                        data.list_day_1[6],
                        data.list_day_1[5],
                        data.list_day_1[4],
                        data.list_day_1[3],
                        data.list_day_1[2],
                        data.list_day_1[1],
                        data.list_day_1[0]
                    ]
                },
                {
                    name: '男',
                    type: 'bar',
                    stack: '总量1',
                    barWidth: 50,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: [
                        data.list_day_2[11],
                        data.list_day_2[10],
                        data.list_day_2[9],
                        data.list_day_2[8],
                        data.list_day_2[7],
                        data.list_day_2[6],
                        data.list_day_2[5],
                        data.list_day_2[4],
                        data.list_day_2[3],
                        data.list_day_2[2],
                        data.list_day_2[1],
                        data.list_day_2[0]
                    ]
                }
            ]
        };
        myChart2.setOption(option);
    })
})
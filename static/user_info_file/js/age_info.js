$(document).ready(function () {
    $.getJSON("/user_info/age", function(data){
        $('#user_info').append(
            '<tr>' +
            '<td>时间</td>' +
            '<td>' + data.res_day[0].data[0].option[0] + '</td>' +
            '<td>' + data.res_day[0].data[0].option[1] + '</td>' +
            '<td>' + data.res_day[0].data[0].option[2] + '</td>' +
            '<td>' + data.res_day[0].data[0].option[3] + '</td>' +
            '<td>' + data.res_day[0].data[0].option[4] + '</td>' +
            '<td>' + data.res_day[0].data[0].option[5] + '</td>' +
            '<td>' + data.res_day[0].data[0].option[6] + '</td>' +
            '</tr>'
        );
        $(data.res_day).each(function(i, value){
            $('#user_info').append(
            '<tr>' +
            '<td>' + value.time + '</td>' +
            '<td>' + value.data[0].count[0] + '</td>' +
            '<td>' + value.data[0].count[1] + '</td>' +
            '<td>' + value.data[0].count[2] + '</td>' +
            '<td>' + value.data[0].count[3] + '</td>' +
            '<td>' + value.data[0].count[4] + '</td>' +
            '<td>' + value.data[0].count[5] + '</td>' +
            '<td>' + value.data[0].count[6] + '</td>' +
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
                    name: '总量',
                    type: 'bar',
                    barWidth: 50,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: [
                        data.res_day[11].data[0].sum,
                        data.res_day[10].data[0].sum,
                        data.res_day[9].data[0].sum,
                        data.res_day[8].data[0].sum,
                        data.res_day[7].data[0].sum,
                        data.res_day[6].data[0].sum,
                        data.res_day[5].data[0].sum,
                        data.res_day[4].data[0].sum,
                        data.res_day[3].data[0].sum,
                        data.res_day[2].data[0].sum,
                        data.res_day[1].data[0].sum,
                        data.res_day[0].data[0].sum
                    ]
                }
            ]
        };
        myChart2.setOption(option);
    })
})
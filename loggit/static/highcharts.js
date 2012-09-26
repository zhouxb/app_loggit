function chart(id,success_data,failure_data,total_data){
        
        var chart = new Highcharts.Chart({
            chart: {
                renderTo: id,
                width:800,
                type: 'spline',
                marginRight: 10
                /*events: {
                    load: function() {
    
                        // set up the updating of the chart each second
                        var series = this.series[0];
                        setInterval(function() {
                            var x = (new Date()).getTime(), // current time
                                y = Math.random();
                            series.addPoint([x, y], true, true);
                        }, 1000);
                    }
                }*/
            },
            title: {
                text: 'alarm'
            },
            xAxis: {
                type: 'datetime',
                tickPixelInterval: 150
            },
            yAxis: {
                title: {
                    text: 'Value'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function() {
                        
                        return '<b>'+ this.series.name +'</b><br/>'+
                        Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) +'<br/>'+

                        Highcharts.numberFormat(this.y, 0);
                }
            },
            legend: {
                enabled: false
            },
            exporting: {
                enabled: false
            },
            series: [{
                name: 'success',
                data:success_data
                /*data: (function() {
                    // generate an array of random data
                    var data = [],
                        time = (new Date()).getTime(),
                        i;
    
                    for (i = -19; i <= 0; i++) {
                        data.push({
                            x: time + i * 1000,
                            y: Math.random()
                        });
                    }
                    return data;
                })()*/
            },{
                name: 'failure',
                data:failure_data
                
            },{
                name: 'total',
                data:total_data
                
            }]
        });
    }

    function reload_height_chart(){
        starttime = $('#starttime').val()
        endtime = $('#endtime').val()
        $.getJSON('/loggit/api/domain/alarm?starttime='+starttime+'&endtime='+endtime, function(data) {
                        
            chart('alarm_content',data['success_data'],data['failure_data'],data['total_data'])
        });
    }
    $(document).ready(function() {
        
        Highcharts.setOptions({
            global: {
                useUTC: false
            }
        });
        
        reload_height_chart()
        
    });
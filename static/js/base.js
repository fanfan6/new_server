$(document).ready(function () {

    var nowURL = window.location.pathname;
    if(nowURL === '/report/search') {
        $(document).find('.UL2').hide();
        $(document).find(".table1").addClass('cur').siblings().removeClass('cur');
    }
    if(nowURL === '/report/service'){
        $(document).find('.UL2').hide();
        $(document).find(".table2").addClass('cur').siblings().removeClass('cur');
    }
    if(nowURL === '/report/history'){
        $(document).find('.UL2').hide();
        $(document).find(".table3").addClass('cur').siblings().removeClass('cur');
    }
    if(nowURL === '/count/search'){
        $(document).find(".table4").addClass('cur').siblings().removeClass('cur');
        $(document).find('.UL2').hide();
    }
    if(nowURL === '/statistics/index'){
        $(document).find(".table5").addClass('cur').siblings().removeClass('cur');
        $(document).find('.UL2').show();
    }

});

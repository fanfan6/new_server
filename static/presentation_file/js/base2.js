$(document).ready(function () {
    function savepdf() {
        var windowsHeigh = $(document.body).outerHeight(true);
        var windowsWidth = $(document.body).outerWidth(true);

        var pdf = new jsPDF('', 'pt', [windowsHeigh, windowsWidth]);
        pdf.internal.scaleFactor = 1;
        var options = {
            pagesplit: true
        };
        pdf.addHTML(document.body, options, function () {
            pdf.save('{{ user_info.name }}.pdf');
        });
    }

    $("#download").click(function () {
        savepdf();
        event.stopPropagation();
    })
}
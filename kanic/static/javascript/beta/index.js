$(document).ready(function() {
    $('#myModal').on('shown.bs.modal', function () {
        $('#id_name').focus()
    });

    if($('strong').length) {
        $('#myModal').modal('toggle');
    }

    if($('ul.messages').length) {
        $('ul.messages').fadeOut(10000, function() {

        });
    }
});

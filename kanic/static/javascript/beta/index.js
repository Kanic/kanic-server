$(document).ready(function() {
    // set min-height
    // $(".contentContainer").css("min-height",$(window).height());

    $('#myModal').on('shown.bs.modal', function () {
        $('#id_name').focus()
    });

    if($('#carOwner_invalid').length) {
        $('#CarOwnerModal').modal('toggle');
    }

    if($('#mechanic_invalid').length) {
        $('#MechanicModal').modal('toggle');
    }

    if($('ul.messages').length) {
        $('ul.messages').fadeOut(10000, function() {

        });
    }

    $('#submit').on('submit', function() {
        $('#submit').prop('disabled', true);
    });
});

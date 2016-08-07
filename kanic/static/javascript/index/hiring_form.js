$(function() {
    // render good file upload widget
    $(":file").filestyle({buttonName: "btn-primary"});

    // Disable submit button when form is submmiting
    $("#job-form").on('submit', function() {
        $('button.apply').prop('disabled', true);
    });
});

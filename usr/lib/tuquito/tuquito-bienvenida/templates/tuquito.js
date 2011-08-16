function changeTitle(title) {
    document.title = title;
    document.title = 'nop';
}
function closeWindow() {
    if (document.getElementById('showDialog').checked)
        changeTitle('event_close_true');
    else
        changeTitle('event_close_false');
}
function assessCheckbox() {
    if (document.getElementById('showDialog').checked)
        changeTitle('checkbox_checked');
    else
        changeTitle('checkbox_unchecked');
}
$(function() {
    cont = $('#com').html();
    $('#ajax').html(cont).fadeIn(1800);

    $('#showDialog').click(function() {
        assessCheckbox();
    });

    $('#closeButton').click(function() {
        closeWindow();
    });

    $('.boton').click(function() {
        data = $(this).data('cont');
        cont = $('#' + data).html();
        $('#ajax').hide().html(cont).fadeIn();
    });
});

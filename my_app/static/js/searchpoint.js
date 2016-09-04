$(document).ready(function(){
$("#form_searchpoint").bind("submit", function() {
if (!$("#id_pid").val())
{

return false;
}
$('<div id="my-dialog">Поиск...</div>').dialog({
    title: 'Карточка клиента',
    width: 1024,
    height: 768,
    modal: true,
    position: "top",
    open: function() {
    $.ajax({
    type: 'GET',
    cache: false,
    url: 'point_form?id='+$("#id_pid").val(),
    success: function(data){$('#my-dialog').html(data);}
    });
    setTimeout("$('#my-dialog').dialog('close')",300000);
    },
    close: function() {
    
    $('#my-dialog').remove();
        parent.location.reload(true);
    }
});
return false;

});

});

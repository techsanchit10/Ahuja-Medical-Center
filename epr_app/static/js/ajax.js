$(function(){

  $('#p_id').keyup(function() {

    $.ajax({
      type: "POST",
      url: "/epr_app/exist_eprsc",
      data: {
        'search_text': $('#p_id').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
      },
      success : searchSuccess,
      dataType : 'html'

    });
  });
});

function searchSuccess(data, textStatus, jqXHR)
{
  $('#p_id').html(data);
}

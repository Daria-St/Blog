$('#favoriteButton').click(function(e) {
    e.preventDefault();
    let baseUrl = 'http://127.0.0.1:8000/';
    $.ajax({
        type: 'GET',
        url: baseUrl + $(this).attr('href'),
        success: function(response) {
            $('#favoritesCount').text(response.favorites)
            $('#favoriteButton').hide()
            $('#unfavoriteButton').show()
            }

    })
})

$('#unfavoriteButton').click(function(e) {
    e.preventDefault();
    let baseUrl = 'http://127.0.0.1:8000/';
    $.ajax({
        type: 'GET',
        url: baseUrl + $(this).attr('href'),
        success: function(response) {
            $('#favoritesCount').text(response.likes)
            $('#favoriteButton').show()
            $('#unfavoriteButton').hide()
            }
    })
})

$('#feedbackForm').on('submit',function(e) {
    e.preventDefault();
    let baseUrl = 'http://127.0.0.1:8000/';

    $.ajax({
        type: 'POST',
        url: baseUrl + $(this).attr('action'),
        data: {
            name: $('#id_name').val(),
            text: $('#id_text').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(response) {
            $('.post-card').text('Обратная связь отправлена')
        },
        error: function(response){
            const errors = response.responseJSON.errors
            let err = ''

            for (let field in errors) {
                for (let error of errors[field]) {
                    err += '<p>' + error + '</p>'
                }
            }

            $('.formErrors').html(err)

        }
    })
})
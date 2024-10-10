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
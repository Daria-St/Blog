function loadComments(){
    let baseUrl = 'http://127.0.0.1:8000/';
    let postId = $('.container-post').data('post-id')

    $.ajax({
        type: 'GET',
        url: baseUrl + `/api/${postId}/comments`,
        success: function(response) {
            let comments = ''
            $.each(response.comments, function(index, comment) {
                comments += '<div class="comment">'
                comments += '<p class="comment-author">' + comment.profile + '</p>'
                comments += '<p class="comment-text">' + comment.text + '</p>'
                comments += '</div>'
            })

            $('.comments-section').html(comments);
        }
    })
}

$(document).ready(function(){
    loadComments();
})
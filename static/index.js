$(document).ready(function() {
    $('#form').on('submit',function(e) {
        $.ajax({
            data : {
                regex : $('#regex').val(),
                string : $('#string').val(),
            },
            type : 'POST',
            url : '/'
        })
        .done(function(data) {
            let output = '';
            if (data.matches.length > 0) {
                output += `<p>${data.matches.length} matches found.</p>`;
            }

            for (let match of data.matches) {
                output += `<li>${match}</li>`;
            }
            $('#formatted_matches').html(output).show();
        });
        e.preventDefault();
    });
});

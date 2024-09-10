$(document).ready(function() {
    $('#search').on('input', function() {
        let query = $(this).val();
        
        if (query.length >= 3) {  // Commence la recherche après 3 lettres
            $.ajax({
                url: "{% url 'liste_tickets' %}",
                data: {
                    'q': query,
                },
                dataType: 'json',
                success: function(data) {
                    $('#tickets-list').html(data.html);  // Mets à jour la liste des tickets
                }
            });
        }
    });
});
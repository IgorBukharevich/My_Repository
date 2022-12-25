$(document).ready(function() {
    let select_title_movie = $('#select_title_movie');
    let select_date_show = $('#select_date_show');
    let opt1 = localStorage.getItem('opt1')

    select_title_movie.change(function() {
        opt1 = $(this).val();
        localStorage.setItem('opt1', opt1);
        $('#price').html("");
        select_date_show.empty();
        select_date_show.append(`<option value="0">-Выбрать-</option>`);
        $.ajax({
            type: 'GET',
            url: 'api/date_shows/from_movie/' + opt1,
            success: function(response) {
                for (let i = 0; i < response.length; i++) {
                    let date_show_id = response[i].id;
                    let date_show = response[i].date_time_show;
                    let price_ticket = response[i].price_ticket;
                    select_date_show.append(`<option value="${date_show_id}">${date_show} Стоимость: ${price_ticket}</option>`);
                    console.log(response);
                }
            }
        });
    });

    select_title_movie.append(`<option value="0">-Выбрать-</option>`);
    select_date_show.append(`<option value="0">-Выбрать-</option>`);
    $.ajax({
        url:  'api/movies/',
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                let movie_id = response[i].id;
                let name_movie = response[i].title_movie;
                select_title_movie.append(`<option value="${movie_id}">${name_movie}</option>`);
            }
        }
    });
});

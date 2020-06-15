$(document).ready(function () {

    $('#bannerTitle').fadeIn(1000);

    // scroll Fade In
    $(window).scroll(function () {

        /* Check the location of each desired element */
        $('.hideme').each(function (i) {

            var bottom_of_object = $(this).offset().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();

            /* If the object is completely visible in the window, fade it it */
            if (bottom_of_window > bottom_of_object) {

                $(this).animate({'opacity': '1'}, 800);

            }

        });
    });

    $('.login-item').click(function() {
        $('.login-modal').modal('show');
    })

    $('.register-item').click(function() {
        $('.register-modal').modal('show');
    })

    $('#login').click(function() {
        var email = $('.login-email').val();
        var password = $('.login-password').val();

        $.ajax({
            url: './login',
            method: 'POST',
            dataType: 'JSON',
            data: {
                'email': email,
                'password': password
            },
            success: function(data) {
                if (data['success'] == 0) {
                    location.reload();
                } else {
                    alert(data['message']);
                }
            }
        })
    })

    $('#register').click(function() {
        var name = $('.register-name').val();
        var email = $('.register-email').val();
        var password = $('.register-password').val();

        $.ajax({
            url: './register',
            method: 'POST',
            dataType: 'JSON',
            data: {
                'name': name,
                'email': email,
                'password': password
            },
            success: function(data) {
                if (data['success'] == 0) {
                    location.reload();
                } else {
                    alert(data['message']);
                }
            }
        })
    })
});
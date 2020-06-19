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

    $('.add-item').click(function() {
        $('.add-modal').modal('show');
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
                    alert(data['message']);
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
                    alert(data['message']);
                    location.reload();
                } else {
                    alert(data['message']);
                }
            }
        })
    })

    $('#add-restaurant').click(function() {
        var type = $('.add-type').val();
        var name = $('.add-name').val();
        var address = $('.add-address').val();
        var time = $('.add-time').val();
        var phone = $('.add-phone').val();
        var image = $('.add-image').val();
        var website = $('.add-website').val();

        console.log(type)
        console.log(name)
        console.log(time)
        console.log(phone)
        console.log(image)
        console.log(website)
        $.ajax({
            url: './add',
            method: 'POST',
            dataType: 'JSON',
            data: {
                'type': type,
                'name': name,
                'address': address,
                'time': time,
                'phone': phone,
                'image': image,
                'website': website,
            },
            success: function(data) {
                if (data['success'] == 0) {
                    alert(data['message']);
                    location.reload();
                } else {
                    alert(data['message']);
                }
            }
        })
    })
});

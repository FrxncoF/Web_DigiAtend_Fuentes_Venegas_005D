window.addEventListener('load', function() {
    var cerrar_sesion = document.getElementById('deslogearse');
    cerrar_sesion.addEventListener('click', function() {
        var cookies_array = document.cookie.split(';');
        var cookies_dict = [];
        var csrftoken;
        cookies_array.forEach(elem => {
            var temp = elem.split('=');
            cookies_dict.push({
                key: temp[0],
                value: temp[1]
            });
        })
        cookies_dict.forEach(elem => {
            if(elem.key == 'csrftoken') {
                csrftoken = elem.value;
            }
        })
        $.ajax({
            type: 'POST',
            url: '/post/logout/',
            data: {csrfmiddlewaretoken: csrftoken},
            success: function() {
                setTimeout(function() {
                    location.reload();
                }, 500);
            },
            error: function() {
                alert('error');
            }
        })
    }, false);
}, false);
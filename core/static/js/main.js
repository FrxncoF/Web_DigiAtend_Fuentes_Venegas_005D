function genqr(e) {
    console.log(e.id);
    var id= e.id;
    $.get(`${window.location.origin}/api/${id}/`)
    .then(elem => {
        var codigo = elem.codigo;
        new QRious({
            element: $('#codigoqr')[0],
            value: codigo,
            size: 200,
            foreground: 'darkslateblue',
            level: 'H'
          });
    })
    .catch(error => {
        console.log('error: ' + error);
    });
}
// Validações do formulário de cadastro
(function () {
    'use strict';
    window.addEventListener('load', function () {
        // Get the forms we want to add validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

// Máscara telefone
$(document).ready(function () {
    $('#tel').mask('(00)00000-0000');
});

// Máscara cep
$(document).ready(function () {
    $('#cep').mask('00000-000');
});

// Consumindo a API ViaCEP
$(document).ready(function () {
    $('#getCep').click(function () {
        event.preventDefault();
        let cep = $("#cep").val();
        let urlViaCep = `https://viacep.com.br/ws/${cep}/json`;
        $.ajax({
            url: urlViaCep,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $('#rua').val(data.logradouro);
                $('#bairro').val(data.bairro);
                $('#cidade').val(data.localidade);
                $('#uf').val(data.uf);
                if (data.logradouro != undefined) {
                    address = `${data.logradouro.replace(' ', '+')},${data.bairro.replace(' ', '+')},${data.localidade.replace(' ', '+')},${data.uf}`;
                    zoom = 20;
                } else {
                    address = `${localizacao.lat},${localizacao.lng}`;
                    zoom = 3;
                }
            }
        });

        setTimeout(function () {
            const key = 'AIzaSyBFrXEyEmLX2yvAE5-LyfFfLPe4ASfSK6I';
            let urlGMaps = `https://maps.googleapis.com/maps/api/geocode/json?address=${address}&key=${key}`;
            $.ajax({
                url: urlGMaps,
                type: 'get',
                dataType: 'json',
                success: function (data) {
                    $('#pais').val(data.results[0].address_components[4].long_name);
                    localizacao.lat = Number(data.results[0].geometry.location.lat);
                    localizacao.lng = Number(data.results[0].geometry.location.lng);
                    initMap();
                }
            });
        }, 1000)
    });
});

// Google Maps
let map;
let address;
let localizacao = { lat: -13.6561589, lng: -69.7309264 }
let zoom = 3;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: localizacao,
        zoom: zoom,
    });
};
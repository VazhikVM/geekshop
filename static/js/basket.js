// window.onload = function(){
//     $('.basket_list').on('click', 'inpyt[type=number]', function(){
//         var t_href = event.target;
//
//         $.ajax({
//             url: '/basket/edit/' + t_href.name + '/' + t_href.value + '/',
//
//             success: function(data) {
//                 $('.basket_list').html(data.result)
//             }
//         })
//         return false;
//     });
// };
window.onload = function () {
    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });

    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });

    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */

    // добавляем ajax-обработчик для обновления количества товара
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var target_href = event.target;

        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

}
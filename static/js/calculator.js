document.addEventListener('DOMContentLoaded', function () {
    console.log('coś tam');

   var count_button = document.querySelector('#count');
   var count_area = document.querySelector('#count_area');

   function amount(event) {
        var wind_h = document.querySelector('#id_window_height');
        var wind_w = document.querySelector('#id_window_weight');
        var area = document.querySelector('#id_slot_area');
        console.log(area.value);

        var result = parseInt(area.value) + wind_w.value * wind_h.value;
        result = Math.round(result, 2);


        return area.value = result
   }

   function amount_2(event) {
        var lenght = document.querySelector('#id_lenght');
        var weight = document.querySelector('#id_weight');
        var floor_area = document.querySelector('#id_floor_area');
        console.log(floor_area.value);

        var result = parseInt(floor_area.value) + weight.value * lenght.value;
        result = Math.round(result, 2);


        return floor_area.value = result
   }

    count_button.addEventListener('click', amount);
    count_area.addEventListener('click', amount_2);
});

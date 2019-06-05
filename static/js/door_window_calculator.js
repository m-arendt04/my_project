document.addEventListener('DOMContentLoaded', function () {
    console.log('coś tam');

   var count_button = document.querySelector('#count');
   
   function amount(event) {
        var wind_h = document.querySelector('#id_window_height');
        var wind_w = document.querySelector('#id_window_weight');
        var area = document.querySelector('#id_slot_area');
        console.log(area.value);

        var result = parseInt(area.value) + wind_w.value * wind_h.value;
        result = Math.round(result, 2);


        return area.value = result
   }

   count_button.addEventListener('click', amount)
});

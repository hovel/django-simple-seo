;(function ($) {
    'use strict';

    $(function () {
        var $input_list = $('input[type="text"]');
        $input_list.each(function () {
            var $input = $(this);
            $input.after(' <span class="length">' + $input.val().length + '</span>')
        });

        $input_list.on('keyup', function () {
            var $input = $(this);
            $input.next('.length').text($input.val().length);
        })
    });
})(jQuery || django.jQuery)

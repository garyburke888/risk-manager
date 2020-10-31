  $(document).ready(function(){
    $(".sidenav").sidenav();
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});
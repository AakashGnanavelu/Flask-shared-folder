var previous = null;
var current = null;
setInterval(
    function() {
    $.getJSON("/data_json", function(json) {
        current = JSON.stringify(json);
        console.log("Data Recieved")
        if (previous && current && previous !== current) {
            console.log('refresh');
            location.reload();
        }
        previous = current;
    });                       
}, 2000);   
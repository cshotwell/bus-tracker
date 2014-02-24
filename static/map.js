function initialize() {
    var myLatlng = new google.maps.LatLng(39.4053947,-95.363801);
    var mapOptions = {
        zoom: 5,
        center: myLatlng
    }
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    var carl = new google.maps.Marker({
        name: "Carl!",
        position: new google.maps.LatLng(41.489067,-81.7831769),
        map: map,
    });

    var jordan = new google.maps.Marker({
        name: "Jordan!",
        position: new google.maps.LatLng(40.6281346,-74.0008018),
        map: map,
    });

    var infowindow = function(marker) {
        return new google.maps.InfoWindow({
            content: marker.name,
        });
    };

    google.maps.event.addListener(jordan, 'click', function() {
        infowindow(jordan).open(map,jordan);
    });
    google.maps.event.addListener(carl, 'click', function() {
        infowindow(carl).open(map,carl);
    });

}

google.maps.event.addDomListener(window, 'load', initialize);


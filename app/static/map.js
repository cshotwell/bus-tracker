google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {
    var myLatlng = new google.maps.LatLng(39.4053947,-95.363801);
    var mapOptions = {
        zoom: 4,
        center: myLatlng
    }
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    var infowindow = new google.maps.InfoWindow({
            content: 'loading',
            load_content: function(marker, id){
                $.ajax({
                    url: "https://api.twitter.com/1/statuses/oembed.json?id=" + marker.tweet_id + "&omit_script=true&hide_media=true&hide_thread=true",
                    crossDomain: true,
                    dataType: 'jsonp',
                    success: function(data){
                        infowindow.setContent(data.html);
                        infowindow.open(map, marker);
                        twttr.widgets.load();
                    }
                })
            }
    });

    var points = []
    var cities = []
    addBusMarkers();

    function fetch_bus_icon(bus) {
        var marker;
        switch(bus) {
            case "South":
                marker = "https://maps.gstatic.com/mapfiles/ms2/micons/blue-dot.png";
                break;
            case "Mexico":
                marker = "https://maps.gstatic.com/mapfiles/ms2/micons/red-dot.png";
                break;
            case "Midwest":
                marker = "static/images/Carl_pin_blue.png";
                break;
            case "WestCoast":
                marker = "https://maps.gstatic.com/mapfiles/ms2/micons/ltblue-dot.png";
                break;
            case "Southeast":
                marker = "static/images/Carl_pin_OJ.png";
                break;
            case "North":
                marker = "https://maps.gstatic.com/mapfiles/ms2/micons/purple-dot.png";
                break;
            case "Northeast":
                marker = "https://maps.gstatic.com/mapfiles/ms2/micons/pink-dot.png";
                break;
            default:
                marker = "http://labs.google.com/ridefinder/images/mm_20_black.png";
                break;
        }
        return marker;
    }

    $(document).ready(function(){ 
        $.ajax({
            url: "/users", 
            success: function(data){
                _.each(data.user_list, function(user){

                    points = _.map(user.tweets, function(tweet){
                        var new_marker = new google.maps.Marker({
                            position: new google.maps.LatLng(parseFloat(tweet.lat), parseFloat(tweet.lon)), 
                            map: map, 
                            name: tweet.body,
                            tweet_id: tweet.tweet_id,
                            icon: fetch_bus_icon(user.bus)
                        });

                        google.maps.event.addListener(new_marker, 'click', function() {
                            infowindow.close();
                            infowindow.load_content(new_marker, tweet.tweet_id);
                        });

                        return new_marker
                    });

                });
            }
        });
    }); //document.ready

    function addBusMarkers() {
        starting_cities = [[39.079152,-94.5929357], //KC
                [40.7277495,-73.9924231], //NYC
                [20.6598988,-103.351442], //MEX
                [47.6058384,-122.3317757], //SEA
                [37.7682851,-122.4205412], //SFO
                [27.9420771,-82.4707102], //tam
                [36.1656477,-86.781603]];

        cities = _.map(starting_cities, function(city) {
            var new_city = new google.maps.Marker({
                position: new google.maps.LatLng(city[0],city[1]), 
                map: map, 
                icon: "http://maps.google.com/mapfiles/ms/micons/bus.png"
            });
        });
    }

}


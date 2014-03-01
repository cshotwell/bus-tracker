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
//marker for carl
    var carl_marker = new google.maps.Marker({
        position: new google.maps.LatLng(41.5010421,-81.6942719),
        map: map,
        icon: "http://google-maps-icons.googlecode.com/files/rattlesnake.png"
    });

    cities.push(carl_marker);

    google.maps.event.addListener(carl_marker, 'click', function() {
        $('#AboutMeModal').modal('show')
    });
//end marker for carl

    function fetch_bus_icon(bus) {
        var marker;
        switch(bus) {
            case "South":
                marker = "static/images/Carl_pin_OJ_3.png";
                break;
            case "Mexico":
                marker = "static/images/Carl_pin_blue_3.png";
                break;
            case "Midwest":
                marker = "static/images/Carl_pin_red_3.png";
                break;
            case "WestCoast":
                marker = "static/images/Carl_pin_pink_3.png";
                break;
            case "Southeast":
                marker = "static/images/Carl_pin_purp_3.png";
                break;
            case "North":
                marker = "static/images/Carl_pin_green_3.png";
                break;
            case "Northeast":
                marker = "static/images/Carl_pin_yel_3.png";
                break;
            default:
                marker = "static/images/Carl_pin_ugh_3.png";
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


google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {
    var myLatlng = new google.maps.LatLng(39.4053947,-95.363801);
    var mapOptions = {
        zoom: 5,
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
                            tweet_id: tweet.tweet_id
                        });

                        google.maps.event.addListener(new_marker, 'click', function() {
                            infowindow.close();
                            infowindow.load_content(new_marker, tweet.tweet_id);
                            //infowindow(new_marker).open(map,new_marker);
                        });

                        return new_marker
                    });

                });
            }
        });
    });
}


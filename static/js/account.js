$.get("http://23.97.142.158/authorisation",
    { "link": "http://23.97.142.158" },
    function (result) {
        $("#login").attr("href", result);
    }
);

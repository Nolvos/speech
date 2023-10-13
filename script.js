$(document).ready(function() {
    console.log("Script loaded!");  // Add this line to verify script execution

    // Fetch stories from the server
    $.get("/api/stories", function(data) {
        data.forEach(story => {
            $("#story-list").append("<li>" + story + "</li>");
        });
    });
});

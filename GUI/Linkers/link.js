let { PythonShell } = require("python-shell");
var path = require("path");

function getLinks() {
    var link = document.getElementById("link").value
    // alert(link);

    var options = {
        scriptPath: path.join(__dirname, '/../engine/'),
        args : [link]
    }
    
    alert(link);
    var downloader = new PythonShell("youtube.py", options);
    
    downloader.on('message', (message) => {
        swal(message);
    })
}
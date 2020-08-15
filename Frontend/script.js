// async function getLinks() {
// 	alert("clicked");
// 	var n = await eel.alert_value("hii")();
// 	alert(n);
// }
eel.expose(progress);
function progress(current_progress) {
	// var current_progress = 0;
	console.log(current_progress);
	// current_progress = current_progress + h;
	$("#dynamic")
		.css("width", current_progress + "%")
		.attr("aria-valuenow", current_progress)
		.text(current_progress + "% Complete");
	// var interval = setInterval(function () {
	// 	current_progress += 1;
	// 	$("#dynamic")
	// 		.css("width", current_progress + "%")
	// 		.attr("aria-valuenow", current_progress)
	// 		.text(current_progress + "% Complete");
	// 	if (current_progress >= 100) clearInterval(interval);
	// }, 100);
}

// eel.expose(getLinks);
function getLinks() {
    return $("#link").alert_value;
}

async function callpython() {

	var a = $("#link").val();
	$("#progress-div").show();
	// alert(a);
    await eel.start_video(a)();
}

eel.expose(streams_log);
function streams_log(streams) {
	// alert("jiii");
	streams_arr = streams.split(",");
	console.log(streams_arr);
	// t = "";
	streams_arr.forEach(x => {
		// t = t + x + "99999999999999</br>";
		// console.log(x);
		// var theDiv = document.getElementById("stream");
		// var content = document.createTextNode(x);
		// theDiv.appendChild(content);
		ul = document.getElementById("stream");
		var li = document.createElement("li");
		var text = document.createTextNode(x);
		li.appendChild(text);
		ul.appendChild(li);
		// $("#stream").text(x);

		// $("#stream").append("<br");
	});

	// $("p").append(t);
	// console.log(typeof streams);
}

function poll() {
	$.get("http://23.97.142.158/new_payment",
		{"user_id": "user1"},
		function (result) {
			if (result != "no") {
				$('#exampleModal').modal('toggle')
			}
			else {
				window.setTimeout(poll, 3000);
			}

		}
	);
}
window.setTimeout(poll, 3000);

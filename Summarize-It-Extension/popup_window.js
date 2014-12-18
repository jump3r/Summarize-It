

chrome.runtime.onMessage.addListener(
	function(req, sender, sendResponse) {

		if (req.summarized_text) {
			
			var text = req.summarized_text;
			console.log(text);
			$('#text-summary')[0].innerHTML = text;
			/*
			$('input[name="title"]').val(details.title);
			$('input[name="url"]').val(details.url);
			$('input[name="page_url"]').val(details.pageUrl);
			$('input[name="id"]').val(details.id);
			$('input[name="anchor"]').val(details.text);
			$('input[name="editable"]').val(details.editable);
			*/
		}
	}
);
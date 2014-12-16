
/*
Example info

info: {
"editable":false,
"menuItemId":"context:selection",
"pageUrl":"https://www.google.ca/search?q=wassily+kandinsky+famous+paintings&hl=en&biw…bih=697&source=lnms&sa=X&ei=GNWPVLnAJpOYyQTXxIKADA&ved=0CAUQ_AUoAA&dpr=1.1",
"selectionText":"esionistic landscape, which already marked the slow transition into abstraction. Wassily Ka"
}

tab: {
"active":true,
"favIconUrl":"https://www.google.ca/favicon.ico",
"height":767,
"highlighted":true,
"id":313,
"incognito":false,
"index":7,
"openerTabId":307,
"pinned":false,
"selected":true,
"status":"complete",
"title":"wassily kandinsky famous paintings - Google Search",
"url":"https://www.google.ca/search?q=wassily+kandinsky+famous+paintings&hl=en&biw…bih=697&source=lnms&sa=X&ei=GNWPVLnAJpOYyQTXxIKADA&ved=0CAUQ_AUoAA&dpr=1.1",
"width":1600,
"windowId":1}

*/
function onClickHandler(info, tab) {
  if (info.menuItemId == "user-context-selection") {        
		//console.log(info.selectionText);
		console.log(info["selectionText"]);
		var xml_http = new XMLHttpRequest();
		xml_http.onreadystatechange=function() {

			if (xml_http.readyState==4 && xml_http.status==200)
			{			
				console.log(xml_http.responseText);
				alert(xml_http.responseText);
			}
		}
		xml_http.open("POST","http://localhost:5000/Query",true);
		xml_http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		xml_http.send("query_text="+ info["selectionText"] + "&query_uri=" + info["pageUrl"]);
  }

};

chrome.runtime.onInstalled.addListener(function() {

  chrome.contextMenus.create({"title": "Summarize it!", "contexts":["selection"], "id": "user-context-selection"});
  chrome.contextMenus.create({"title": "Select Text To Summarize it!", "id": "NoSelection"});

});

chrome.contextMenus.onClicked.addListener(onClickHandler);

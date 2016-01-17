var getInfo = function() { 	
	callWikipediaAPI("Kanye West", 0);
	callWikipediaAPI("Kanye West", 1);
	callWikipediaAPI("Kanye West", 2);
	callWikipediaAPI("Kanye West", 3);
	callWikipediaAPI("Kanye West", 4);
	callWikipediaAPI("Kanye West", 5);
	callWikipediaAPI("Kanye West", 6);
	callWikipediaAPI("Kanye West", 7);
	callWikipediaAPI("Kanye West", 8);
	callWikipediaAPI("Kanye West", 9);
};

function callWikipediaAPI(wikipediaPage, idNum) {
	// http://www.mediawiki.org/wiki/API:Parsing_wikitext#parse
    var jsonObject = $.getJSON('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=Kanye%20West&callback=?').done(function(data) {
    	var pageId = getPageId(data.query.pages);
    	var extractString = data.query.pages[pageId]["extract"];
    	// console.log(extractString);
    	// console.log(JSON.stringify(data.query.pages.523032));
    	$("#wikiText" + idNum).text(extractString.substring(0, extractString.indexOf(". ") + 1));
    })
};

var getPageId = function(jsObj) {
	for (var pageid in jsObj) {
		return pageid;
	}
};

//creates each card div.
var createCardDivs = function() {
    for (var i=0; i < 10; i++) {
    	var $newDiv = $("<div/>")   // creates a div element
                 .attr("id", "someID" + i)  // adds the id
                 .addClass("card row")   // add a class
    	$("#options").append($newDiv.clone());
    };
    createImage();
};

//creates the image portion of each card
var createImage = function() {
	for (var i = 0; i < 10; i++) {
		var $newDiv = $("<div/>")   // creates a div element
                 // .attr("id", "someID")  // adds the id
                 .addClass("col-md-1 text-left")   // add a class
                 .html('<img src="http://placehold.it/150x150" class="picture">');
        $("#someID" + i).append($newDiv.clone());
	};
	createName();
};

//creates the name portion of each card
var createName = function() {
	for (var i = 0; i < 10; i++) {
		var $newDiv = $("<div/>")   // creates a div element
	                 // .attr("id", "someID")  // adds the id
	                 .addClass("col-md-2 text-left info")   // add a class
	                 .html('<p class="name"> Kanye <br> West </p>');
	    $("#someID" + i).append($newDiv.clone());
	};
	createWiki();
}; 

//creates the wiki portion for each card
var createWiki = function() {
	for (var i = 0; i < 10; i++) {
	var $wikiText = "wikiText" + i;
	var $newDiv = $("<div/>")   // creates a div element
	                 // .attr("id", "someID")  // adds the id
	                 .addClass("col-md-5 text-center info wiki")   // add a class
	                 .html("<p id =" + $wikiText + "></p>");
	$("#someID" + i).append($newDiv.clone());
	};
	createWorth();
}

var createWorth = function() {
	for (var i = 0; i < 10; i++) {
		var $newDiv = $("<div/>")   // creates a div element
		                 // .attr("id", "someID")  // adds the id
		                 .addClass("col-md-2 stats circle-singleline")   // add a class
		                 .html("Hello");
	    $("#someID" + i).append($newDiv.clone());
	};
	createDirection();
};

var createDirection = function() {
	for (var i = 0; i < 10; i++) {
		var $newDiv = $("<div/>")   // creates a div element
		                 // .attr("id", "someID")  // adds the id
		                 .addClass("col-md-2 stats circle-singleline glyphicon")   // add a class
		                 .html('<span class="fa fa-caret-up fa-4x" aria-hidden="true"> </span> ');
	    $("#someID" + i).append($newDiv.clone());
	};
}

createCardDivs();
getInfo();

var cardImage = new Array(); 
cardImage[0] = "Images/pudding.png";
cardImage[1] = "Images/dumpling.png";
cardImage[2] = "Images/1_maki_roll.png";
cardImage[3] = "Images/2_maki_roll.png";
cardImage[4] = "Images/3_maki_roll.png";
cardImage[5] = "Images/pudding.png";
cardImage[6] = "Images/sashimi.png";
cardImage[7] = "Images/tempura.png";
cardImage[8] = "Images/wasabi.png";
cardImage[9] = "Images/egg_nigiri.png";
cardImage[10] = "Images/salmon_nigiri.png";
cardImage[11] = "Images/squid_nigiri.png";


//Yates shuffle to randomize cards
function shuffle(cardImage) {
    for (let i = cardImage.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [cardImage[i], cardImage[j]] = [cardImage[j], cardImage[i]];
    }
    return cardImage;
}

function displayHand() {
    var i = 0;
    //Make len equal to the number of unique cards (12) minus 5 (7)		
    len = shuffle(cardImage).length-5; 
    
	
    for (; i < len; i++) {
        var img = document.createElement("img");
        const img2 = document.createElement("img");
        const span = document.createElement('span');
        
        img.className = "card-image";
        img.src = cardImage[i];
        img.style.width = '80px';
        img.style.height = '100px'; 
        img.style.paddingRight='25px';  
        img.id = cardImage[i];
        img.style.zIndex = i;
        
        //Create tooltip image for cards
        img2.className = "tooltip";
        img2.src = cardImage[i];
        img2.id = cardImage[i];

        //Container for the image
        span.className = 'image-wrapper';
        //Set draging event on the image container
        span.setAttribute("ondragstart","drag(event)");
        span.setAttribute("ondragend","hideTooltip();");
        span.draggable="true";
        //Set id of the container related to the card image
        span.id = "span-" + cardImage[i];
        //Apend images to container
        span.appendChild(img);
        span.appendChild(img2);

        document.getElementById('images').appendChild(span);
    }

};



$(function() {
    displayHand();

    //Beginning of the submit button logic
    const submitButton = document.getElementById("submit");

    submitButton.addEventListener('click', function () {
        var $lastImage = $("li.flex-item .image-wrapper:last-child");
        $lastImage.addClass("submited-card").removeClass("staged");

        //TO DELETE START
        var randomNum2 = Math.floor(Math.random() * cardImage.length);
        var randomNum3 = Math.floor(Math.random() * cardImage.length);
        var randomNum4 = Math.floor(Math.random() * cardImage.length);
        
        var elem2 = document.createElement("img");
        var elem3 = document.createElement("img");
        var elem4 = document.createElement("img");
        var play2 = document.getElementById("p2");
        var play3 = document.getElementById("p3");
        var play4 = document.getElementById("p4");

        elem2.setAttribute("src", cardImage[randomNum2]);
        elem2.setAttribute("height", "100px");
        elem2.setAttribute("width", "80px");
        elem2.setAttribute("padding", "25px");
        elem3.setAttribute("src", cardImage[randomNum3]);
        elem3.setAttribute("height", "100px");
        elem3.setAttribute("width", "80px");
        elem3.setAttribute("padding", "25px");
        elem4.setAttribute("src", cardImage[randomNum4]);
        elem4.setAttribute("height", "100px");
        elem4.setAttribute("width", "80px");
        elem4.setAttribute("padding", "25px");
        play2.appendChild(elem2);
        play3.appendChild(elem3);
        play4.appendChild(elem4);

        function deleteImages () {   
            var im = 0;
            for (; im < 10; im++) {
                i = 2;
                play2.removeChild(play2.childNodes[i]);
                play3.removeChild(play3.childNodes[i]);
                play4.removeChild(play4.childNodes[i]);
                i += 1;
            }
        };
        //TO DELETE END

        //End of the round if 7 cards are placed
        if ($(".submited-card").length == 7) {

            displayHand();


            //Clear the board
            $(".player1 .submited-card").remove();
			$(".player2 .submited-card").remove();
			$(".player3 .submited-card").remove();
            $(".player4 .submited-card").remove();
            

            //End of round dialog
            $("#modal-wrapper").removeClass("hidden");

            //TO DELETE START
            deleteImages();
            //TO DELETE END
        };
    });

    //Close the dialog and continue next round
    $("#continue").on("click", function (){
        $("#modal-wrapper").addClass("hidden");
    });
});

//Prepare target for dropping
function allowDrop(ev) {
    ev.preventDefault();
}

//Execute on target dragstart
function drag(ev) {
    var $tooltip = $(".tooltip");

    //Hide opened tooltip to not colide with dragging
    $tooltip.addClass("hidden");

    //Drag created wrapper span not only the image
    var item = "span-" + ev.target.id;

    ev.dataTransfer.setData("text/html", item);
}

//Execute on drop
function drop(ev) {
    ev.preventDefault();

    var data = ev.dataTransfer.getData("text/html");
    
    var $target;

    //If dropped on container set target to it
    if($(ev.target).hasClass("drag-container")) {
        $target = ev.target;
    }
    //If dropped to inner element and not actual container
    //set target to container containing the inner element
    else {
        $target = $(ev.target).closest(".drag-container");
    }

    try {
    //Check if card is dropped to the board and not the hand
    isBoard = $($target).parent().attr('id') == "board" ? true : false;
    
    //If card is dropped on the board stage it for submission
    if (isBoard) {
        $staged = $(".staged");

        //If there is already one card staged and not sumbitted yet
        //return that card back to hand
        if ($staged.length) {
            let id = $staged.attr("id");
            $("#images").append(document.getElementById(id));
        }
    }

    //Drop card
    $target.append(document.getElementById(data));

        //If it's dropped to the board, stage the card for submission
        if(isBoard) {
            $(document.getElementById(data)).addClass("staged");
        }
        //If it's dropped from board to hand, unstage the card
        else {
            $(document.getElementById(data)).removeClass("staged");
        }
    }
    catch(err) {
        console.log(err.message);
    }
}

function hideTooltip() {
    var $tooltip = $(".tooltip");

    $tooltip.removeClass("hidden");
}
//Method for taking in JSON object and converting it to javascript array
function convertFromJson()
{
    var JSONstring='{ "cardID1": ["cardType1", "isTagged1"], "cardID2": ["cardType2", "isTagged2"] }'
    object = JSON.parse(JSONstring), //reads in the JSON
    array = Object.keys(object).map(function(k) 
	{
	 //Returns JSON as key:value pair
        return object[k];
    });
	
	//Traverse the card array
	for (var key in array) 
	{
		let value = array[key];
		//Print  array
		console.log(value);
		//Print specific value from an array
		console.log(value.label);
		//var cards = new Card(value.name,value.type,value.ID, value.isTagged);
		//newCardArray.push(cards);
	}

}
//Method for taking in javascript array and converting it to JSON string
function convertToJson(jarray)
{
	return JSON.stringify(jarray);
	console.log(jarray);
}

//After converting JSON objects use this class to create Javascript card objects
function Card(type, name, ID, isTagged) {
    var classname = 'Card';
    this.type = type;
    this.name = name;
	this.ID=ID;
	isTagged=false;
   
}

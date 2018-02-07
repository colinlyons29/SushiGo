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


//yates shuffle to randomize cards
function shuffle(cardImage) {
    for (let i = cardImage.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [cardImage[i], cardImage[j]] = [cardImage[j], cardImage[i]];
    }
    return cardImage;
}

function displayHand() {
    var i = 0,		
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
        
        //create tooltip image for cards
        img2.className = "tooltip";
        img2.src = cardImage[i];
        img2.id = cardImage[i];

        //container for the image
        span.className = 'image-wrapper';
        //set draging event on the image container
        span.setAttribute("ondragstart","drag(event)");
        span.setAttribute("ondragend","hideTooltip();");
        span.draggable="true";
        //set id of the container related to the card image
        span.id = "span-" + cardImage[i];
        //apend images to container
        span.appendChild(img);
        span.appendChild(img2);

        document.getElementById('images').appendChild(span);
    }

};

$(function() {
    displayHand();

    //Begining of the submit button logic
    const submitButton = document.getElementById("submit");

    submitButton.addEventListener('click', function () {
        var $lastImage = $("li.flex-item .image-wrapper:last-child");
        $lastImage.addClass("submited-card").removeClass("staged");

        //End of the round if 7 cards are placed
        if ($(".submited-card").length == 7) {

            displayHand();

            //Clear the board
            $(".player1 .submited-card").remove();

            //End of round dialog
            $("#modal-wrapper").removeClass("hidden");
        };
    });

    //Close the dialog and continue next round
    $("#continue").on("click", function (){
        $("#modal-wrapper").addClass("hidden");
    });
});

//Prepare target for droping
function allowDrop(ev) {
    ev.preventDefault();
}

//Execute on target dragstart
function drag(ev) {
    var $tooltip = $(".tooltip");

    //Hide opened tooltip to not colide with draging
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

    //if droped on container set target to it
    if($(ev.target).hasClass("drag-container")) {
        $target = ev.target;
    }
    //if droped to inner element and not actuall container
    //set target to container containing the inner element
    else {
        $target = $(ev.target).closest(".drag-container");
    }

    try {
    //check if card is droped to the board and not the hand
    isBoard = $($target).parent().attr('id') == "board" ? true : false;
    
    //if card is droped on the board stage it for submition
    if (isBoard) {
        $staged = $(".staged");

        //if there is already one card staged and not sumbited yet
        //return that card back to hand
        if ($staged.length) {
            let id = $staged.attr("id");
            $("#images").append(document.getElementById(id));
        }
    }

    //drop card
    $target.append(document.getElementById(data));

        //if it's droped to the borad, stage the card for submition
        if(isBoard) {
            $(document.getElementById(data)).addClass("staged");
        }
        //if it's droped from board to hand, unstage the card
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

var cardImage = new Array(); 
cardImage[0] = "images/chopsticks.jpg";
cardImage[1] = "images/dumpling.jpg";
cardImage[2] = "images/maki1.jpg";
cardImage[3] = "images/maki2.jpg";
cardImage[4] = "images/maki3.jpg";
cardImage[5] = "images/pudding.jpg";
cardImage[6] = "images/sashimi.jpg";
cardImage[7] = "images/tempura.jpg";
cardImage[8] = "images/wasabi.jpg";
cardImage[9] = "images/eggnigiri.jpg";
cardImage[10] = "images/salmonnigiri.jpg";
cardImage[11] = "images/squidnigiri.jpg";



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
        img.src = cardImage[i];
        img.style.width = '80px';
        img.style.height = '100px'; 
		img.style.paddingRight='25px';	
		img.id = cardImage[i];
        document.getElementById('images').appendChild(img);
		img.onmouseover = function(){
        
      }
	   img.onmouseout = function(){
       
      }
    }
	
};

$(function() {
    displayHand();   
});

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("img", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("img");
    ev.target.appendChild(document.getElementById(data));
}

var circle = document.getElementById("cirlce");
var upBtn = document.getElementById("upbutton");
var DwnBtn = document.getElementById("DwnBtn");

var rotateValue = circle.style.transform;
var rotateSum;

upBtn.onclick = function(){
    rotateSum = rotateValue + "rotate(-90deg)";
    circle.style.transform = rotateSum;
    rotateValue = rotateSum;
}

DwnBtn.onclick = function(){
    rotateSum = rotateValue + "rotate(90deg)";
    circle.style.transform = rotateSum;
    rotateValue = rotateSum;
}

document.write("No");


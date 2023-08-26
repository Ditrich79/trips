'use strict';


let viewport = document.getElementById("viewport").offsetWidth;
let btnNext = document.getElementById("next");
let btnPrev = document.getElementById("prev");
let slider = document.querySelector("div.slider");
let viewSliders = document.querySelectorAll(".viewSlide");
let viewSlide = 0;
 
viewSliders[0].style.backgroundColor = "green";
 
btnNext.addEventListener("click", function () {
    viewSliders[viewSlide].style.backgroundColor = "red";
    if (viewSlide < 4) { 
        viewSlide++;
    } 
    else { 
        viewSlide = 0;
    }
    viewSliders[viewSlide].style.backgroundColor = "green";
    slider.style.left = -viewSlide * viewport + "px";
});
 
btnPrev.addEventListener("click", function () {
    viewSliders[viewSlide].style.backgroundColor = "red";
    if (viewSlide > 0) { 
        viewSlide--; 
    } 
    else { 
        viewSlide = 4; 
    }
    viewSliders[viewSlide].style.backgroundColor = "green";
    slider.style.left = -viewSlide * viewport + "px";
});


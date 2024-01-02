var menu = document.querySelector(".menu-icon")
var hummber = document.querySelector(".menu")

menu.addEventListener("click", function(){
    if ("hidden" in hummber.classList){
        hummber.classList.toggle("opacity-100");
    }else{
        hummber.classList.toggle("opacity-0");
    }
    
})

var kicon = document.querySelector(".kicon");
var kmenu = document.querySelector(".kmenu");

kicon.addEventListener("click", function(){
    if ("hidden" in kmenu.classList){
        kmenu.classList.toggle("opacity-100");
    }else{
        kmenu.classList.toggle("opacity-0");
    }
    
})
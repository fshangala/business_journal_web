document.addEventListener("DOMContentLoaded", function(){
    var dropdowns = document.querySelectorAll(".dropdown-menu");
    for (var i = 0; i < dropdowns.length; i++) {
        var dropdownButton = dropdowns[i].querySelector(".dropdown-menu-button");
        var dropdown = dropdowns[i].querySelector(".dropdown-menu-content");

        dropdownButton.addEventListener("click",(e)=>{
            dropdown.classList.toggle("hidden");
        });
    }
});

document.addEventListener("click", function(event){
    if (!event.target.classList.contains("dropdown-menu-button")) {
        var dropdowns = document.querySelectorAll(".dropdown-menu .dropdown-menu-content");
        for (var i = 0; i < dropdowns.length; i++) {
            dropdowns[i].classList.add("hidden");
        }
    }
});
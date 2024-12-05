var button = document.getElementById("BtnIniSesion");
var content = document.getElementById("FormSesion");

button.addEventListener("click", function() {
    if (content.style.display === "none") {
    content.style.display = "block";
    } else {
    content.style.display = "none";
    }
    });
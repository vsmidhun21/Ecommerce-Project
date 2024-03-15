var closeicon = document.getElementById("closeicon")
var signup = document.querySelector(".signup")
closeicon.addEventListener('click', () => {
    signup.style.display = "none"
})

var menubar = document.getElementById("menubar")
var sidemenu = document.querySelector(".sidemenu")

var sidemenu__closebar = document.getElementById("sidemenu__closebar")

menubar.addEventListener('click', () => {
    sidemenu.style.right = 0
})

sidemenu__closebar.addEventListener('click', () => {
    sidemenu.style.right = "-50%"
})


var tags = document.getElementsByName("tags");
var products = document.querySelectorAll(".products");

for (let i = 0; i < tags.length; i++) {
    tags[i].addEventListener("click", () => {
        if (tags[i].checked) {
            var tagString = tags[i].value.toLowerCase();

            for (let j = 0; j < products.length; j++) {
                var productName = products[j].querySelector("h1").textContent.toLowerCase();
                if (!productName.includes(tagString)) {
                    products[j].style.display = "none";
                } else {
                    products[j].style.display = "block";
                }
            }
        } else {
            for (let j = 0; j < products.length; j++) {
                products[j].style.display = "block";
            }
        }
    });
}


var product = document.querySelectorAll(".products")
var search_input = document.getElementById("search-input")
var products_container = document.querySelectorAll(".product_container")
var closeIcon = document.getElementById("filter_close_icon");


search_input.addEventListener('keyup', function (event) {
    if (search_input.value.trim() !== "") {
        closeIcon.style.display = "inline-block";
    } else {
        closeIcon.style.display = "none";
    }
    var enteredvalue = event.target.value.toLowerCase();
    for (var i = 0; i < product.length; i++) {
        var products = product[i].querySelector("h1").textContent.toLowerCase();

        if (products.includes(enteredvalue)) {
            product[i].style.display = "block";
        } else {
            product[i].style.display = "none";
        }
    }
});


closeIcon.addEventListener("click", function () {;
    search_input.value = "";
    closeIcon.style.display = "none";
});


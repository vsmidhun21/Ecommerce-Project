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

const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');
const displayedImage = document.getElementById('displayed-image');

const images = ['./images/others/slider-one.jpg', './images/others/slider-two.jpg', './images/others/slider-three.jpg'];

let currentImageIndex = 0;

function updateDisplayedImage() {
    displayedImage.src = images[currentImageIndex];
}

leftArrow.addEventListener('click', function () {
    currentImageIndex--;
    if (currentImageIndex < 0) {
        currentImageIndex = images.length - 1;
    }
    updateDisplayedImage();
});

rightArrow.addEventListener('click', function () {
    currentImageIndex++;
    if (currentImageIndex >= images.length) {
        currentImageIndex = 0;
    }
    updateDisplayedImage();
});

function changeImageAutomatically() {
    currentImageIndex++;
    if (currentImageIndex >= images.length) {
        currentImageIndex = 0;
    }
    updateDisplayedImage();
}
setInterval(changeImageAutomatically, 3000);
updateDisplayedImage();

window.addEventListener("scroll", function () {
    var elements = this.document.querySelectorAll(".initial-scroll-animate")
    elements.forEach((el) => {
        windowHeight = window.innerHeight
        var elbound = el.getBoundingClientRect()

        if (windowHeight > elbound.top - 100) {
            el.classList.remove("reveal-scroll-animate")

        }
    })
})



var liked = document.querySelectorAll(".liked")

for(let i=0;i<liked.length; i++){

liked[i].addEventListener("click", function () {
    if (liked[i].src.includes('redheart.png')) {
        liked[i].src = './images/icons/blackheart.png';
    } else {
        liked[i].src = './images/icons/redheart.png';
    }
});
}


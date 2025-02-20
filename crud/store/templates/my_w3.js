// Modal Image Gallery
function onClick(element) {
    document.getElementById("img01").src = element.src;
    document.getElementById("modal01").style.display = "block";
    var captionText = document.getElementById("caption");
    captionText.innerHTML = element.alt;
}

// Change style of navbar on scroll
window.onscroll = function () { myFunction() };
function myFunction() {
    var navbar = document.getElementById("myNavbar");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        navbar.className = "w3-bar" + " w3-card" + " w3-animate-top" + " w3-white";
    } else {
        navbar.className = navbar.className.replace(" w3-card w3-animate-top w3-white", "");
    }
}

// Used to toggle the menu on small screens when clicking on the menu button
function toggleFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

// typewriter function
function typeWriter() {
    if (i < txt.length) {
        document.getElementById("demo").innerHTML += txt.charAt(i);
        i++;
        typing = setTimeout(typeWriter, speed); // Save the timeout to be cleared later
    }
}

function startErasing() {
    clearTimeout(typing);  // Stop typing if it hasn't finished
    eraseTimeout = setTimeout(eraseText, eraseDelay);  // Wait before erasing
}

function eraseText() {
    var demoText = document.getElementById("demo").innerHTML;
    if (demoText.length > 0) {
        document.getElementById("demo").innerHTML = demoText.substring(0, demoText.length - 1);  // Erase one character at a time
        setTimeout(eraseText, eraseSpeed);  // Continue erasing at the given speed
    } else {
        i = 0;  // Reset the index when everything is erased
    }
}

// Working hide and show content (load more button functionality)
// function toggleContent(dotsId, moreTextId, btnId) {
//     var dots = document.getElementById(dotsId);
//     var moreText = document.getElementById(moreTextId);
//     var btnText = document.getElementById(btnId);

//     if (dots.style.display === "none") {
//         dots.style.display = "inline";  // Show dots if content is collapsed
//         btnText.innerHTML = "Load more";  // Change button text
//         moreText.style.display = "none";  // Hide additional content
//     } else {
//         dots.style.display = "none";  // Hide dots if content is expanded
//         btnText.innerHTML = "Load less";  // Change button text
//         moreText.style.display = "inline";  // Show additional content

//            }
// }     
    //   enchanced hide-show functionality
    function toggleContent(dotsId, moreTextId, btnId) {
        var dots = document.getElementById(dotsId);
        var moreText = document.getElementById(moreTextId);
        var btnText = document.getElementById(btnId);
    
        // Check if content is collapsed or expanded
        if (dots.style.display === "none") {
            // Collapse the additional content
            dots.style.display = "inline";  // Show dots if content is collapsed
            btnText.innerHTML = "Load more";  // Change button text
            moreText.style.display = "none";  // Hide additional content
    
            // Scroll back to the button after collapsing (Show less clicked)
            setTimeout(function() {
                btnText.scrollIntoView({ behavior: 'auto', block: 'center' });
            }, 0); // Small delay to handle collapse effect
        } else {
            // Expand the additional content
            dots.style.display = "none";  // Hide dots if content is expanded
            btnText.innerHTML = "Load less";  // Change button text
            moreText.style.display = "inline";  // Show additional content
    
            // No scroll on expanding (Show more clicked)
        }
    }
    
    

// this helps text to slide
window.addEventListener('scroll', function () {
    const slides = document.querySelectorAll('.slide');
    slides.forEach(slide => {
        const slidePosition = slide.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.5;

        if (slidePosition < screenPosition) {
            slide.classList.add('visible');
            slide.classList.remove('hidden');
        }
    });
});


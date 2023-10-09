'use strict';

/**
 * add event listener on multiple elements
 */

const addEventOnElements = function (elements, eventType, callback) {
  for (let i = 0, len = elements.length; i < len; i++) {
    elements[i].addEventListener(eventType, callback);
  }
}



/**
 * PRELOADER
 * 
 * preloader will be visible until document load
 */

const preloader = document.querySelector("[data-preloader]");

window.addEventListener("load", function () {
  preloader.classList.add("loaded");
  document.body.classList.add("loaded");
});



/**
 * MOBILE NAVBAR
 * 
 * show the mobile navbar when click menu button
 * and hidden after click menu close button or overlay
 */

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNav = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNav);



/**
 * HEADER & BACK TOP BTN
 * 
 * active header & back top btn when window scroll down to 100px
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeElementOnScroll = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

window.addEventListener("scroll", activeElementOnScroll);



/**
 * SCROLL REVEAL
 */

const revealElements = document.querySelectorAll("[data-reveal]");

const revealElementOnScroll = function () {
  for (let i = 0, len = revealElements.length; i < len; i++) {
    if (revealElements[i].getBoundingClientRect().top < window.innerHeight / 1.15) {
      revealElements[i].classList.add("revealed");
    } else {
      revealElements[i].classList.remove("revealed");
    }
  }
}

window.addEventListener("scroll", revealElementOnScroll);

window.addEventListener("load", revealElementOnScroll);

document.addEventListener('DOMContentLoaded', async function() {
  const startCallButton = document.querySelector('.start-call-button');

  startCallButton.addEventListener('click', async function() {
    try {
      const name = document.querySelector('[name="name"]').value;
      const countryCode = document.querySelector('[name="country_code"]').value;
      const phoneNumber = document.querySelector('[name="phone_number"]').value;

      const phoneNumberWithCode = `+${countryCode}${phoneNumber}`;

      const requestData = {
        name: name,
        phone_number: phoneNumberWithCode
      };

      const response = await fetch('http://172.20.10.2:5000/make_call', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data); 
        window.location.href = 'call.html'; // Navigate to call.html
      } else {
        throw new Error('Network response was not ok');
      }
    } catch(error) {
      console.error('Error:', error);
    }
  });
});

document.addEventListener('DOMContentLoaded', function() {
  const backButton = document.querySelector('.back-to-home-button');
  console.log("Button found:", backButton);

  backButton.addEventListener('click', function() {
    console.log("Button clicked!");
  });
});

// document.addEventListener('DOMContentLoaded', async function() {
//   const backButton = document.querySelector('.back-to-home-button');
//   console.log("hi");

//   backButton.addEventListener('click', async function() {
//     console.log("Button clicked!"); 

//     try {
//       const phone_number = "+918978843640"; 

//       const response = await fetch('http://172.20.10.2:5000/make_sms', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ phone_number }) // Ensure phone_number is sent as an object
//       });

//       if (response.ok) {
//         const data = await response.json();
//         console.log(data); 
//         window.location.href = 'index.html';
//       } else {
//         throw new Error('Network response was not ok');
//       }
//     } catch(error) {
//       console.error('Error:', error);
//     }
//   });
// });



  

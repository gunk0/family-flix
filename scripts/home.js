"use strict;";

$(document).ready(function() {
  $('.genre').on('click', function() {
      $('html, body').animate({scrollTop: 0}, 600);
  });
});

function filter(className) {
  var divs = document.querySelectorAll('#mov');
  divs.forEach(function(div) {
    console.log(divs.classList)
      if (div.classList.contains(className)) {
          div.style.display = 'block';
      } else {
          div.style.display = 'none';
      }
  });
};

function filterTV(className) {
  var divs = document.querySelectorAll('#tv');
  divs.forEach(function(div) {
    console.log(divs.classList)
      if (div.classList.contains(className)) {
          div.style.display = 'block';
      } else {
          div.style.display = 'none';
      }
  });
};


function filterName(event) {
  var searchInput = event.target.value.toLowerCase();
  var divs = document.querySelectorAll('.contained');
  console.log(event.target.value)

  for (var i = 0; i < divs.length; i++) {
      var div = divs[i];
      var boldElement = div.querySelector("b");
      var searchText = boldElement.textContent.toLowerCase(); 
      
      // search movie title
      if (searchText.startsWith(searchInput)) {
          div.style.display = 'block';
      } else {
        if (searchText.includes(searchInput)) {
          div.style.display = 'block';
        } else {
          div.style.display = 'none';
        }
          // div.style.display = 'none';
      }
  }
  $('html, body').animate({scrollTop: 0}, 600);
};



function addValue(element) {
  var i = element.querySelector("#value");
  var value = element.getAttribute("value");
  i.innerText = value;
}

function retValue(element) {
  var i = element.querySelector("#value");
  i.innerText = "";
}

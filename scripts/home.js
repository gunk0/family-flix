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
}

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
}


// update side nav with genres, etc
// function updateSide(u) {
//   var uls = document.querySelectorAll(".category");
//   uls.forEach(function(ul) {

//     if (ul.)
//   }
  
//   )
// }

// $(function(){
//   $('#selGenre').change(function(){
//     var selected = $(this).find(':selected').text();
//     console.log(selected)
//     if (selected=="All"){
//       $(".desc").show();
//       $("html, body").animate({
//         scrollTop: 0
//     }, 600);
//     } else {
//       $(".desc").hide();
//       $('#' + selected).show();
//       $("html, body").animate({
//         scrollTop: 0
//     }, 600);
//     }
//   }).change()

// });

// $(function(){
//   $('#selSeason').change(function(){
//     var selected = $(this).find(':selected').text();
//     console.log(selected)
//     if (selected=="All"){
//       $(".desc").show();
//       $("html, body, .sidebar").animate({
//         scrollTop: 0
//     }, 600);
//     } else {
//       $(".desc").hide();
//       $('#' + selected).show();
//       $("html, body, .sidebar").animate({
//         scrollTop: 0
//     }, 600);
//     }
//   }).change()

// });


// function filter(name) {
//   const genre = document.getElementById(name)
//   if (genre.id=="All"){
//     $(".All").show();
//     $("html, body, .sidebar").animate({
//       scrollTop: 0
//   }, 600);
//   } else {
//     $("#mov").hide();
//     $('.' + genre.id).show();
//     $("html, body, .sidebar").animate({
//       scrollTop: 0
//   }, 600);
//   console.log(genre.id)
// }}













// function setSrc(seasonEpisode) {
//     const video = document.getElementById('videoContent');
//     const show = document.getElementById(seasonEpisode);
//     let file = `http://localhost:5500/content/tv/${show.className}/content/${seasonEpisode.substring(0, 3)}/${seasonEpisode}.mp4`;
    
//     fetch(file)
//     .then(response => {
//       if (response.ok) {
//         // file exists, set the video source
//         video.src = file;
//       } else {
//         // try adding "mkv" extension
//         file = file.slice(0, -3) + "mkv";
//         console.log(file)
//         fetch(file)
//           .then(response => {
//             if (response.ok) {
//               // file exists, set the video source
//               video.src = file;
//               console.log(file)
//             } else {
//                // try adding "mkv" extension
//               file = file.slice(0, -3) + "m4v";
//               console.log(file)
//               fetch(file)
//                 .then(response => {
//                   if (response.ok) {
//                   // file exists, set the video source
//                   video.src = file;
//                   console.log(file)
//                 } else {
//                   // try adding "avi" extension
//                   file = file.slice(0, -3) + "avi";
//                   fetch(file)
//                     .then(response => {
//                       if (response.ok) {
//                         // file exists, set the video source
//                         video.src = file;
//                         console.log(file)
//                       } else {
//                         // file doesn't exist with any of the extensions
//                         console.error('File not found!');
//                       }
//                     });
//             }
//           });
//       }
//     });
//   }
// });
// }

// function adjcol(id) {
//   if (id=="film") {
//     $('#header').css('background-color','#2CAB38')
//   }
//   else if (id=="tv") {
//     $('#header').css('background-color','#58782B')
//   }
//   else if (id=="for") {
//     $('#header').css('background-color','#A9DEAE')
//     }
//     else if (id=="doc") {
//       $('#header').css('background-color','#6D5185')
//     }
//     else {
//       $('#header').css('background-color','#4F2CAB')
//     } 

// }



function addValue(element) {
  var i = element.querySelector("#value");
  var value = element.getAttribute("value");
  i.innerText = value;
}

function retValue(element) {
  var i = element.querySelector("#value");
  i.innerText = "";
}

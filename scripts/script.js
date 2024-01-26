// Get sidebar items and content sections
const sidebarItems = document.querySelectorAll(".sidebar li");
const contentSections = document.querySelectorAll(".item");

// Function to update content and about section
function updateContent(event) {
  // Remove active class from all sidebar items
  sidebarItems.forEach((item) => {
    item.classList.remove("active");
  });

  // Add active class to clicked sidebar item
  event.target.classList.add("active");

  // Get clicked sidebar item's data section
  const sectionId = event.target.getAttribute("data-section");

  // Hide all content sections
  contentSections.forEach((section) => {
    section.style.display = "none";
  });

  // Show clicked content section and about section
  const contentSection = document.querySelector(`#${sectionId}`);
  contentSection.style.display = "block";

  const aboutSection = document.querySelector(".about");
  aboutSection.innerHTML = `About ${event.target.innerText}`;
}

// Add click event listener to each sidebar item
sidebarItems.forEach((item) => {
  item.addEventListener("click", updateContent);
});


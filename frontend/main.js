document.addEventListener("DOMContentLoaded", () => { // Ensure DOM is loaded
  // --- Element references ---
  const refreshBtn = document.querySelector(".refresh-btn");
  const sidebarButtons = document.querySelector(".sidebar-buttons");
  const mainContent = document.querySelector(".main-content");
  const generateBtn = document.querySelector(".generate-btn");

  let selectedEpicIndex = null; // Store currently selected epic

  // --- Load epics from backend and create buttons ---
  async function loadEpics() { // Fetch epics from backend
    mainContent.textContent = "Loading epics...";
    sidebarButtons.innerHTML = ""; // Clear sidebar
    selectedEpicIndex = null; // Reset selected epic

    try {
      const response = await fetch("http://127.0.0.1:5000/refresh-epics"); // Call backend endpoint
      if (!response.ok) throw new Error("Failed to fetch epics"); // Error handling

      const epics = await response.json();
      if (Object.keys(epics).length === 0) { // No epics found
        mainContent.textContent = "No epics found."; // Update main content
        return; // Exit function if no epics found
      }

      mainContent.textContent = "Select an epic to generate AI stories.";

      // Create epic buttons
      for (const key in epics) { // Iterate over epics
        const epic = epics[key]; // Get epic details
        // Create button element
        const btn = document.createElement("button");
        btn.type = "button"; // ensure no form submission
        btn.className = "epic-btn league-spartan";
        btn.textContent = `${epic.key}: ${epic.name}`; // Button text
        btn.dataset.index = key; // Store epic key in data attribute

        sidebarButtons.appendChild(btn); // Add button to sidebar

        // Epic selection handler
        btn.addEventListener("click", () => { // On button click
          selectedEpicIndex = key; // Store selected epic key

          // Highlight selected epic
          document.querySelectorAll(".epic-btn").forEach(b => b.classList.remove("selected")); // Remove highlight from all
          btn.classList.add("selected"); // Highlight clicked button

          mainContent.textContent = `Selected ${epic.key}: ${epic.name}. Click "Generate" to create AI stories.`; // Update main content
        }); // End click handler
      }
    } catch (err) { // Error handling
      mainContent.textContent = "Failed to load epics."; // Update main content
      console.error(err);
    }
  }

  // --- Generate AI stories for selected epic ---
  async function generateAI() { //call backend to generate AI stories
    if (!selectedEpicIndex) { //if No epic selected
      mainContent.textContent = "Please select an epic first.";
      return; //exit if no epic selected
    }

    mainContent.textContent = "Generating AI response...";

    try {
      const response = await fetch(`http://127.0.0.1:5000/generate-ai/${selectedEpicIndex}`); //call backend endpoint to generate AI stories from selected epic index
      if (!response.ok) throw new Error("Failed to fetch AI response"); //error handling

      const data = await response.json(); //parse JSON response

      // Display the **human-readable** text only
      mainContent.innerHTML = `<pre>${data.readable_text}</pre>`; //display human-readable text in main content
    } catch (err) {
      mainContent.textContent = "Failed to generate AI response.";
      console.error(err);
    }
  }

  // --- Event listeners ---
  refreshBtn.addEventListener("click", loadEpics);
  generateBtn.addEventListener("click", generateAI);

  //loads epics automatically on page load
  //loadEpics();
});

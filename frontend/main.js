document.addEventListener("DOMContentLoaded", () => {
  const refreshBtn = document.querySelector(".refresh-btn");
  const sidebarButtons = document.querySelector(".sidebar-buttons");
  const mainContent = document.querySelector(".main-content");
  const generateBtn = document.querySelector(".generate-btn");

  let selectedEpicIndex = null; // Store the currently selected epic

  // Function to fetch epics and create buttons
  async function loadEpics() {
    mainContent.textContent = "Loading epics...";
    sidebarButtons.innerHTML = ""; // Clear existing buttons
    selectedEpicIndex = null;

    try {
      const response = await fetch("http://127.0.0.1:5000/refresh-epics");
      if (!response.ok) throw new Error("Failed to fetch epics");
      const epics = await response.json();

      if (Object.keys(epics).length === 0) {
        mainContent.textContent = "No epics found.";
        return;
      }

      mainContent.textContent = "Select an epic to generate AI stories.";

      // Create buttons for each epic
      for (const key in epics) {
        const epic = epics[key];
        const btn = document.createElement("button");
        btn.className = "epic-btn league-spartan";
        btn.textContent = `${epic.key}: ${epic.name}`;
        btn.dataset.index = key; 
        sidebarButtons.appendChild(btn);

        // Click event to select epic
        btn.addEventListener("click", () => {
          selectedEpicIndex = key;

          // Highlight selected epic
          document.querySelectorAll(".epic-btn").forEach(b => b.classList.remove("selected"));
          btn.classList.add("selected");

          mainContent.textContent = `Selected ${epic.key}: ${epic.name}. Click "Generate" to create AI stories.`;
        });
      }
    } catch (err) {
      mainContent.textContent = "Failed to load epics.";
      console.error(err);
    }
  }

  // Generate AI stories for the selected epic
  async function generateAI() {
    if (!selectedEpicIndex) {
      mainContent.textContent = "Please select an epic first.";
      return;
    }

    mainContent.textContent = "Generating AI response...";

    try {
      const aiResponse = await fetch(`http://127.0.0.1:5000/generate-ai/${selectedEpicIndex}`);
      if (!aiResponse.ok) throw new Error("Failed to fetch AI response");

      const data = await aiResponse.json();
      mainContent.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    } catch (err) {
      mainContent.textContent = "Failed to generate AI response.";
      console.error(err);
    }
  }

  refreshBtn.addEventListener("click", loadEpics);
  generateBtn.addEventListener("click", generateAI);
});

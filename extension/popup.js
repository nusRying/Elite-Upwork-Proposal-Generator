document.getElementById('generateBtn').addEventListener('click', async () => {
    const statusEl = document.getElementById('status');
    statusEl.innerText = "Analyzing page...";

    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.tabs.sendMessage(tab.id, { action: "scrape" }, async (response) => {
        if (!response) {
            statusEl.innerText = "Error: Use on Upwork job page.";
            return;
        }

        statusEl.innerText = "Sending to Elite Backend...";
        
        try {
            const res = await fetch('http://localhost:8000/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(response)
            });
            const result = await res.json();
            statusEl.innerText = "Proposal Generated! Check Dashboard.";
        } catch (err) {
            statusEl.innerText = "Error: Backend not running.";
        }
    });
});


chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "extract_content") {
        console.log("Extracted Data:", message.data);

        // Now, send this data to the backend API
        fetch("http://localhost:5000/check_fact", { 
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(message.data)
        })
        .then(response => response.json())
        .then(data => console.log("Backend Response:", data))
        .catch(error => console.error("Error:", error));
    }
});

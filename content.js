chrome.runtime.onMessage.addListener((message) => {
    if (message.result) {
        let alertBox = document.createElement("div");
        alertBox.innerText = message.result;
        alertBox.style.position = "fixed";
        alertBox.style.top = "10px";
        alertBox.style.right = "10px";
        alertBox.style.background = "red";
        alertBox.style.color = "white";
        alertBox.style.padding = "10px";
        alertBox.style.borderRadius = "5px";
        alertBox.style.zIndex = "9999";
        document.body.appendChild(alertBox);
    }
});
chrome.runtime.sendMessage({
    action: "extract_content",
    data: { 
        title: document.title, 
        content: Array.from(document.querySelectorAll('p')).map(p => p.innerText).join("\n").substring(0, 1000),
        url: window.location.href // Extract the URL from the webpage
    }
});
// Function to extract title from different sources
function getTitle() {
    let title = document.querySelector('meta[property="og:title"]')?.content || 
                document.querySelector('meta[name="title"]')?.content || 
                document.title;
    return title || "Unknown Title";
}

// Function to extract main text from article or paragraphs
function getMainContent() {
    let article = document.querySelector('article');
    if (article) return article.innerText;

    let paragraphs = document.querySelectorAll('p');
    let content = Array.from(paragraphs).map(p => p.innerText).join("\n");
    return content.substring(0, 1000);  // Limit to first 1000 chars
}

// Extracting data
let extractedData = {
    title: getTitle(),
    content: getMainContent(),
    url: window.location.href
};

// Send data to background script or extension popup
chrome.runtime.sendMessage({ action: "extract_content", data: extractedData });

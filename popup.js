document.getElementById("checkNews").addEventListener("click", async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: checkNewsOnPage
    });
});

function checkNewsOnPage() {
    chrome.runtime.sendMessage({ url: window.location.href });
}

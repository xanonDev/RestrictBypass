chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var currentUrl = tabs[0].url;
    document.getElementById("link").value = currentUrl;
    const button = document.getElementById("submit");
    button.addEventListener("click", function() {
        data = btoa(document.getElementById("link").value)
        chrome.tabs.create({ url: document.getElementById("server").value + "/bypass?link=" + data });
    });
});
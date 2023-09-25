chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.storage.sync.get(['server'], function(result) {
        if (!result.server) {
            let data = {
                server: "https://restrictbypass.xanondev.repl.co"
            }
            chrome.storage.sync.set(data, function() {});
        } else {
            document.getElementById("server").value = result.server;
        }
    });
    var currentUrl = tabs[0].url;
    document.getElementById("link").value = currentUrl;
    const button = document.getElementById("submit");
    server = document.getElementById("server");
    button.addEventListener("click", function() {
        data = btoa(document.getElementById("link").value)
        chrome.tabs.create({ url: server.value + "/bypass?link=" + data });
    });
    server.addEventListener('change', function(event) {
        dataToChange = {
            server: server.value
        }
        chrome.storage.sync.set(dataToChange, function() {});
    });
});

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
    AutoCheck = document.getElementById("automode");
    manual = document.getElementById("manual");
    button.addEventListener("click", function() {
        data = btoa(document.getElementById("link").value)
        chrome.tabs.create({ url: server.value + "/bypass?link=" + data });
    });
    chrome.storage.sync.get(['automode'], function(result) {
        if (!result.automode) {
            let data = {
                automode: false
            }
            chrome.storage.sync.set(data, function() {});
        } else {
            if (result.automode === true) {
                AutoCheck.checked = true;
                manual.style.display = 'none';
            }
            if (result.automode === false) {
                manual.style.display = 'block';
            }

        }
    });
    server.addEventListener('change', function(event) {
        dataToChange = {
            server: server.value
        }
        chrome.storage.sync.set(dataToChange, function() {});
    });
    AutoCheck.addEventListener('change', function(event) {
        dataToChange = {
            automode: AutoCheck.checked
        }
        chrome.storage.sync.set(dataToChange, function() {});
        if (AutoCheck.checked) {
            manual.style.display = 'none';
        }
        if (!AutoCheck.checked) {
            manual.style.display = 'block';
        }
    });
});

chrome.storage.sync.get(['automode'], function(result) {
    if (!result.automode) {
        let data = {
            automode: false
        }
        chrome.storage.sync.set(data, function() {});
    } else {
        if (result.automode === true) {
            let currentURL = window.location.href;
            let urlObject = new URL(currentURL);
            let protocolAndDomain = urlObject.origin;
            chrome.storage.sync.get(['server'], function(res) {
                if (protocolAndDomain != res.server) {
                    let encodedurl = btoa(currentURL);
                    window.location.href = res.server + "/bypass?link=" + encodedurl;
                } else {
                    console.log(currentURL)
                }
            });
        }

    }
});
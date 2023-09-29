const button = document.getElementById("submit");
        const link = document.getElementById("link");
        const errorBox = document.getElementById("error");
        const howToUseOverlay = document.getElementById("howToUseOverlay");

        button.addEventListener("click", function () {
            data = btoa(link.value);
            window.location.href = "/bypass?link=" + data;
        });

        link.addEventListener("keyup", function (event) {
            if (event.keyCode === 13) {
                button.click();
            }
        });

        function closeHowToUseOverlay() {
            howToUseOverlay.style.display = "none";
        }
        let url = new URL(window.location.href);
        errorUrl = url.searchParams.get("error");
        errorDet = url.searchParams.get("errorDet");
        if(errorUrl) {
          howToUseOverlay.style.display = "none";
          link.style = "border: 2px solid red;"
          errorBox.textContent = errorUrl;
          console.error(errorDet)
          console.error("you can go to https://github.com/xanonDev/RestrictBypass/issues to report bug")
        }

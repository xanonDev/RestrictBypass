const button = document.getElementById("submit");
const link = document.getElementById("link");
const errorBox = document.getElementById("error");
const howToUseOverlay = document.getElementById("howToUseOverlay");
const body = document.getElementById("body")
const container = document.getElementById("container");
const linkField = document.getElementById("link");
const themeIcon = document.getElementById("theme-icon");

if (localStorage.getItem("showAgain") === "No") {
  howToUseOverlay.style.display = "none";
}

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
  if (document.getElementById("ShowAgain").checked) {
    localStorage.setItem("showAgain", "No");
  }
}
let url = new URL(window.location.href);
errorUrl = url.searchParams.get("error");
errorDet = url.searchParams.get("errorDet");
if (errorUrl) {
  howToUseOverlay.style.display = "none";
  link.style = "border: 2px solid red;"
  errorBox.textContent = errorUrl;
  console.error(errorDet)
  console.error("you can go to https://github.com/xanonDev/RestrictBypass/issues to report bug")
}

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  body.classList.add("dark-body");
  container.classList.add("dark-container");
  link.classList.add("dark-link");
  mode = "dark"
} else {
    themeIcon.src = "https://www.uplooder.net/img/image/55/7aa9993fc291bc170abea048589896cf/sun.svg";
    body.classList.remove("dark-body");
    container.classList.remove("dark-container");
    link.classList.remove("dark-link");
    mode = "light"
}
themeIcon.addEventListener("click", function () {
  if(mode === "dark") {
  themeIcon.src = "https://www.uplooder.net/img/image/55/7aa9993fc291bc170abea048589896cf/sun.svg";
    body.classList.remove("dark-body");
    container.classList.remove("dark-container");
    link.classList.remove("dark-link");
    mode = "light"
  } else {
    themeIcon.src = "https://www.uplooder.net/img/image/2/addf703a24a12d030968858e0879b11e/moon.svg";
    body.classList.add("dark-body");
    container.classList.add("dark-container");
    link.classList.add("dark-link");
    mode = "dark"
  }
});

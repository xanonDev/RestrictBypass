# RestrictBypass

RestrictBypass is a Python-based website using Flask, designed to bypass restrictions such as those imposed by internet providers or parental controls.

## How to Use

1. Visit the RestrictBypass website: [restrictbypass.xanondev.repl.co](https://restrictbypass.xanondev.repl.co)
2. Paste the link to the website you want to open into the provided text field (e.g., https://www.youtube.com).
3. Click on the "Bypass" button.

Alternatively, you can import this repository into your own Replit workspace. [Replit Project Link](https://replit.com/@xanonDev/RestrictBypass)
### How to Host Using Replit
1. Visit the [replit site](https://replit.com)
2. login to your account or create it
3. click Create Repl
4. click Import from github
5. paste this repo url
6. select python in Language
7. click Import from github
8. click Run and enjoy

## page list
1. 'Main page (/)' - This is main page of restrict bypass, used to enter links to websites
2. 'Bypass Request (/bypass?LinkToSiteBase64Encoded)' - This subpage proxies the link provided by the user
3. 'File Proxer (/fileProxy?url=LinkToFileBase64Encoded)' - This subpage proxies the file like (image, json etc.) provided by the user

## How it Works

RestrictBypass operates by following these steps:

1. A Python script hosted on Replit (or on your server) downloads the target website on the server-side.
2. It then transforms the website into a JavaScript script.
3. The generated JavaScript script is coded to bypass filtering based on words or content.
4. As a result, the entire website is reconstructed on the client-side, allowing it to bypass restrictions.

## Warning

- **Incomplete Rendering:** Some pages may not display correctly when accessed through RestrictBypass. Efforts are ongoing to improve compatibility.
- **Use at Your Own Risk:** Using this tool may not be condoned by your employer, teacher, or internet service provider. Please be aware that using it comes with potential consequences, and you assume all risks associated with its use.

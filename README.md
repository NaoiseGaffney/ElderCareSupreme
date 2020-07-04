<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome USER_NAME,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## How to run app on local machine

- Clone application repository to you local directory.
- You will need to install python if you don't have it. All python version 3 should work. You can download the newest version from [here](https://www.python.org/downloads/)
- Once you installed python, you will need to create virtual environment. You can learn more about it from [here](https://docs.python.org/3/tutorial/venv.html). To create virtual env follow steps:
      - open terminal inside your VS code or you favourite code editor.
      - inside terminal run `python -m venv venv-eldercaresupreme`
      - now you virtual env should be created. But you need to activate it. If you are working on VS Code, press `Ctrl + Shift + P` and start typing `Python: select interpreter`. After first few letters it should come up. 
      - once you picked that option you should see a list of Python version and you virtual environment should be there. If you can't see it there. You will have to open folder where you created your virtual env and find activate.bat inside Scripts folder. Then you need to copy the absolute path to this file inside your terminal if you are working on windows. For Mac/Linux you need to add `source` at the beginning
      - then open new terminal. Above or before the line (depends which terminal you are using) you should see inside the brackets `(venv-eldercaresupreme)`
- now you need to install all packages from requirements file. To do it type in terminal `pip install -r requirements.txt`
- Almost there :). Now to run application you need to navigate inside the terminal to `src` folder. If you are in the main repository folder run `cd src`.
- If you are inside the `src` folder run `python manage.py runserver`. After this command server should lunch and when you type `localhost` inside your browser you should see that app is running as well you should see inside the terminal that server lunched and it should show you the address to the app and you can `Ctrl + click` to open it in the browser


## Design Decisions

### Design Decision - CSS:

Materialize 1.0.0 to create a simple and easy-to-read website for the elderly.

### Design Decision - Colour Scheme:

The colour scheme must provide a strong enough contrast to make the website easy to read. It needs “air” to make all elements visibly stand out, and it needs to use colours suitable for the elderly.

White background (bright and easy to read for an Elder as opposed to a dark background), possibly off-white or beige (softer, less harsh on the eyes).

Blue is a common colour for care sites, however, blue is not an ideal colour for the elderly. Nor is green. A soft purple contrasts with the white/beige background and complements the accent colour of pink.

Text colour is black and in some cases white when the buttons are purple or pink.
Accent colour needs to stand out, a strong contrast to both the background and primary colour. Pink is a strong and visible colour, perhaps in a softer and lighter shade.

Text Colour 1: #000000 Black
Text Colour 2: #FFFFFF White
Primary Colour: #B288C0 Blue Violet
Background Colour: #F4ECD6 Eggshell
Accent Colour: #FFADAD Light Pink

These colours work well for people with colour blindness, good contrasts while maintaining colour scheme integrity (Protanopia, Deuteranopia, Tritanopia, Achromatopsia, Protanomaly, Deuteranomaly, Tritanomaly, Achromatomaly).

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!

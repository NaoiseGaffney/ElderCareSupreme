

# ELDERCARE SUPREME #

Advanced Team A
 
Code Institute - 
Hackerthon July 2020


**<u>About</u>** 

This web application is has been created by a team of coders working remotely to produce a quality online resource. The project will be submitted to a panel of expert to be judged as part of an online competition which is run regularly by the Institute. The idea is to give current and past students the valuable experience of working as a team.


<u>**Concept</u>**


To create an online resource for users who are self-isolating due to Covid-19. The web application will allow someone to ask for assistance for tasks that they are unable to complete themselves. For example, Shopping, Fetching Prescriptions, Walking pets etc.

The ability for volunteers to be able to offer their time and provide assistance in completing tasks for those requesting assistance. 


**<u>UI/UX</u>**

The site design has completed with all types of user in mind, keeping the graphics and text clean and tidy. Easy to read and follow the paths through the application. 

**<u>Design Decisions</u>**

Design Decision - CSS:

Materialize 1.0.0 to create a simple and easy-to-read website for the elderly.

Design Decision - Colour Scheme:

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

**<u>User Stories:</u>**

**General Users:**

As a user, I would like to create a secure user profile. 

As a registered user I would like to be able to ask for assistance by selecting from a pre-defined drop-down menu or by entering my own details.

As a registered user I would like to be able to ask offer assistance by selecting from a pre-defined drop-down menu or by entering my own details.


As a registered user I would like to browse a list of users requesting assistance selected by distance. Then being able to select the item on the list to assign that item request to my profile. 

As a registered user I would like to be able to browse a list of assistance being offered so that I can select an item to be allocated to my profile to select that item.

**Admin users:**

As an admin user, I would like to be able to create, amend or delete the predefined tasks in the drop-down menu.

As an admin user, I would like to be able to add, amend or delete user accounts.





**<u>Testing</u>**

We have tested the application by using the in-built testing tools provided by Django. 

Also, the application has been tested by several humans using as many different devices as possible. Mobile phones, Tablets, Notebooks, and Desktops.

All the forms have been tested for field validation and functionality. The buttons throughout the site have all been tested to make sure that they are working as planned


**<u>Technology Used</u>**

* Python
* Django
* Javascript
* HTML
* CSS
* Materialize
* Heroku
* Visual Studio Code
* GitHub
* GitPod



**<u>Deployment</u>**

How to run app on local machine
Clone application repository to you local directory.

You will need to install python if you don't have it. All python version 3 should work. You can download the newest version from here

Once you installed python, you will need to create virtual environment. You can learn more about it from here. 
terminal run python -m venv venv-eldercaresupreme - now you virtual env should be created. But you need to activate it. If you are working on VS Code, press Ctrl + Shift + P and start typing Python: select interpreter. After first few letters it should come up. - once you picked that option you should see a list of Python version and you virtual environment should be there. 

If you can't see it there. You will have to open folder where you created your virtual env and find activate.bat inside Scripts folder. Then you need to copy the absolute path to this file inside your terminal if you are working on windows. 

For Mac/Linux you need to add source at the beginning - then open new terminal. Above or before the line (depends which terminal you are using) you should see inside the brackets (venv-eldercaresupreme)
now you need to install all packages from requirements file.

 To do it type in terminal pip install -r requirements.txt
Almost there :). Now to run application
 you need to navigate inside the terminal to src folder. If you are in the main repository folder run cd src.
If you are inside the src folder run python manage.py runserver. 

After this command server should lunch and when you type localhost inside your browser you should see that app is running as well you should see inside the terminal that server lunched and it should show you the address to the app and you can Ctrl + click to open it in the browser








<<<<<<< HEAD
=======
git pull origin master

git checkout master
git merge GaffTestBranch
git push
>>>>>>> d44b0c3dd74d4c02674ce78275bcd87600a11dbe































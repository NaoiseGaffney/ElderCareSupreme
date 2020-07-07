

# ELDER CARE SUPREME #

Advanced Team A
 
Code Institute - 
Hackerthon July 2020


**<u>About</u>** 

This web application is has been created by a team of coders working remotely to produce a quality online resource. The project will be submitted to a panel of expert to be judged as part of an online competition which is run regularly by the Institute. The idea is to give current and past students the valuable experience of working as a team.

**<u>Concept</u>** 

To create an online resource for users who are self-isolating due to Covid-19, those who need care and people who can give care. The web application will allow someone to ask for assistance for tasks that they are unable to complete themselves. For example, Shopping, Fetching Prescriptions, Walking pets etc.

The ability for volunteers to be able to offer their time and provide assistance in completing tasks for those requesting assistance. 

**<u>Coding Process</u>** 

We had an initial zoom meeting to introduce ourselves and decide on the concept for the project. After a short discussion, we split the team into Front-End, rear-end developers based on experience and individual preference.

We started a Trello board to contain a breakdown of the tasks required to build the website. This would also include being able to allocate tasks to team members to avoid work duplication. 

We decided to use GiHub as a store, working locally by creating branches from the master whilst working on the code and then pushing back to the master branch when completed. 

During the project we have had a morning and evening zoom meeting to keep in touch, discussing any issues and allocating work to team members.  


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

Landing Page: 

As a visitor, I would like to be able to login or register for an account.

Login Page:

As a user, I would like to be able to login to the site using my credentials.

Dashboard:

As a user, I would like to make a selection from Adding a new task, Selecting an existing task, and updating my profile details.

Search for a task:

As a user, I would like to be able to search for a task by city name or post code.

Add task:

As a user, I would like to be able to add a new task.

Update Profile:

As a user, I would like to be able to update the details in my profile.


**<u>Testing</u>**

Testing has been completed by humans using as many different devices and screen sizes as possible. Also, testing has been completed remotely at several locations using a mixture of 4g and 3g to check on response and download times.

**<u>General Website Functionality Tests:</u>**

Landing Page: 

All the buttons have been checked for functionality. All are working as planned.

Login Page:

The form has been tested line by line for validation and functionality. Working as planned.
The buttons on the page have also been tested and the links are all working correctly.

Dashboard:

All of the buttons have been tested and are working as desired.

Search for a task:

The form has been tested and is working correctly. If no tasks are available in the area selected then the correct message is displayed. Otherwise, the available tasks are displayed as planned.

Select task:

The functionality of this page has been tested and is working correctly

My tasks:

The buttons and functionality of this page have been confirmed to be working correctly.

Add task: 

The form has been tested and is working as desired.

Update Profile:

The form has been tested and works as planned. 

**<u>Technology Used</u>**

* Python
* Django
* Django REST Framwork
* Javascript
* HTML
* CSS
* Materialize
* Heroku
* Visual Studio Code
* GitHub
* GitPod
* Zoom
* Visual Studio Code



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

After this command server should lunch and when you type localhost inside your browser you should see that app is running as well you should see inside the terminal that server lunched and it should show you the address to the app and you can Ctrl + click to open it in the browser.

**<u>Acknowledgements</u>**

A special thank you for all team members for their hard work, understanding and friendship shown during the process of creating this site.

Also, a big thank you to all of our family and friends for their understanding and support shown.



































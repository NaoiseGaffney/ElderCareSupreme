# Elder Care Supreme (Code Institute Hackathon July 2020)
"Elder Care Supreme allows the elderly and aiders to connect, communicate, and collaborate on elderly daily tasks." - Team Hackathon Heart Warmers

The elderly lady / gentleman (Elder), supported by a helping hand (Care), providing diamond standard services (Supreme).

Team Heart Warmers – We warm the hearts of the Elderly we help with our Elder Care Supreme application that enables the elderly to ask for help with their daily tasks.

[Elder Care Supreme](https://elder-care-supreme.herokuapp.com/)

![Elder Care Supreme Logo (index.html)](https://github.com/NaoiseGaffney/ElderCareSupreme/blob/production/eldercaresupreme/static/images/ElderCareSupremeLogo.png)

A responsive and interactive website that provides a service to the elderly, and linking the elderly to aiders that have the opportunity to help with their daily tasks.

## Our Hackathon Challenge
Thriving in the New Normal - Connecting Together: Many older and vulnerable people are still cocooning or carefully and actively socially distancing in order to stay safe. While we may still need to remain physically distanced from others, the opportunities for connection are greater than ever before. Can you deliver or promote a simple solution that could help older and vulnerable people to stay connected to each other, the people they love and the world around them?

## Business
### External Users' Goals
Elder Care Supreme is a service for the elderly requiring help with daily chores, aided by volunteers who have the ability to provide the necessary professional services.

### Site Owner's Goals
To create an online resource for users who are self-isolating due to Covid-19, those who need care and people who can give care. The web application will allow someone to ask for assistance for tasks that they are unable to complete themselves. For example, shopping, fetching prescriptions, walking pets etc.

The ability for volunteers to be able to offer their time and provide assistance in completing tasks for those requesting assistance.

The site has potential to become more informative and interactive. It currently serves as a proof-of-concept of providing aide to the elderly based on tasks, categories, and geography.

It serves as a strong prototype for an application serving the needs of the elderly, and as an example of going above-and-beyond by the team using and improving upon the knowldege and skills the team has gained by attending the Full Stack Development course by the Code Institute.

This Hackathon is a continuous learning experience for the team:

* Working in sprints, collaborating and communicating using Trello, Slack, and Zoom.
* Working with new paradigms (Python OOP and new Django extensions), new frameworks (Materialize 1.0.0), and new databases (PostgreSQL).
* Continuous knowledge and skill sharing through Slack Video Seesions and Zoom Team Calls.

### Features
Current features:

* Register as a new user, and create a profile as either an elderly person or an aider.
* Login and logout, with password reset via e-mail.
* Create, Read, Update, and Delete daily tasks as both an elderly person and as an aider.
* Aider can search for elderly tasks to perform, view these tasks, add / view / update / and delete own tasks for help from other aiders.
* Both the elderly and aiders can communicate via task chat to better plan the execution of the daily task(s).
* [Admin Page](https://elder-care-supreme.herokuapp.com/admin/login/?next=/admin/) to work with "Group and User Authentication and Authorisation", "User Profiles", "Task Messages" between the elderly and aiders, and "Task Categories" and "Tasks".
* Footer Modal presenting the Hackathon Heart Warmers team and members, as well as providing a description of the logo, and a link to the GitHub repository.

Future improvements:

* Add location map markers and enable task selction by more precise areas.
* Provide a summary of tasks requiring help, and a list of aiders willing to help.
* View full profiles of both the elderlt and the aiders.
* Online chat forum for all to partake in, to share experiences.
* Adding a payment and money-transfer service so that aiders can go shopping and know they're covered for their expenses.
* Communicate with the Hackathon Heart Warmers to add features and functions to Elder Care Supreme.

## Processes
### UX

Elder Care Supreme is a responsive and easy-to-use service with a natural flow and easy-to-use by primarily the elderly, though also by the aiders.

There are two main actors/roles that use the services provided by the website: an elderly person and an aider.

* Elderly and Aider - UC 1 - Register, Login, and Logout: As a user, to access Elder Care Supreme, I need to register to login, and login to access my dashboard.
	* Access Landing Page --> click on Register on the navigation bar --> Register Page: enter my details (username, first name, email, password, and password confirmation) --> User Profile: enter additional details to link to aiders in the vicinity of my location (city, post code / Eircode, "is aider", phone number) --> Logout.
* Elderly and Aider - UC 2 - CRUD a task: As a user I want to add a task, view it, update it, and delete it, to allow for an aider to help me with my tasks, add additional details to help the aider, and delete it when it's done.
	* Access Landing Page --> click on Login on the navigation bar --> Login Page: provide username and password, click on the Login buton --> Dashboard: click on Add Task --> Add Task Page: fill in the form (title, select category, provide a detailed description, select a date, and optionally a time), click on the Submit button --> My Tasks Page: I can click on messages to send a message to the aider that selects my task, or edit task (pencil), or select done (tick), or delete when the task is done and I no longer need it (trash can / rubbish bin).
		* Messages --> Messages Page: click on the message field, type a message and click on the Send button. When done, click on the Dashboard button on the navigation bar, or use the breadcrumbs.
		* Edit Task -->  Update Task Page: the form is pre-populated with the previous information, and is easily updated by clicking on a form field and entering new or additional text. Click on the Submit button --> Delete Task Page: confirmation of removal, click on the Go Back To Task List button.
		* Done: click on the Done button, and it changes status/colour.
		* Delete Task: once the task is done and no longer needed, it can be deleted by clickiing on the Delete button (trash-can / rubbish bin).
* Elderly and Aider - UC 3 - View My Tasks: as a user I want to view the tasks I've created o see who is aiding, or to read my task messages.
	* Access Landing Page --> click on Login on the navigation bar --> Login Page: provide username and password, click on the Login buton --> Dashboard: click on My Tasks --> My Tasks Page: I can add another task, view my list of tasks and perform similar functions as in UC 2.
* Aider - UC 4 - Task Search and Aider Tasks: As an aider I want to search for tasks that I can do for an elderly person, and view these searched & selected tasks in my Aider Tasks.
	* Access Landing Page --> click on Login on the navigation bar --> Login Page: provide username and password, click on the Login buton --> Dashboard:
		* Task Search: enter city or post codes in the search field and click on the Search button, or simply select the tasks you can do in the card list --> Select a task by clikcing on the +person button on the lower left of a card, and the status on the card changes from "No Assigned Aider" to "Assigned aider - <username of aider>".
		* Aider Tasks: view your list of tasks for the elderly, and either message an elderly or print the card to perform the task.
* Admin - UC 5 - Administration: as an administrator I want to CRUD "Group and User Authentication and Authorisation", "User Profiles", "Task Messages" between the elderly and aiders, and "Task Categories" and "Tasks" to maintain the Elder Care Supreme service.

## Solution

#### Adherence to Theme
"Elder Care Supreme allows the elderly and aiders to connect, communicate, and collaborate on elderly daily tasks." - Team Hackathon Heart Warmers

The elderly lady / gentleman (Elder), supported by a helping hand (Care), providing diamond standard services (Supreme).

#### Team Collaboration
Extensive use of Zoom calls for Hackathon Virtual Standup meetings with agenda, notes, and video recordings stored on Trello and shared on Slack.

[Kanban Board](https://trello.com/b/cQ9G18LO/agile-sprint-board)

#### Usability and Practicability
The IA and UX Design guide the user throughout the whole Elder Care Service experience, and the colour scheme as well as the styling using Materialize CSS 1.0.0 is most apt for the elderly and those having one form or another of colour blindness.

#### Effective Use of Course Knowledge
We all went outside of our comfort zone on this Hackathon, going above-and-beyond in terms of paradigms, frameworks, deployment, and working as a global virtual team.

#### Awesomeness
![Awesomeness right there!](https://github.com/NaoiseGaffney/ElderCareSupreme/blob/GaffBranch/eldercaresupreme/static/images/Screenshot 2020-07-09 04.01.29.png)


Elder Care Supreme allows the elderly and aiders to connect, communicate, and collaborate on elderly daily tasks.

**Information Architecture:** Elder Care Supreme uses a Sequential Information Architecture to guide the elderly (who may not have the knowledge, nor skills, nor confidence to appreciate the complexity of technology) through the features they need to perform their tasks in an easy manner.

**UX Design and Design Decisions:** the colour scheme is soft and generally avoids the colours blue and green which is well suited for the elderly.

The colour scheme must provide a strong enough contrast to make the website easy to read. It needs “air” to make all elements visibly stand out, and it needs to use colours suitable for the elderly.

White background (bright and easy to read for an Elder as opposed to a dark background), possibly off-white or beige (softer, less harsh on the eyes).

Blue is a common colour for care sites, however, blue is not an ideal colour for the elderly. Nor is green. A soft pink contrasts with the white/beige background and complements the accent colour of purple.

Text colour is black and in some cases white when the buttons are purple or pink. Accent colour needs to stand out, a strong contrast to both the background and primary colour.

* Text Colour: #000000 Black or #ffffff White.
* Primary Colour: #f06292 Pink Lighten-2
* Secondary / Accent Colour: #800080 Purple
* Background Colour: #FBF8EF Eggshell White
 
These colours work well for people with colour blindness, good contrasts while maintaining colour scheme integrity (Protanopia, Deuteranopia, Tritanopia, Achromatopsia, Protanomaly, Deuteranomaly, Tritanomaly, Achromatomaly). We've tested Elder Care Supreme with Sim Daltonism to ensure we always have good contrast and visibility regardless of colour blindness condition. In addition we've opted for a clear font, Raleway, and large font-sizes on all devices to ensure readability for our users.

We have chosen Materialize CSS 1.0.0 as our front-end framework as the iconography, features, and availble colour schemes provide clear, contrasting, and visible features suitable to the elderly and people with some form of colour blindness.

### Code

[GitHub Repository](https://github.com/NaoiseGaffney/ElderCareSupreme/)

## Technology

A list of the languages, frameworks, libraries, and other tools used for this project.

### Code:
* [HTML 5.2. - W3C Recommendation, 14 December 2017](https://www.w3.org/TR/html52/)
	* The project uses HTML 5 to create the content.
* [CSS 3 CSS - Snapshot 2018 W3C Working Group Note, 22 January 2019](https://www.w3.org/TR/css-2018/)
	* The project uses CSS 3 to style the content and provide the layout.
* [Materialize CSS 1.0.0](https://materializecss.com/)
	* The front-end framework is Materialize CSS 1.0.0.
* [ECMAScript&reg; 2015 Language Specification](http://www.ecma-international.org/ecma-262/6.0/)
	* The project uses JavaScript, based on the ECMAScript language specification and implemented by numerous browser vendors. As a general rule, I read the implementation of this at [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript).
* [Python 3.8.2](https://www.python.org/)
	* All back-end heavy lifting is done through Python, the Django Web Framework and assocaited extensions, as well as PostgreSQL.
* [Django Web Framework](https://www.djangoproject.com/)
	* All back-end heavy lifting is done through Python, the Django Web Framework and assocaited extensions, as well as PostgreSQL.
* [PostgreSQL](https://www.postgresql.org/)
	* All back-end heavy lifting is done through Python, the Django Web Framework and associated extensions, as well as PostgreSQL.

### Development and Staging Platforms and Environments
* [GitHub / GitPod /Git / GitHub Pages](https://github.com/)
	* The project uses GitHub:
		* Git to add, commit, and push the project files to GitHub.
* [Code Institute GitPod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
	* Using the GitPod Full Template from the Code Institute for our project.
* [DropBox](https://www.dropbox.com/)
	* Using DropBox as a staging area for Visual Studio Code, and synching this with GitHub.
* [Visual Studio Code](https://code.visualstudio.com/)
	* Code writing and staging. Use Visual Studio Code for all team development.
* [LiveServer for Visual Code Studio](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
	* This is the local Web Server used for development and testing, running as an add-on to Visual Studio Code.
* [Heroku](https://www.heroku.com/)
	* Cloud Application Platform and is where Elder Care Supreme is hosted.
* [Zoom](https://zoom.us/)
	* All Hackathon Virtual Standup Calls, all recorded, stored on DropBox, shared notes/agenda/recording on Slack and Trello.
* [Trello](https://trello.com/)
	* Our Kanban Board is on Trello, and we move our cards along as we finish each stage.
* [Slack](https://slack.com/)
	* For all ad-hoc communication and collaboration.

### Documentation Tools
* [MacDown](https://macdown.uranusjr.com/)
	* Using this application to write this documentation in MarkDown.
* [Microsoft Office 365 - PowerPoint](https://office.live.com/start/powerpoint.aspx)
	* Using this application to create website diagrams, logos, and presentations.

### Acknowledgements and Attributions of Used Features and Functions
* [Google Fonts: Raleway](https://fonts.googleapis.com/css?family=Raleway%7C&display=swap)
	* Using this font in different sizes for all text.
* [FontAwesome CDN](https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css)
	* Using FontAwesome font icons to add visual elements to key website features, making the website memorable and easier to navigate.
* [Material Design](https://material.io/)
	* Using icons throughout the website as they suit Materialize CSS 1.0.0 and the UX Design pricniples of this service.

### General Knowledge and Hours of Reading
* Team Collaboration and Knowledge Sharing is the cornerstone of our success as a team. We shared knowledge and skills, based on previous experiences and through the Code Institute course, as well as what we learned by going above-and-beyond on this Hackathon project.
* A special mention must go to Toby, our resident Python

### Elixir of Life
* [Strong Black French Press Coffee](https://www.youtube.com/watch?v=st571DYYTR8)
	* Keeps me alert and on-schedule; keeps me going through the night. This is the secret source of my programming-powers. :-)

## Testing

### Manual Testing Technology - Unit, Integration, and System Testing
The following combination of software and hardware is used for all manual tests:

* Chrome on MacOSX (MacBook Pro) for both laptop/large display and mobile devices (inspect --> responsive).
* Firefox Developer Edition on MacOSX (MacBook Pro) for both laptop/large displays and mobile devices (Web Developer Tools --> Responsive Design Mode).
* Safari on MacOSX (MacBook Pro) for laptop/large display testing.
* Physical devices: Samsung Galaxy Note 10+ 5G with Chrome, Samsung Browser and Firefox. Apple iPhone 8 with Chrome and Safari.

### Automated Testing Technology - Acceptance (System) Testing
Automated testing is performed using:

* [Selenium IDE](https://www.selenium.dev/selenium-ide/) - the Chrome and Firefox extensions.
* [Selenium IDE Automated Test File](https://github.com/NaoiseGaffney/ElderCareSupreme/blob/production/src/Elder%20Care%20Supreme.side)
* [Video Walkthrough of General Test Case 1]()
* [Video Walkthrough of General Test Case 2]()

### Testing Notes
All devices and formats are tested in both portrait and landscape mode. The website is responsive and supports all tested browsers.

A couple of things to note:

* We discovered that running complete (end-to-end) continuous website walkthrouhgs aided in identifying functional and styling issues, as well as ensuring conformity to our design standards.
* We have discovered ways in which to easily add custom CSS to Materialize CSS 1.0.0 using the Chrome Inspector features.
* Using the Django Materialize extension causes styling and conformity issues, as it uses the earlier version of Materialize CSS 0.100.2 and not Materialize CSS 1.0.0. We've found ways in which to deal with this and consistently style with Mateialize CSS 1.0.0.

### HTML, CSS, and JS Validation
#### HTML
[HTML Validation](https://validator.w3.org/nu/)

![HTML Validated](https://github.com/NaoiseGaffney/CitiesInCountries/blob/master/documentation/HTML%20Validation.png)

[HTML Validation Link for the website](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnaoisegaffney.github.io%2FCitiesInCountries%2F)

#### CSS
[CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input)

[CSS Validation Link for the website](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Felder-care-supreme.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

One error beyond our control as it relates to the Materialize CSS 1.0.0 CDN. Otherwise the website has warnings, which are not considered critical. We could donwload and install Materialize CSS 1.0.0, edit the highlighted error, and use that instead of the CDN.

## Deployment

![Deployment, CD, Roles and Responsibilities](https://github.com/NaoiseGaffney/ElderCareSupreme/blob/GaffBranch/eldercaresupreme/static/images/Elder Care Supreme CD and Platform.png)

### Initial Environment Setup

* git clone https://github.com/NaoiseGaffney/ElderCareSupreme.git
* git branch <yourbranchname>
* git config --global user.mail "<youremailaddress>"
* git config --global user.name "<yourGitHubname>"
* git add .
* git commit -m "Sensible and descriptive message"
* git push --set-upstream origin <yourbranchname>
* Login pop-up: login (first time only)

### Pushing Code

* git add .
* git commit -m "Sensible and descriptive message"
* git push
* git checkout master
* git merge <yourbranchname>
* git push
* git checkout production
* git merge master
* git push

### Configuring and Running `manage.py`

#### Initial Model Creations when Using SQLite3 (moved to PostgreSQL in production)

* src/python manage.py makemigrations
* src/python manage.py migrate
* src/python manage.py createsuperuser

#### Running `manage.py`

* src/python manage.py runserver

For this project we use Visual Studio Code for coding, and using the Source Code Management provider with git to synch (stage, commit, synch) updates to GitHub.

A simplified view of the Continuous Delivery: VS Code on own <branch>, tested by individual `python manage.py runserver`, pushed to GitHub --> merged with <master>, pushed to GitHub, tested by peer --> merged with <production>, pushed to GitHub --> automatically deployed to Heroku Staging in Pipeline, tested in staging --> manually promoted to production on Heroku with final testing.

![Heroku Staging Deployment triggered by GitHub production branch update](https://github.com/NaoiseGaffney/ElderCareSupreme/blob/GaffBranch/eldercaresupreme/static/images/Screenshot 2020-07-09 03.45.51.png)

![Heroku Production Promotion - manual](https://github.com/NaoiseGaffney/ElderCareSupreme/blob/GaffBranch/eldercaresupreme/static/images/Screenshot 2020-07-09 03.46.50.png)

![Heroku Production Deployment](https://github.com/NaoiseGaffney/ElderCareSupreme/blob/GaffBranch/eldercaresupreme/static/images/Screenshot 2020-07-09 03.46.57.png)

## Credits
Team Hackathon Heart Warmers!
Miklos!
Code Institute!

### Content
- [GitHub: Project Repository](https://github.com/NaoiseGaffney/ElderCareSupreme/)
- [Website: Elder Care Supreme](https://elder-care-supreme.herokuapp.com/)
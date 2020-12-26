<h1>Mathed, a fun way to learn mathematics.</h1>
<br>
<br>
<h2>List of contents:<h2>
1. Technology used and packages, libraries, frameworks.<br>
2. Project Overview.<br>
3. Functionality explaination.<br> 
<br>
<br>
<h2> Technology used:</h2>
<br>
1. Languages: Python 3.8, JavaScript ES6.<br>
2. Frameworks: React JS, Django, UIKit (css), Bootstrap (CSS via CDN and only in snippets) Dashboard Nav Fireship IO responsive Navigation ``https://github.com/fireship-io/222-responsive-icon-nav-css/tree/master/public``.<br>
3. Dependencies: Django psycopg_2.<br>
4. Database: PostgreSQL(heroku).<br>
<br>
<br>
<h2> Project overview:</h2>
<br>
Mathed is a math education test generator and game which involves solving math equations by the user, the supported quizz types are Sum, Substraction and Multiplication.
<br>
The difficulty is set at a fixed medium difficulty standard which means fixed three figure math operations.
<br>
The test workload is fixed to 5 questions, we can alter the number of questions dynamiclly in the python file, the system is engineered to work automatically and render content acordinglly to the variables modified.
<br>
The project was based in my personal experience as a child with boring and antiquated methods for external learning (for example, kumon math centers, etc...), i figured out that there may be a way to make easier for the parents to make their children learn math and to watch the progress closely, also the possibility to make school groups and make easier for the teachers to teach (this functions are in the main application blueprint and models, as i plan to lauch this project to the market, the structure of it and main engines are created providing an overall blueprint of the project, also in the production version i will include an A.I that raises the difficulty, i will use this projec's A.I as my final project for the A.I course i plan to take next year.)
<br>
The user can edit their profile, this math learning game offers a ranking system by points, by default, each question answered correctlly grants one point.
Also there are 4 achievements and one secret achievement.
<br>
<br>
<h2> Functionallity explaination:</h2>
<br>
The project structure the following (it only explains the added files):
<br>
- final: our application manager directory
<br>
- mathed: our application directory
<br>
--static/mathed: static files for our application (CSS, JS)
<br>
--templates: our html templates<br>
--auxfunctions.py: Our test process functions and helper functions for views.py<br>
--models.py: database models<br>
--sessionmaker.py: our sessionmaker and account creation helpers<br>
--views.py<br>
- manage.py<br>
- requirements.txt<br>
<br>
<br>
<h3> Brief fuctions, methods and classes overview</h3>
<br>
Our application entry point is views.py, which includes routing functions and api routes.
In our profile function we can see a switch implementation in python by using a dictionary data structure, the only way to retrieve data is by a POST request and a valid session, this part of the application is managed by our controls.js file, which is in charge of controlling processes in our page application and sending data to our api.js file which contains a cookie CSRF token generator and different api engines for various data queries.
<br>
Finally the components are rendered using reactjs framework, all code snippets and elements are located in renderengine.js.
<br>
The test engine generates random numbers and solves the equation, afterwards converts the result into a hex value to prevent any potential cheating.
<br>
<br>
<h2>Conclussion</h2>
<br>
With this project i hope to make easier for all the children lo learn math, this final project represents my idea and provides blueprinting for future functions such as A.I and parent/tutor control and advanced data statistics, including various achevements.
<br>
Special thanks to Brian, David and CS50, hopefully you will see this project converted in a startup, wish me luck.
<br>
Created by: Jose Alejandro Melendez Garcia, Chihuahua, Mexico.<br>
Version 1.0 finished by 26/12/2020 at 1:30 AM using a lot of coffee.

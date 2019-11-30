# DesignMarket

In this project I tested my Full Stack Development skills to build a web application where users can
request designers to make graphic designs for them.
 
## UX
 
The site is built for people who want to earn money through designing and for people who want to buy designs.

- When making the site I focused on making it very easy to use, yet very practical.
- The user knows what to do with reading/instructions because of the design.

1. User Story: A user can register and login.
2. User Story: A user can request a design.
3. User Story: A designer can look through all requests.
4. User Story: Once a designer has found one he/she can start designing.
5. User Story: Once the designer is done, he/she can send the design to the user.
6. User Story: The user and designer can see the final product.
7. User Story: When the user opens the quote which the designer sent back, the user can review the design.
8. User Story: Then the user can pay with credit card, the money will be sended to the site owner, and the site owner pays 80% to the designer.
9. User Story: The user can now use their design, and the designer can spend his/her money.


## Features

 
### Existing Features
for users:
- Registering
- Creating requests
- Seeing all own requests
- Paying

for designer:
- Registering
- Seeing all requests which haven't been completed yet
- Sending quotes after requests


## Technologies Used

- [HTML5]
	- The project uses **HTML5** to build the structure of the website

- [CSS3]
	- The project uses **CSS3** to style the HTML5/structure of the website.

- [Python](https://www.python.org/)
	- The project uses **Python** to create and import functions for running the whole site.

- [Django](https://www.djangoproject.com/)
	- The project uses **Django** to link urls/pages, databases, models, views and more with eachother

- [Javascript](https://www.javascript.com/)
	- The project uses **Javascript** to make the project interactive.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [PostgreSQL](https://www.postgresql.org/)
  - The project uses **PostgreSQL** for storing data.

- [Google Fonts](https://fonts.google.com/)
	- The project uses **Google Fonts** to use fonts which aren't included in the browser.

- [Bootstrap](https://getbootstrap.com/)
	- The project uses **Bootstrap** to use icons and a more pleasant user experience.




## Testing

The most testing was done through building the site.
Tested a lot of unusual actions to try and "break" the site, and then fix it if needed.
Tested it on a small laptop, a large monitor, multiple phones and ofcourse used the browser's function to show the project on various screen sizes.
And also tested it on various browsers.


## Deployment

The changes made were commited through git and then later pushed to (https://github.com/SemSmit/designermarket).

But due to bugs the first repository I used was: (https://github.com/SemSmit/designmarket), the second (https://github.com/SemSmit/designersmarket)
and the third and final one: (https://github.com/SemSmit/designermarket)


Heroku automatically retrieves these files from git when pushed and then builds the app on heroku.
The ENV.py values like SECRET_KEY are stored in the config vars of Heroku, so it can run properly.

I deployed the site using Heroku.
The site can be found on: (https://designmarket.herokuapp.com/)


###Local Deployment
Install Python version 3 or higher.
Create a virtual environment using "python3 -m venv path/to/virtual/env"
to run, go to your local virtual environment in your terminal and type 'source venv/scripts/activate', then go to ......./designmarket 
then use "pip3 install -r requirements.txt" to install the python packages for this project.
Then in ...../designmarket type "./manage.py runserver" to build&run the app.

The link where you can see your app is shown in your terminal.


## Credits

  Thanks to the StackOverflow and the tutors of CodeInstitute for helping me out a few times
  And to my mentor Ignatius Ukwuoma for giving me tips throughout the project

### Additional notes
	- The Cart and Checkout app were mostly copied from CodeInstitute's lessons.
	
	- Due to lack of time, and my access to the course being ended in five minutes from now,
	I unfortunately couldn't implement everything like I wanted. Building this project took me more time than expected, 
	probably due to bugs.
	And I just didn't have a lot of time.
	I hope you give me points on what is there, not on what isn't.

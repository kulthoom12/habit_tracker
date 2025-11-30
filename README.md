# Habit_Tracker

## Project Rationale

Habits Tracker is a web application made with Django that helps users keep track of, create, dleete  and look after their daily habits. User’s can add new habits, check there progress, tick off ones they’ve finished, edit any details that changed, and delete habits they don’t need anymore. Each user has their own private account so all their habit info stays personal and secure, without anyone else being able to see it. The whole idea was to make something simple that isn’t over complicated or confussing for people to use.

This app is mainly made for people who want to build better routiens or just try get more organised in thier day-to-day life. It works well for anyone who struggles keeping on top of habits, forgets what they planned to do, or just wants something simple to help keep them motivated. 


## User Stories
  
- As  a user, I want to register so I can create an account and start tracking habits.

- As  a user, I want to login so I can access my personal d- As dashboard.

- As  a user, I want to logout so my account stays secure.

- As  a user, I want to create a habit so I can track my daily routines.

- As  a user, I want to edit a habit to update its name or details.

- As  a user, I want to delete a habit if I no longer need it.

- As  a user, I want to mark a habit complete so I can track my progress.

## Wireframes
<details>
<summary>Click here to view  the  Mobile, Tablet and Desktop  Wireframes</summary>


### Mobile Wireframes

Home Page:
Login Page:

### Tablet Wireframes

Home Page:
Login Page:

### Desktop Wireframes

Home Page:
Login Page:

</details>

### Features
###  Existing Features
#### navbar:
-The navbar shows up at the top of every page so ppl can find their way around easier.
nav-links: 
Home (where the list of habits is)
Login / Register (only if the user isn’t signed in)
Logout (only shown when the user is logged in)

When someone logs in, the navbar “switches” so the login link switches to a logout button.

On mobile screens the navbar collapses down into a lil hamburger menu thanks to Bootstrap’s responsive classes (so it doesn’t take up the whole screen).

The logo/link of“Habit Tracker” always links back to the homepage.

Desktop navbar
![screenshot](navbar)

#### home page
This page shows all the habits for the user who’s currently logged in n is responsive
each habit shows following:
-  A checkbox so you can tick it off for the day
- A  The habit title 
- An Edit button
- A Delete button

and an add Habit” button so users can quickly add a new habit.

#### EDIT Page
edit page allowing users to add a title, description frewuency and a completed today checkbox. submitting the form saves hbaut to user acc  directing them to homw page/ 
![screenshot](editopage)

#### delete button
Users may delte habits from the home page via a red delete buton.

Habit deletion requiers confirmation via a dedicated delete rout, ensuring the user does not accidnetally remove a habit.

Only the habit owner is alowed to delete a habit 

## User Authentiaction (Login, Logout, Register)

Secure user authentiction is implemented using Django’s built-in forms.

Register Page

Allows new users to creat an account

Automaticaly logs them in upon succesful registration

Login Page

Uses Django AuthenticationForm

Provides error feedbak for incorect credentials

Logout

Ends the sesson and redirects users to the login page.



###  Future  Features

Habit Categrories

- Group habbits by type (health, work, personal) to keep things orgnized.

Dashboard Themes

L- ight/dark mode or custom thems so users can pick what looks best.

Password Reset

- Users can resset forgotten passwords via an email link.

Two-Factor Auth

- Optional 2FA for extra securtiy at login.

## Tools & Technologies Used

- https://www.w3schools.com/css/
- https://www.w3schools.com/html/
- https://www.w3schools.com/python/
- https://getbootstrap.com/docs/5.0/getting-started/introduction/
- https://www.djangoproject.com/
- https://www.sqlite.org/
- https://pypi.org/project/python-decouple/
- https://docs.djangoproject.com/en/stable/topics/security/
- http://whitenoise.evans.io/en/stable/
- https://render.com/
- https://github.com/
- https://pip.pypa.io/
- https://black.readthedocs.io/en/stable/

## Credits
- https://www.youtube.com/watch?v=-tyBEsHSv7w
- https://www.youtube.com/watch?v=HyN51x01Ve8
-  https://www.youtube.com/watch?v=uvISKB2ROrQ
-  https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
-  https://www.youtube.com/watch?v=F5mRW0jo-U4
-  https://www.youtube.com/watch?v=akXfF066MY0&t=20s
- https://www.youtube.com/watch?v=H_cWdD-aXCQ
- https://www.youtube.com/watch?v=nXe4mZs1hHQ
- https://www.youtube.com/watch?v=qKS87S0Imsk
-  https://www.youtube.com/watch?v=vzBFJ3WEvOQ


## Database and Relationship

- The Habit Tracker app uses a relational databse.
- Every user can have many habits. 
- This is done by adding a foreign key in the Habit model: user = models.ForeignKey(User, on_delete=models.CASCADE).
- Every habit belongs to one user only.
- If a user is deletd, all of their habits get removed too, helping keep data integraty.
- Each habit has properties like:

  - title,  descrption,  frequency , whether it was completed today , streak count
, date it was created,.
This setup makes sure that data is stored consistantly and in a organized way., It also keeps the relationship between users and their habbits clear.

## Deployment


# Habit_Tracker

## Project Rationale

Habits Tracker is a web application made with Django that helps users keep track of, create, dleete  and look after their daily habits. User’s can add new habits, check there progress, tick off ones they’ve finished, edit any details that changed, and delete habits they don’t need anymore. Each user has their own private account so all their habit info stays personal and secure, without anyone else being able to see it. The whole idea was to make something simple that isn’t over complicated or confussing for people to use.

This app is mainly made for people who want to build better routiens or just try get more organised in thier day-to-day life. It works well for anyone who struggles keeping on top of habits, forgets what they planned to do, or just wants something simple to help keep them motivated. 


## User Stories

## Wireframes
### Mobile Wireframes
### Tablet Wireframes
### Desktop Wireframes

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


## Tools & Technologies Used
## Credits



## Database and Relationship

## Deployment


### HTML Validator

<details>
<summary>Click here to view the HTML  Validator  </summary>

| **PAGE** | **Before** | **After** |
|----------|------------|-----------|
| HTML     | ![Before Screenshot]() | ![After Screenshot]() |

</details>

### CSS Validator

<details>
<summary>  Click here to view the CSS Validator </summary>

| **PAGE** | **Before** | **After** |
|----------|------------|-----------|
| CSS     | ![Before Screenshot]() | ![After Screenshot]() |

</details>

## Browser Performance

<details>
<summary>Click here to view the Browser Compatibility  or habit tracker</summary>

| Browser          | Screenshot |
|------------------|------------|
| Chrome           | ![Chrome Screenshot]() |
| Opera            | ![Opera Screenshot]() |
| Brave            | ![Brave Screenshot]() |
| Mozilla Firefox  | ![Firefox Screenshot]() |

</details>

## Responsiveness

<details>
<summary>Click here to view responsiveness screenshots</summary>

| Responsiveness          | Screenshot |
|-----------------|------------|
| Mobile          | ![Mobile Screenshot]() |
| Tablet          | ![Tablet Screenshot]() |
| Laptop / Desktop| ![Laptop Screenshot]() |

</details>

## Device Testing 

<details ><summary>Click here to view the Device Testing</summary>

| Device | Screenshot |
|--------|------------|
| Mobile | ![Mobile Screenshot]() |
| Tablet | ![Tablet Screenshot]() |
| Laptop | ![Laptop Screenshot]() |

</details>

## Lighthouse Audit

<details>
<summary>Click here to view the Lighthouse Audit </summary>

| **Lighthouse Audit** | **Screenshot** |
|---------------------|----------------|
| Mobile              | ![Mobile Screenshot]() |
| Tablet              | ![Tablet Screenshot]() |
| Laptop              | ![Laptop Screenshot]() |

</details>

## User Story Testing

<details>
<summary>Click here to view the User Story Testing</summary>

| **User Story** | **Testisting** | **Screenshot** |
|----------------|--------------------|----------------|
| As a user I want to regster so I can make acccount and start track my habbits. | The user fill in the registrtion form (`register.html`) and make an acccount. If succes, user is loged in and redirect to dashbord (`home`). Shows erros if somthing wrong. | ![Register Screenshot]() |
| As a user I want to logn so I can go to my dashbord. | User put credentails in login form (`login.html`). If correct, user go to dashbord. Wrong credentails show erro. | ![Login Screenshot]() |
| As a user I want to logout so my acccount stay safe. | User click logout buton in navbr. Session ends and user go back to login page. | ![Logout Screenshot]() |
| As a user I want create a habbit to track my daily rutines. | User fill habbit form (`form.html`) with titel, descripton, frequncy and done status. Habbit save in databse and show in dashbord. | ![Create Habit Screenshot]() |
| As a user I want edit a habbit to change name or info. | User edit existng habbit and change detals. Save changes in datbase and show in dashbord. | ![Edit Habit Screenshot]() |
| As a user I want delete a habbit if I dont need it. | User click delete buton next to habbit. Habbit removed from databse and gone from dashbord. | ![Delete Habit Screenshot]() |

</details>


## Testing Existing Features

<details>
<summary>Click here to view the Feature Testing</summary>

| **features** | **what  was tested** | **Screenshot** |
|--------------------------------|-------------------|----------------|
| Navbar                        | User click links in navabr to go pages                   | ![Navbar Screenshot]() |
| Homepage                      | User open home page                                       | ![Homepage Screenshot]() |
| Edit Page                      | User change habbit info and click save                   | ![Editpage Screenshot]() |
| Delete Button                  | User click delete next to habbit                           | ![Delete Screenshot]() |
| Login                          | User enter email and pass to login                        | ![Login Screenshot]() |
| Register                       | User fill register form                                    | ![Register Screenshot]() |
| Logout                         | User click logout                                          | ![Logout Screenshot]() |

</details>

## CRUD Functionality Tests

<details>
<summary>Click here to view the CRUD  Tests</summary>

| **Action** | **What User Does** | **Screenshot** |
|------------|---------------------------|----------------|
| Create     | User fill in habbit form and click submit to add new habbit | ![Create Screenshot]() |
| Edit       | User select existng habbit, update info and open edit form | ![Edit Screenshot]() |
| Save       | User edit habbit and click save to update it in databse | ![Save Screenshot]() |
| Delete     | User click delete buton next to habbit to remove it | ![Delete Screenshot]() |
| Toggle     | User click "Completed Today" checkbok to mark habbit done/undone | ![Toggle Screenshot]() |

</details>

## Bugs

<details>
<summary>Click here to view Bugs </summary>

| file     |  / What was wrong | How it was fixed |
|----------------|--------------------|-----------------|
| form.html      | Django cudnt understnd the if habit else in input fields. Form broked. | Changed code so input fields only show habit info if it exists. If no habit, fields stay empty. |
| index.html     | {% endblock %} gave error. Template tag maybe wrong or not inherited. | Fixed template so it extends base template proper and all {% block %} tags closed. |
| homepage.html  | Habits not showing. {% if habits %} not working or view didnt pass habits. | Made sure view sends habits to template and loop show them correctly. |
| base.html      | Django cudnt find URL pattern named task_create. | Added URL in urls.py called task_create to link to right view. |
| init__.py    | Django expected number but got SimpleLazyObject (AnonymousUser). Crash happend. | Added check so code only use user info if logged in. Anonymous users dont break it. |

</details>


## Unfixed Bugs
<details>
<summary>Click here to view the unfixed Bugs </summary>

</details>
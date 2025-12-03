### HTML Validator

<details>
<summary>Click here to view the HTML Validator</summary>

| **Page**       | **Before** | **After** |
|----------------|------------|-----------|
| login.html     | ![Before Screenshot](habits/static/images-testing/html-login.png) | No change |
| form.html      | ![Before Screenshot](habits/static/images-testing/html-form-before.png) | ![After Screenshot](habits/static/images-testing/html-form-after.png) |
| register.html  | ![Before Screenshot](habits/static/images-testing/html-register.png) | ![After Screenshot](habits/static/images-testing/html-register-after.png) |

</details>

### CSS Validator

<details>
<summary>Click here to view the CSS Validator</summary>

| **Page** | **Before** | **After** |
|----------|------------|-----------|
| CSS      | ![Before Screenshot](habits/static/images-testing/css-before.png) | ![After Screenshot](habits/static/images-testing/css-after.png) |

</details>

## Browser Performance

<details>
<summary>Brave</summary>

| Page | Screenshot |
|------|------------|
| Login  | ![](habits/static/images-testing/brave-login.png) |
| Register  | ![](habits/static/images-testing/brave-register.png) |
| Save Habit  | ![](habits/static/images-testing/brave-save.png) |
| Edit/Delete  | ![](habits/static/images-testing/brave-edit-delete.png) |

</details>

<details>
<summary>Chrome</summary>

| Page | Screenshot |
|------|------------|
| Login | ![](habits/static/images-testing/chrome-login.png) |
| Register | ![](habits/static/images-testing/chrome-register.png) |
| Save Habit | ![](habits/static/images-testing/chrome-save.png) |
| Edit/Delete Habit | ![](habits/static/images-testing/chrome-edit-delete.png) |

</details>

<details>
<summary>Opera</summary>

| Page | Screenshot |
|------|------------|
| Login  | ![](habits/static/images-testing/opera-login.png) |
| Register  | ![](habits/static/images-testing/opera-register.png) |
| Save Habit  | ![](habits/static/images-testing/opera-save.png) |
| Edit/Delete Habit  | ![](habits/static/images-testing/opera-edit-delete.png) |

</details>

<details>
<summary>Mozilla</summary>

| Page | Screenshot |
|------|------------|
| Login  | ![](habits/static/images-testing/mozilla-login.png) |
| Register  | ![](habits/static/images-testing/mozilla-register.png) |
| Save Habit  | ![](habits/static/images-testing/mozilla-save.png) |
| Edit/Delete Habit  | ![](habits/static/images-testing/mozilla-edit-delete.png) |

</details>

## Responsiveness

<details>
<summary>Click here to view responsiveness screenshots</summary>

| Responsiveness | Screenshot |
|----------------|------------|
| Mobile         | ![Mobile Screenshot](habits/static/images-testing/responsiveness-mobile.png) |
| Tablet         | ![Tablet Screenshot](habits/static/images-testing/responsiveness-tablet.png) |
| Laptop         | ![Laptop Screenshot](habits/static/images-testing/responsiveness-laptop.png) |

</details>

## Lighthouse Audit

<details>
<summary>Click here to view the Lighthouse Audit</summary>

| **Lighthouse Audit** | **Screenshot** |
|----------------------|----------------|
| Mobile               | ![Mobile Screenshot](habits/static/images-testing/lighthouse-mobile.png) |
| Laptop               | ![Laptop Screenshot](habits/static/images-testing/lighthouse-desktop.png) |

</details>

## User Story Testing

<details>
<summary>Click here to view the User Story Testing</summary>

| As a user I want to register so I can make account and start track my habits. | The user fill in the registration form (`register.html`) and make an account. If success, user is logged in and redirect to dashboard (`home`). Shows errors if something wrong. | ![Register Screenshot](habits/static/images-testing/user-testing-register.png) |
| As a user I want to login so I can go to my dashboard. | User put credentials in login form (`login.html`). If correct, user go to dashboard. Wrong credentials show error. | ![Login Screenshot](habits/static/images-testing/user-testing-login.png) |
| As a user I want to logout so my account stay safe. | User click logout button in navbar. Session ends and user go back to login page. | ![Logout Screenshot](habits/static/images-testing/user-testing-logout.png) |
| As a user I want create a habit to track my daily routines. | User fill habit form (`form.html`) with title, description, frequency and done status. Habit save in database and show in dashboard. | ![Create Habit Screenshot](habits/static/images-testing/user-testing-add.png) |
| As a user I want edit a habit to change name or info. | User edit existing habit and change details. Save changes in database and show in dashboard. | ![Edit Habit Screenshot](habits/static/images-testing/user-testing-edit-habit.png) |
| As a user I want delete a habit if I dont need it. | User click delete button next to habit. Habit removed from database and gone from dashboard. | ![Delete Habit Screenshot](habits/static/images-testing/user-testing-edit-delete.png) |

</details>

## Testing Existing Features

<details>
<summary>Click here to view the Feature Testing</summary>

| **Features** | **What was tested** | **Screenshot** |
|--------------|-------------------|----------------|
| Navbar       | User click links in navbar to go pages | ![Navbar Screenshot](habits/static/images-testing/existing-navbar.png) |
| Homepage     | User open home page | ![Homepage Screenshot](habits/static/images-testing/existing-home.png) |
| Edit         | User change habit info and click save | ![Editpage Screenshot](habits/static/images-testing/existing-edit.png) |
| Delete Button | User click delete next to habit | ![Delete Screenshot](habits/static/images-testing/existing-delete.png) |
| Login        | User enter email and pass to login | ![Login Screenshot](habits/static/images-testing/user-testing-login.png) |
| Register     | User fill register form | ![Register Screenshot](habits/static/images-testing/existing-register.png) |
| Logout       | User click logout | ![Logout Screenshot](habits/static/images-testing/user-testing-logout.png) |

</details>

## CRUD Functionality Tests

<details>
<summary>Click here to view the CRUD Tests</summary>

| **Action** | **What User Does** | **Screenshot** |
|------------|------------------|----------------|
| Create     | User fill in habit form and click submit to add new habit | ![Create Screenshot](habits/static/images-testing/crud-create.png) |
| Edit       | User select existing habit, update info and open edit form | ![Edit Screenshot](habits/static/images-testing/crud-edit.png) |
| Save       | User edit habit and click save to update it in database | ![Save Screenshot](habits/static/images-testing/crud-save.png) |
| Delete     | User click delete button next to habit to remove it | ![Delete Screenshot](habits/static/images-testing/curd-delete.png) |
| Toggle     | User click "Completed Today" checkbox to mark habit done/undone | ![Toggle Screenshot](habits/static/images-testing/crud-toggle.png) |

</details>

## Bugs

<details>
<summary>Click here to view Bugs</summary>

| File         | What was wrong | How it was fixed |
|--------------|----------------|-----------------|
| form.html    | Django couldn't understand the if habit else in input fields. Form broke. | Changed code so input fields only show habit info if it exists. If no habit, fields stay empty. |
| index.html   | {% endblock %} gave error. Template tag maybe wrong or not inherited. | Fixed template so it extends base template properly and all {% block %} tags closed. |
| homepage.html | Habits not showing. {% if habits %} not working or view didn't pass habits. | Made sure view sends habits to template and loop show them correctly. |
| base.html    | Django couldn't find URL pattern named task_create. | Added URL in urls.py called task_create to link to right view. |
| init__.py    | Django expected number but got SimpleLazyObject (AnonymousUser). Crash happened. | Added check so code only use user info if logged in. Anonymous users don't break it. |

</details>

## Unfixed Bugs

No bugs found to my knowledge.
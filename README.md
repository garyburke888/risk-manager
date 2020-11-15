# eRisk

![eRisk Responsive Design](/static/images/erisk_multi.png)

[View the live app here.](http://flask-risk-manager-project.herokuapp.com/)

**eRisk** a 'Risk Management' app primarily aimed at 'Project Management' but appropriate for use by corporations, organisations and individuals alike. The app requests that all users register and login to view the 'Risk Register' associated with their particular project. Once logged in the user can then create, read, update and delete their 'Risks'. In line with current 'Risk Management' process each 'Risk' contains the following editable fields: Risk Name, Risk Description, Risk Owner, Likelihood Rating, Impact Rating, Overall Rating, Mitigating Action, Contingent Action, Progress on Actions, Date Raised and Risk Status. The app is optimized for use on phones and tablets.

## User Experience (UX)

### User stories
-   #### First Time User Goals
    1. As a first time user, I want to see that the app meets my needs or those of my organisation.
    2. As a first time user, I want to easily navigate throughout the app to find content.
    3. As a first time user, I want to see that I can quickly and easily input relevant information.
-   #### Returning User Goals
    1. As a returning user, I want to create and read Risks.
    2. As a returning user, I want to share my Risks with other members of my team.
    3. As a returning user, I want help rating Risks.
-   #### Frequent User Goals
    1. As a frequent user, I want to update and delete Risks.
    2. As a frequent user, I want to create and manage Risk Owners.
    3. As a frequent user, I want to view and manage the status of Risks.
-   #### Owner Goals
    1. As the app owner, I want to provide a clean and easy-to-use app that appeals to a certain market.
    2. As the app owner, I want to ensure the app provides industry-standard functionality.
    3. As the app owner, I want to sell other apps to users.

### Design
-   #### Colour Scheme
    -   The two main colours used are teal and white.
-   #### Typography
    -   Roboto 2.0 is the standard font used by the Materialize framework, which is utilised by this app.
-   #### Imagery
    -   There is little imagery used in the app, just a favicon and a popup risk matrix - to help users compile ratings.

### Wireframes

![eRisk Wireframes](/static/images/erisk_wireframe_1.png)
![eRisk Wireframes](/static/images/erisk_wireframe_2.png)

## Features

-   Responsive on all device sizes.
-   User registration, login & logout.
-   Create, read, update and delete functionality.
-   Search functionality.
-   Confirm delete functionality.
-   Materialize Collapsible Risk Register.
-   Risk Rating Guide modal.
-   Mobile collapse nav bar.
-   Different user permissions (Admin/User)

![eRisk Index / Login / Register / Profile](/static/images/erisk_screenshots_1.png)
![eRisk Add / Edit / Matrix](/static/images/erisk_screenshots_2.png)
![eRisk Delete / Owners](/static/images/erisk_screenshots_3.png)

## Technologies Used

### Languages

-   [HTML](https://www.w3schools.com/html/)
-   [CSS](https://www.w3schools.com/css/)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs

-   [Flask](https://flask.palletsprojects.com/)
    - Flask was used to develop the app.
-   [Materialize](https://materializecss.com/)
    - Materialize was used to assist with the responsiveness and styling of the website.
-   [Font Awesome](https://fontawesome.com/)
    - Font Awesome icons are used throughout the app.
-   [jQuery](https://jquery.com/)
    - jQuery was used in conjunction with Materialize to initialise components.
-   [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub & Heroku.
-   [GitHub](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
-   [MongoDB](https://www.mongodb.com/)
    - MongoDB was the database chosen for use with this app.
-   [Werkzeug](https://werkzeug.palletsprojects.com/)
    - Werkzeug was used for its generate and check password hash functionality.

## Testing

### Code
-   The W3C Markup & CSS Validators [here](https://validator.w3.org/) were used to ensure there were no critical syntax errors in the project.
-   The PEP8 online checker [here](http://pep8online.com/) was used to check Python code for PEP8 requirements.

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a first time user, I want to see that the app meets my needs or those of my organisation.

        1. The full workings of the app are apparent from first time use.
        2. The minimalist design allows users to quickly 'Register'/'Login' and see what the 'Risk Register' contains and how to edit or add to it.
        3. The 'Profile' page gives information on user permissions with regards to create, read, update and delete rights.

    2. As a first time user, I want to easily navigate throughout the app to find content.

        1. The app has been designed to be minimalist, with concise information and as few links as possible. 
        2. The 'Risk Register' itself appears as a collapsible list as each 'Risk' contains a lot of information, all of which is industry standard.
        3. The user permissions are slightly different for 'admin' as compared to a regular user and with this in mind, 'Risk Owner' links don't appear for regular users. (to test this, login as 'admin' with password 'adminpassword')

    3. As a first time user, I want to see that I can quickly and easily input relevant information.
        1. The 'Login' and 'Register' pages only contain 2 input fields.
        2. The 'Add Risk' link is in the main menu.
        3. The 'Add Owner' link is in the main menu for admin. (to test this, login as 'admin' with password 'adminpassword')

-   #### Returning Visitor Goals

    1. As a returning user, I want to create and read Risks.

        1. The 'Add Risk' link is in the main menu for all users.
        2. The 'Risk Register' link is in the main menu for all users.
        3. The 'Risk Register' is a collapsible list, all information on a 'Risk' can be viewed by clicking the 'Risk' title.

    2. As a returning user, I want to share my 'Risks' with other members of my team.

        1. There is no limit to how many users can register, login and view the 'Risk Register'.
        2. All 'Risks' are visible the whole team.
        3. 'Risks' can only be edited or deleted by the user who created them, or by admin.

    3. As a returning user, I want help rating Risks.
        1. Each 'Risk Rating' (Likelihood, Impact & Overall) is colour coded for Low, Medium and High.
        2. The 'Add Risk' form contains a popup 'Risk Matrix' to help users make more precise ratings.
        3. The 'Edit Risk' form contains the same popup.

-   #### Frequent User Goals

    1. As a frequent user, I want to update and delete Risks.

        1. The 'Edit' and 'Delete' button links are visible within each 'Risk'. 
        2. 'Risks' can only be edited or deleted by the user who created them, or by admin.
        3. To delete a 'Risk' the user will be prompted to confirm they wish to do so.

    2. As a frequent user, I want to create and manage Risk Owners.

        1. The 'Manage Owners' link is only visible to admin.
        2. The 'Add Owner', 'Delete Owner' & 'Edit Owner' button links are only visible to admin. 
        3. To delete a 'Risk Owner' the user will be prompted to confirm they wish to do so.

    3. As a frequent user, I want to view and manage the status of Risks.

        1. 'Risk Status' can be changed from within the 'Edit Risk' form, via a Materialize switch.
        2. 'Risk Status' is quickly visible through locked/unlocked icons beside each 'Risk' in the 'Risk Register'.
        3. These icons are tool-tipped to state if a 'Risk Status' is open or closed.

-   #### Owner Goals

    1. As the app owner, I want to provide a clean and easy-to-use app that appeals to a certain market.
        -   The app has been designed to be minimalist, with concise information and as few links as possible.
    2. As the app owner, I want to ensure the app provides industry-standard functionality.
        -   The 'Risk Register' contains industry-standard fields and information.
    3. As the app owner, I want to sell other apps to users.
        -   The footer contains a link which can be used to take the user to advertisements for other apps that they might be interested in.

### Further Testing

-   The Website was tested on Google Chrome, Opera, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone.
-   A large amount of testing was done to ensure there were no broken links.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   Despite requesting that a user registers and logs in, any page is visible in the browser by copying and pasting the full web address.
-   The 'Risk Matrix' modal appears with a scrollbar on tighter landscape screens, which is not optimal.

## Deployment

### Heroku

The project was deployed to Heroku using the following steps;

1. ???

## Credits

### Tutorial
-   This app was built in conjunction with The Code Institute 'Data Centric Development' module.

### Code & Content
-   [Am I Responsive?](http://ami.responsivedesign.is/) - Used to obtain README image of app on various screens.
-   [Materialize](https://materializecss.com/) - Used throughout the project mainly for responsive navigation and the collapsible list components.

### Acknowledgements

-   Mentor - Gerry McBride
-   Tutor Support - Code Institute
-   Developer - Gary Burke
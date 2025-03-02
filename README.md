# FlavorFrames API

## Code Institute Portfolio Project 5

Welcome to the backend of FlavorFrames, a platform designed for food enthusiasts to share and discover popular eateries and hidden gems. You can find detailed information on the frontend implementation [here](https://github.com/Maximiliane-K/flavorframes).

In an era where food crawls, mukbangs, and street food adventures are widely shared, FlavorFrames makes it easy for users to showcase their favorite finds. Whether it’s a hidden café, a must-visit food stall, or a trending restaurant, the platform helps users connect through their culinary discoveries.

FlavorFrames focuses exclusively on food and drinks, making it easier to find trending spots in your city or while traveling.

The FlavorFrames API powers the platform by providing essential functionalities that allow users to share and engage with food content. 
Users can create, update, and delete posts that include images, written descriptions, and location tags. They can follow other users, like and comment on posts, and engage with the community. Additionally, users can create, update, and delete events, which feature images, descriptions, event dates, and categorized event types. Users also have the option to mark themselves as attending an event if they are interested.

To enhance the experience, the API also includes search and filtering capabilities, making it easier to discover posts that match individual tastes and interests.

You can view the live API [here](https://flavorframes-drf-api-571215953f7d.herokuapp.com/).

## **Table Of Contents**
 * [Strategy Plane](#strategy-plane)
   * [Agile Project Management](#agile-project-management)
   * [Developer User Stories](#developer-user-stories)
  * [Structure Plane](#structure-plane)
    * [Features](#features)
  * [Skeleton Plane](#skeleton-plane)
    * [Database Shema](#database-shema)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks and Software](#frameworks-and-software)
* [Testing](#testing)
* [Deployment](#deployment)
  * [Deploying To Heroku](#deploying-to-heroku)
* [Forking The Repository](#forking-the-repository)
* [Cloning The Repository](#cloning-the-repository)
* [Credits](#credits)
  * [Media](#media)
  * [Content](#content)
      
  ---
  
## Strategy Plane

#### Agile Project Management

This project was managed using agile methodologies, focusing on incremental feature delivery and iterative development. 

The backend work was structured into six epics, guiding the development process, and managed across four sprints to ensure an organized workflow.

The Kanban board and Project board can be viewed [here](https://github.com/users/Maximiliane-K/projects/14/views/2?layout=table&visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%2C%22Milestone%22%5D).

![Kanban board image](https://res.cloudinary.com/maxiscloud/image/upload/v1738670509/kanban-board-flavorframes_rbfw70.png)

![Project board image](https://res.cloudinary.com/maxiscloud/image/upload/v1738671974/project-board-flavorframes_gxdwvx.png)

#### Developer User Stories

**Profiles**
  - DUS 01 View All Profiles: As a developer or superuser, I can access a list of all user profiles so that I can manage and review the profiles created on the platform.
    
  - DUS 02 View a Single Profile: As a developer or superuser, I can view the details of an individual profile so that I can see specific user information when needed.
  
  - DUS 03 Edit Profile Information: As a developer or superuser, I can update a profile when logged in so that I can modify personal information as needed.
  
  - DUS 04 Delete a Profile: As a developer or superuser, I can delete a profile that I own so that I can remove my account and personal data from the API.
 
**Posts**

 - DUS 05 View All Posts: As a developer or superuser, I can access a list of all posts so that I can manage and review all published content.

 - DUS 06 View a Single Post: As a developer or superuser, I can view the details of an individual post, including comments, so that I can review its content and interactions.

 - DUS 07 Create a New Post: As a developer or superuser, I can create a new post so that it is displayed in the posts list and accessible to other users.

 - DUS 08 Edit a Post: As a developer or superuser, I can update a post that I created so that I can correct or improve its content as needed.

 - DUS 09 Delete a Post: As a developer or superuser, I can delete a post that I created so that I can remove its data from the API.

**Comments** 

- DUS 10 Create a Comment: As a developer or superuser, I can create a comment so that it is linked to a specific post.

- DUS 11 View All Comments: As a developer or superuser, I can access a list of all comments so that I can review and manage all comments in the API.

- DUS 12 Retrieve a Single Comment: As a developer or superuser, I can retrieve a comment by its ID so that I can view, edit, or delete it as needed.

- DUS 13 Edit a Comment: As a developer or superuser, I can update a comment that I created so that I can correct or improve its content.

- DUS 14 Delete a Comment: As a developer or superuser, I can delete a comment that I created so that I can remove its data from the API.

**Likes**

- DUS 15 Like a Post: As a developer or superuser, I can create a like object linked to a specific post so that I can indicate my appreciation for the post.

- DUS 16 Unlike a Post: As a developer or superuser, I can delete a like object that I created so that I can remove my like from a post.

- DUS 17 Restrict Unauthorized Like Deletion: As a developer or superuser, I cannot delete a like object that I did not create so that only the original user can remove their like.

- DUS 18 View All Likes: As a developer or superuser, I can access a list of all like objects so that I can review and manage all likes stored in the API.

**Followers**

- DUS 19 Follow a User: As a developer or superuser, I can create a follow object so that I can follow another user.

- DUS 20 View All Follows: As a developer or superuser, I can access a list of all follow objects so that I can review and manage all follow relationships in the API.

- DUS 21 Unfollow a User: As a developer or superuser, I can delete a follow object that I created so that I can unfollow another user.

**Events**

- DUS 22 View All Events: As a developer or superuser, I can access a list of all events so that I can manage and review all published events.

- DUS 23 View a Single Event: As a developer or superuser, I can view the details of an individual event, including attendees, so that I can review its content and user interactions.

- DUS 24 Create a New Event: As a developer or superuser, I can create a new event so that it is displayed in the events list and accessible to other users.

- DUS 25 Edit an Event: As a developer or superuser, I can update an event that I created so that I can correct or improve its content as needed.

- DUS 26 Delete an Event: As a developer or superuser, I can delete an event that I created so that I can remove its data from the API.

**Attendance**
- DUS 27 Register Event Attendance: As a developer or superuser, I can create an attendance record linked to a specific event and user so that a user is marked as attending.

- DUS 28 Revoke Attendance: As a developer or superuser, I can delete an attendance record if I am the user who created it so that users can revoke their attendance when they no longer plan to attend.

- DUS 29 Retrieve Event Attendees: As a developer or superuser, I can retrieve a list of all users attending a specific event so that I can review attendance.

- DUS 30 Restrict Unauthorized Attendance Modifications: As a developer or superuser, I cannot modify or delete another user's attendance.

**Search & Filter**

- DUS 31 Search for Posts and Events: As a developer or superuser, I can enter keywords into a search bar to find specific posts or events based on their title or description.

- DUS 32 View Events and Posts from Followed Profiles: As a developer or superuser, I can view a list of posts only from profiles I follow so that I can keep up with content from my preferred users.

- DUS 33 View Posts I Have Liked: As a developer or superuser, I can view a list of posts that I have liked so that I can revisit content I found interesting.

- DUS 34 View Events I Have Marked as Attending: As a developer or superuser, I can view a list of events where I have marked myself as attending so that I can easily track my planned events.

- DUS 35 View Posts and Events Created by a Specific Profile: As a developer or superuser, I can view a list of posts and events created by a specific user so that I can explore their content in one place.

- DUS 36 View Comments on a Specific Post: As a developer or superuser, I can view a list of comments on a specific post so that I can see all interactions related to it.

---

## Structure Plane


### **Features**

### Homepage
When entering the API site, you are directed to the Root Route homepage, with a message welcoming you to the API:

![Homepage](https://res.cloudinary.com/maxiscloud/image/upload/v1740864518/Screenshot_2025-03-01_at_22.27.34_ifo6na.png)


### Profile Data

Users can view a list of all profiles available in the API within the Profile List section.

![Profiles list](https://res.cloudinary.com/maxiscloud/image/upload/v1740865325/Screenshot_2025-03-01_at_22.41.55_d5qqt4.png)

Profile creation is not manually enabled, as it is handled automatically through the user registration process.

The Profile List section allows users to view all profiles available in the API.

The Profile model includes fields such as:

- owner
- created_at
- updated_at
- screenname
- city
- about
- profile_picture
  
Additionally, the ProfileSerializer enhances the JSON response with the following fields:

- is_owner 
- following_id 
- posts_count 
- events_count 
- followers_count
- following_count

Users can filter profiles in two ways:

- Profiles that are following the logged-in user.
- Profiles that are being followed by the logged-in user.
  
Profiles can also be sorted using:

- posts_count
- events_count
- followers_count
- following_count
- owner__user_follows__followed_at
- owner__user_followed_by__followed_at

Editing and Deleting Profiles

- Users cannot create a profile manually, as it is tied to their account.
  
If a user visits their own profile, they gain access to:

- A pre-filled form to edit profile details (city, about, profile_picture).
- A delete button to permanently remove their profile.


### Post Data 

Users can view a list of all posts available in the API within the Posts List section.

![Posts list](https://res.cloudinary.com/maxiscloud/image/upload/v1740866393/Screenshot_2025-03-01_at_22.59.41_ypyv89.png)

Each post includes an image, written content, and an optional Google Maps location link to highlight a specific place (e.g., a restaurant or cafe).

Posts are displayed in descending order based on their creation date.

In addition to the fields in the Post model, the PostSerializer enriches the JSON response with:

- is_owner 
- profile_image 
- like_id 
- likes_count 
- comments_count 

The ordering options for posts include:

- likes_count
- comments_count
- likes_created_at
  
The API also supports searching and filtering:

- Posts by followed users 
- Liked posts
- User’s own posts
  
If a user is logged in, they can create a new post that will appear in the posts list.

When a user views a post they own, additional edit and delete options become available:

- A pre-filled edit form allows the user to update the post details.
- A delete button allows them to remove the post permanently from the API.


### Events & Attendance Data 

Users can view a list of all events available in the API within the Events List section.

![Events & Attendance Data](https://res.cloudinary.com/maxiscloud/image/upload/v1740867087/Screenshot_2025-03-01_at_23.11.18_tuaydl.png)

Besides the fields defined in the Event model (as shown in the ERD Diagram), additional fields have been added through the serializer to enhance the JSON response:

- is_owner
- profile_image
- user_status (indicates if the current user is attending or interested in the event)

The Events List allows filtering and ordering of events based on the following parameters:

- event_date (chronological order)
- category (filtering events by type)
- created_at (most recent events first)
  
Filtering Options:

- Events created by users the logged-in user follows ('Event Feed' page).
- Events the logged-in user has marked as attending ('My Events' page).
- Events created by a specific user (profile page).
  
If a user is logged in, they can create new events by submitting a form.

Additionally, if a user views an event they created, they gain access to Edit and Delete functionalities, allowing them to update or remove the event from the API.

#### Event Attendance:

Users have the option to mark themselves as attending or interested in an event. 
This functionality is managed through the Event Attendance model, which records each user's status for a given event.

Through the EventAttendanceSerializer, the following data is included in the JSON response:

- user
- profile_image
- event
- status (whether the user is "attending")
  
Attendance Features:
- A user can mark themselves as attending an event.
- A user can revoke their attendance by clicking the button again.
- A list of attendees for an event is displayed so users can see who is going.
  
Attendance records are unique per user and event to ensure accuracy.


### Comments Data
Users can view all comments available in the API within the Comments List section.

![Comment Data](https://res.cloudinary.com/maxiscloud/image/upload/v1740867817/Screenshot_2025-03-01_at_23.23.27_riscsq.png)

Besides the fields defined in the Comment model (as shown in the ERD Diagram), additional fields have been added through the serializer to enhance the JSON response:

- is_owner
- profile_id
- profile_image
- created_at and updated_at
  
To improve data accessibility, comments can be filtered by the post they are associated with, 
allowing users to see all comments related to a specific post. 

Additionally, comments are ordered by creation date, with the most recent appearing first.

Commenting Features:

- Logged-in users can create a new comment by selecting the post they wish to comment on and entering text.
- Users can edit or delete their own comments from the API.
- A pre-populated form is available when editing a comment.
- A delete button allows users to remove their own comments.
  
This setup ensures that users can actively engage with posts through commenting while maintaining control over their contributions.


### Likes Data 

Users can view a list of all likes within the Likes List section.

Each like is associated with a user and a post, ensuring that users can engage with content by liking posts.

Like Functionality:
- Logged-in users can like a post by selecting it.
- Users cannot like the same post twice—an error message is displayed if they attempt to do so.
- Users cannot like their own posts — attempting to do so will also result in an error.
- Likes are ordered by timestamp, with the most recent likes appearing first.

Deleting Likes:
- Once logged in, users can remove their own likes by interacting with the same post.
- If a user tries to delete a like that does not belong to them, the action is not permitted.
  
This setup ensures that users can interact with posts while preventing duplicate or self-likes, maintaining a fair engagement system.


### Followers Data

Within the Followers List section, users can view a list of all follow relationships in the API.

![Followers data](https://res.cloudinary.com/maxiscloud/image/upload/v1740871262/Screenshot_2025-03-02_at_00.20.53_v0ayfb.png)

If a user is logged in, they can follow another user by selecting their profile. 
This action creates a follow relationship, allowing them to see updates from that profile.

To prevent duplicate relationships, the system ensures that a user cannot follow the same profile more than once. 

If a user attempts to follow someone they are already following, they receive an error message informing them that the follow action is not possible. 

Similarly, a user cannot follow themselves.

Users can also unfollow profiles they are following. However, editing a follow relationship is not possible — users can only create or delete follows.

---

## Skeleton Plane

#### **Database Shema**

**Entity-Relationship Diagram (ERD)**

The relationships between the models are visualized in the following Entity-Relationship Diagram (ERD):

![Entity relationship diagram](https://res.cloudinary.com/maxiscloud/image/upload/v1740873448/Screenshot_2025-03-02_at_00.52.03_ekbvhd.png)

I have structured the database for FlavorFrames API with the following models:

- Users (Managed by Django’s built-in authentication system)
- Profiles (Automatically created upon user registration)
- Posts (Users can create and share posts with descriptions and location links)
- Likes (Users can like posts)
- Comments (Users can comment on posts)
- Events (Users can create and manage food-related events)
- Event Attendance (Users can mark themselves as attending in an event)
- Followers (Users can follow other users)
  
Notes on the ER Diagram:

- The Users table is not explicitly declared in the models but is managed by Django's authentication system.
- The Profiles table is linked one-to-one with Users and stores additional profile information.
- The Event Attendance model connects users with events, allowing them to mark their attendance.
  
The relationships illustrated reflect the logical structure of the database, not necessarily all physical constraints.

--- 

## Technologies

### Languages

[Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>) – The core language used to build the backend API with Django Rest Framework (DRF).

---

### Frameworks and Software

- [Django Rest Framework](https://www.django-rest-framework.org/) - Used to build and manage the API functionalities.
- [PEP8 Validation](https://pypi.org/project/pep8/) - Ensures Python code follows the PEP 8 style guide for readability and consistency.
- [Github](https://github.com/) - Hosts the repository, tracks commit history, and manages the project board for user stories.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - Cloud platform used to deploy and run the API.
- [Cloudinary](https://cloudinary.com/) - Handles image hosting and management for the project.

---

### Libraries 

The backend is built using Django Rest Framework (DRF) and relies on several key libraries for functionality. 
Below is an overview of the most important dependencies included in the requirements.txt file:

asgiref – Handles asynchronous communication in Django applications.

cloudinary – Manages image uploads and storage with Cloudinary.

dj-database-url – Simplifies database configuration using environment variables.

dj-rest-auth – Provides API endpoints for user authentication in DRF.

Django – The core Python framework used for the backend.

django-allauth – Enables user authentication and social login integration.

django-cloudinary-storage – Integrates Cloudinary as the storage solution for media files.

django-cors-headers – Adds Cross-Origin Resource Sharing (CORS) support.

django-filter – Enables filtering of querysets through URL parameters.

django-location-field – Provides location-based fields for Django models.

djangorestframework – The core package enabling REST API functionality in Django.

djangorestframework-simplejwt – Implements JWT authentication for API security.

gunicorn – A WSGI HTTP server for deploying Django applications.

oauthlib – Handles OAuth authentication logic.

pillow – Supports image processing and manipulation.

psycopg2 – PostgreSQL database adapter for Django.

PyJWT – Implements JSON Web Token (JWT) authentication.

python3-openid – Adds OpenID authentication support.

pytz – Provides timezone support in Python.

requests-oauthlib – OAuth authentication support for HTTP requests.

sqlparse – Parses and formats SQL queries for readability.

For a full list of dependencies, refer to the requirements.txt file.


---

## Testing

Please click [here]() to read more about the testing process for the FlavorFrames API

---

## Deployment

### Deploying To Heroku

The FlavorFrames API is deployed to Heroku, using a PostgreSQL database. To replicate the deployment, follow these steps:

1. Set Up GitHub Repository
  - Create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by clicking ‘Use this template’.
  - Fill in the details and click ‘Create Repository From Template’.
  - Once the repository is created, open the project in VS Code (or your preferred IDE).

2. Install Dependencies
  - Install Django and the required libraries:
    - pip3 install 'django<4' gunicorn
    - pip3 install dj_database_url psycopg2
    - pip3 install dj3-cloudinary-storage

  - Create a requirements.txt file:
    - pip3 freeze --local > requirements.txt
    
3. Create Django Project and Apps
  - Start a new Django project:
    - django-admin startproject YOUR_PROJECT_NAME .
  
  - Create the required Django apps:
    - python3 manage.py startapp APP_NAME
      
  - Add the apps to INSTALLED_APPS in settings.py.

4. Migrate and Run the Server
  - Prepare and apply database migration
    - python3 manage.py makemigrations
    - python3 manage.py migrate

5. Deploy to Heroku
   5.1 Create a Heroku App
     - Log in to Heroku, click "New" -> "Create New App".
     - Choose a unique app name, select a region, then click "Create App".

   5.2 Attach PostgreSQL Database
     - Copy your DATABASE_URL:
       - heroku config
     - In Heroku, go to Settings → Reveal Config Vars, add:
       - DATABASE_URL: your_database_url
       - SECRET_KEY: your_secret_key
       - CLOUDINARY_URL: your_cloudinary_url
       - ALLOWED_HOSTS: your_heroku_app_name.herokuapp.com
       
6. Connect GitHub & Deploy
  - In Heroku, go to Deploy -> select GitHub as the deployment method.
  - Search for your repository and connect it.
  - Under Manual Deploy, select main and click "Deploy Branch".

7. Set Up Cloudinary for Media Storage
  - Log in to Cloudinary, copy your API Environment Variable, and add it to settings.py.
  - In INSTALLED_APPS, add:
    - cloudinary_storage
    
8. Set Up Procfile for Heroku
  - Create a Procfile and add
    - web: gunicorn YOUR_PROJECT_NAME.wsgi
 
9. Enable Automatic Deploys
  - In Heroku, under Automatic Deploys, enable automatic deployment for the main branch.

  
## Forking The Repository
  Forking a repository creates an independent copy of the original project in your own GitHub account. 
  This allows you to explore the code, make changes, and experiment without affecting the original repository.

  Steps to Fork the Repository:
  - Log in to GitHub.
  - Navigate to the repository you want to fork.
  - Click the "Fork" button in the top right corner of the page.
  - GitHub will create a copy of the repository under your own account, allowing you to modify it as needed.

  
## Cloning The Repository

To clone and set up this project locally, follow these steps:

1. Clone the Repository
  - Open the GitHub repository.
  - Click on the "Code" button.
  - Copy the repository URL by clicking the clipboard icon.
  - Open your IDE or terminal and navigate to the directory where you want to clone the project.
  - Run the following command to clone the repository:
    - git clone <repository-url>
    
  - Navigate into the project directory:
    - cd <project-folder>
  
2. Install Dependencies
  - To install the necessary packages and dependencies, run:
    - pip3 install -r requirements.txt

3. Set Up Environment Variables
  - Create a file called env.py in the root directory.
  - Add the necessary environment variables:
    - import os
    - os.environ["DATABASE_URL"] = "your-database-url"
    - os.environ["SECRET_KEY"] = "your-secret-key"
    - os.environ["CLOUDINARY_URL"] = "your-cloudinary-url"
      
  - Add env.py to .gitignore to prevent it from being committed to GitHub.

4. Apply Migrations
  - Before running the project, apply database migrations:
    - python3 manage.py migrate
      
5. Run the Development Server
  - Start the local development server with:
    - python3 manage.py runserver

---
  
## Credits
  
### Content
The Code Institute's Moments Walkthrough project was used as a reference and provided the default profile image.
  
  
  

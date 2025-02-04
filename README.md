# FlavorFrames API

## Code Institute Portfolio Project 5

Welcome to the backend of FlavorFrames, a platform designed for food enthusiasts to share and discover popular eateries and hidden gems. You can find detailed information on the frontend implementation [here](https://github.com/Maximiliane-K/flavorframes).

In an era where food crawls, mukbangs, and street food adventures are widely shared, FlavorFrames makes it easy for users to showcase their favorite finds. Whether it’s a hidden café, a must-visit food stall, or a trending restaurant, the platform helps users connect through their culinary discoveries.

FlavorFrames focuses exclusively on food and drinks, making it easier to find trending spots in your city or while traveling.

The FlavorFrames API powers the platform by providing essential functionalities that allow users to share and engage with food content. 
Users can create, update, and delete posts featuring images, written descriptions, and location tags. They can follow others, interact through likes and comments. 

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
  * [Third Party Technologies](#third-party-technologies)
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

**Bookmarks**

- DUS 22 Bookmark a Post: As a developer or superuser, I can create a bookmark object linked to a specific post so that I can save it for later reference.

- DUS 23 Remove a Bookmark: As a developer or superuser, I can delete a bookmark object that I created so that I can remove the saved post from my bookmarks.

- DUS 24 Restrict Unauthorized Bookmark Deletion: As a developer or superuser, I cannot delete a bookmark object that I did not create so that only the original user can remove 
  their bookmark.

- DUS 25 View All Bookmarks: As a developer or superuser, I can access a list of all bookmark objects so that I can review and manage bookmarked posts in the API.

## Structure Plane

#### **Features**

## Skeleton Plane

#### **Database Shema**

## Technologies

### Languages

### Third Party Technologies


## Testing

## Deployment

### Deploying To Heroku
  
## Forking The Repository
  
## Cloning The Repository
  
## Credits

### Media
  
### Content

  
  
  

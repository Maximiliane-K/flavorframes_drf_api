# flavorframes API 

## Backend Testing

### Table of Contents 
  - [Code Validation](#code-validation)
  - [Automated Testing](#automated-testing)
  - [Manual Testing](#manual-testing)

### Core Validation

#### PEP8

The FlavorFrames API has been developed using the pylint and black GitPod extensions to ensure proper formatting, linting, 
and internal PEP8 validation tests. 
At the end of the project, no critical errors or functional issues were found, 
and the code meets all necessary style and quality standards.

---

### Automated Testing

A total of 16 automated tests have been implemented to validate key user story scenarios within the FlavorFrames API. 
These tests ensure core functionalities across the following app components:
- Posts
- Comments
- Likes
- Bookmarks
- Profiles

![Automated Testing](https://res.cloudinary.com/maxiscloud/image/upload/v1740887570/Screenshot_2025-03-02_at_04.51.05_ltclbi.png)

---

### Manual Testing

**Profiles**

✓ Test that all profiles are returned when making a GET request to the profile list endpoint  
✓ Test that a specific profile can be retrieved by its ID using the GET request to the profile detail endpoint  
✓ Test that the profile’s city, about section, and profile picture can be updated correctly by the owner  
✓ Test that a user cannot update another user’s profile (should return a 403 error)  
✓ Test that a profile can only be deleted by its owner (should return a 403 error for others)  

**Posts**

✓ Test that all posts are returned when making a GET request to the post list endpoint  
✓ Test that posts are ordered by creation date in descending order  
✓ Test that posts can only be created by logged-in users with the correct ownership  
✓ Test that the post details can be retrieved with a valid post ID  
✓ Test that a user can update and delete their own posts (should return a 403 error for others)

**Likes**

✓ Test that all likes can be listed when making a GET request to the like list endpoint  
✓ Test that a like can be created only by authenticated users  
✓ Test that a like can be deleted only by the user who created it (should return a 403 error for others)  
✓ Test that a user cannot delete a like they did not create (should return a 403 error)  

**Comments**

✓ Test that all comments can be listed 
✓ Test that a comment can be created by authenticated users
✓ Test that a comment can be retrieved by its ID
✓ Test that a comment can only be updated by its owner  
✓ Test that a comment can be deleted only by its owner
  
**Events**

✓ Test that all events can be listed when making a GET request to the event list endpoint  
✓ Test that an event can be created by authenticated users when making a POST request  
✓ Test that an event can be retrieved by its ID when making a GET request to the event detail endpoint  
✓ Test that a user can only edit their own event when making a PUT request to the event detail endpoint  
✓ Test that an event can be deleted only by the owner when making a DELETE request to the event detail endpoint  

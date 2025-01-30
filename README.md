# Spittin' Bars
test
## Table of Contents
- [Introduction](#introduction)
- [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
  - [Colour Scheme](#colour-scheme)
  - [Font](#font)
  - [Project Planning](#project-planning)
- [Strategy Plane](#strategy-plane)
  - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
  - [MoSCoW Prioritization](#moscow-prioritization)
  - [Sprints](#sprints)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - User Profile](#epic---user-profile)
    - [Epic - Articles](#epic---articles)
    - [Epic - Booking](#epic---booking)
    - [Epic - Photo Gallery](#epic---photo-gallery)
    - [Epic - Visit Us/Reviews](#epic---visit-usreviews)
- [Scope Plane](#scope-plane)
- [Structural Plane](#structural-plane)
- [Skeleton & Surface Planes](#skeleton--surface-planes)
  - [Wireframes](#wireframes)
- [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
- [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies & Languages Used](#technologies--languages-used)
- [Libraries & Frameworks](#libraries--frameworks)
- [Tools & Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku Deployment](#heroku-deployment)
  - [Clone Project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Additional Reading/Tutorials/Books/Blogs](#additional-readingtutorialsbooksblogs)
- [Acknowledgements](#acknowledgements)

### Introduction

Spittin' Bars is a platform tailored for aspiring rappers, poets, and lyricists. It offers a space to compose and refine lyrics, allowing users to hone their craft and share their work with a community of like-minded individuals.

### UX - User Experience

* Design Inspiration

Branding, which will also be the basis of our colour scheme to maintain conformity.

![Logo](readme_docs/readme_images/logo-600px.jpg)

* Colour Scheme
* Font
* Project Planning


<hr>

### User Stories

* As a user, I want to create and save my own lyrics, so that I can share them with friends and get feedback.

* As a user, I want to read and view my saved lyrics, so that I can review my work anytime.

* As a user, I want to update my lyrics, so that I can make improvements and changes.

* As a user, I want to delete my lyrics, so that I can remove any unwanted content.

* As a user, I want to browse other users' lyrics, so that I can get inspired and learn from others.

* As a user, I want to rate and comment on other users' lyrics, so that I can provide feedback and engage with the community.

* As a user, I want to search for lyrics by genre or theme, so that I can find content that matches my interests.

* As a user, I want to record and playback my lyrics, so that I can hear how they sound and make improvements.

## Admin User Stories

* As an admin, I want to manage user accounts, so that I can create, update, or delete accounts to maintain the integrity of the community.

* As an admin, I want to approve or reject new lyric submissions for public display, so that I can ensure the content meets the community guidelines.

* As an admin, I want to monitor user activity and comments, so that I can manage inappropriate behavior and maintain a positive environment.

* As an admin, I want to generate reports on user engagement and content popularity, so that I can assess the app's performance and make data-driven decisions.

* As an admin, I want to manage site settings and configurations, so that I can update the platform as needed.

## MoSCoW Prioritization

### Must Have: Essential features that the app cannot function without.

* User: Manage an account - register, sign in log out

* User: Creating, reading, updating, and deleting lyrics

* User: Playback backing track (looped beat various styles) functionality to practice to work in my lyrics and practice

* User: Browsing and viewing other users' lyrics

* Admin: Managing user accounts

* Admin: Managing user activity

* Admin: Approving or rejecting new lyrics submissions to public area

### Should Have: Important features that are not critical but highly valuable.

* User: Rating and commenting on lyrics

* User: Searching for lyrics by genre or theme

* Admin: Monitoring user activity and comments

### Could Have: Desirable features that are not necessary but would enhance the user experience.

* User: Searching for lyrics by genre or theme

* User: links to other media

* Admin: Generating reports on user engagement and content popularity

### Won't Have: Features that are not planned for the current version of the app.

* Advanced editing tools (e.g., recording, auto-tune, beat matching)

<hr>

### Wireframes
The wireframes were created using Balsamiq
Homepage (unregistered users):
![alt text](readme_docs/readme_images/Homepage.png)
Homepage Registered Logged In Users:
![alt text](<readme_docs/readme_images/User Homepage.png>)
Community Page:
![alt text](<readme_docs/readme_images/View Other Raps.png>)


### Database Schema - Entity Relationship Diagram

| **Field**    | **Type**                    | **Description**                                    |
|--------------|-----------------------------|----------------------------------------------------|
| `id`         | AutoField (Primary Key)     | Unique identifier for each user.                   |
| `username`   | CharField(max_length=150)   | The username of the user.                          |
| `password`   | CharField(max_length=128)   | The password of the user.                          |

## Lyric Model

 **Field**    | **Type**                    | **Description**                                    |
|--------------|-----------------------------|----------------------------------------------------|
| `id`         | AutoField (Primary Key)     | Unique identifier for each song/lyrics.            |
| `title`      | CharField(max_length=255)   | The title of the song/lyrics.                      |
| `content`    | TextField                   | The lyrics content.                                |
| `author`     | ForeignKey(User)            | The user who created the lyrics.                   |
| `published`  | BooleanField(default=False) | Whether the lyrics are published (True/False).     |
| `updated_at` | DateTimeField(auto_now=True) | Timestamp for when the lyrics were last updated. |


## Explanation:

* User: Represents a user in your system.

* id: Unique identifier for each user.

* username: The username of the user.

* password: The password of the user.

* Lyrics: Represents the lyrics or songs created by users.

* id: Unique identifier for each song/lyrics.

* title: The title of the song/lyrics.

* content: The lyrics content.

* author_id: Foreign key that links to the User table.

* published: Indicates whether the lyrics are published.

* created_at: Timestamp when the lyrics were created.

* updated_at: Timestamp when the lyrics were last updated.


## Entity Realtionship Models
```
+------------+         +------------+
|   User     |         |   Lyrics   |
|------------|         |------------|
| id         |         | id         |
| username   |         | title      |
| password   |---------| content    |
|            |         | author_id  |
|            |         | published  |
|            |         | created_at |
|            |         | updated_at |
+------------+         +------------+
```
Realtionship
One-to-Many: Each user can have multiple lyrics, but each piece of lyrics belongs to one user. This is represented by the foreign key author_id in the Lyrics table.


## Deployment

* Connecting to GitHub

Repository initially created on GitHub, Here's how

1. Sign in to GitHub First, go to GitHub and log in to your account. If you don't have an account, you'll need to sign up.

2. Create a New Repository Once you're logged in, click the + icon in the top-right corner of the page, and select New repository.

You’ll be taken to the Create a new repository page.

3. Set Up the Repository Repository name: Choose a name for your repository.

Description (optional): You can add a brief description of your project.

Public or Private: Select whether you want the repository to be public (visible to everyone) or private (only you and selected collaborators can see it). This project is set to public

Initialize this repository with a README: (2) It's often a good idea to check this box. It will create a README.md file in your repository, which you can edit to describe your project.

Now Create repository (3).


![GitHub Deployment Step 1](readme_docs/readme_images/git-deply1.png)

4. Open the GitHub Repository Navigate to your GitHub repository in your web browser and copy the link for your repository.

![GitHub Deployment Step 4](readme_docs/readme_images/git-deply4.png)

5. Launch Gitpod and select New Workspace

![GitHub Deployment Step 2](readme_docs/readme_images/git-deply2.png)

6. Here you can paste the url to the repositry and select your chosen editor.

![GitHub Deployment Step 3](readme_docs/readme_images/git-deply3.png)

7. Now that the repo is open in our editor any addition to the code are submitted to the repo in the terminal with the commands

git add . git commit -m "Initial commit" (details of commit)

git push

8. Each team member created their own branch to work on, which was later merged with the main branch to avoid conflicts.

### Creating a Branch from Main

To create a new branch from the main branch, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to your project directory.
3. Ensure you are on the main branch by running:
  ```bash
  git checkout main
  ```
4. Create a new branch with a descriptive name:
  ```bash
  git checkout -b new-branch-name
  ```
5. Your new branch is now created, and you can start making changes without affecting the main branch.

* Heroku Deployment

1. Create a New App on Heroku:

* Go to Heroku and log in.
* Click the "New" button in the top right corner and select "Create new app".
* Enter a unique name for your app and choose your region.
* Click "Create app".

![Heroku Deployment Step 1](readme_docs/readme_images/horoku-deply1.png)

2. In settings Connect to GitHub repo, search can be used to ensure your Heroku is connected to GitHub:

![Heroku Deployment Step 2](readme_docs/readme_images/horoku-deply2.png)


3. In settings, set config vars to replicate what is in env.py, secret key and database_url-

![Heroku Deployment Step 3](readme_docs/readme_images/horoku-deply3.png)

4. Manual deploy on heroku - heroku-deploy.png

![Heroku Deployment Step 4](readme_docs/readme_images/horoku-deply4.png)

## Credits

* Code

* Media

* Additional Reading/Tutorials/Books/Blogs

* Acknowledgements

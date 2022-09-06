# media-tracker

## Description
A website to help you keep track of all the video media that you watched, are watching or planing to watch.

## technology used:
- Python
- Flask
- HTML
- SASS
- CSS
- Javascript
- Jinja
- SQL

## Usage and explanation
The first function of the website was the login/ logout ' register system. Users can input a name and password. We store the user's username and a hash of his password in our database due to security concerns. 
You can add a media define name, status, type, and URL for an image of its cover. user's media are viewed as the status attribute. Then I store this media info in the database with the user id and date. 
user can edit any media attribute. and can delete an entire media.

## Features to make:
- [X] register
- [X] login 
- [X] Logout system
- [X] add a media
    - media should have:
        - name
        - type
        - cover img Url
        - status
            - watched
            - watching
            - plan to watch
        - date added
- [X] edit media 
- [X] remove media
- [X] index page show all media
- [X] make a different view for ever status
- [ ] responsive design
- [ ] rating system


## expect to finish in: **4 days**

## TODO:
- [X] project set up
    - [X] python
    - [X] sass
    - [X] server
- [X] make a nav bar
- [X] design the database
- [X] connect data base
- [X] error page
- [X] require login wrapper
- [X] login page
- [X] logout page
- [X] register page design
- [X] add media design
- [X] make a design for edit list page
- [X] make a design for Watching
- [X] make watched, plan to watch pages
- [X] adjust add media so that you can't add Media twice
- [X] make edit list 
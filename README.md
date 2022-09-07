# media-tracker

## Description
A website to help you keep track of all the video media that you watched, are watching or planing to watch.

## technology used:
- Python
- Flask
- HTML
- SASS
- BEM
- CSS
- Javascript
- Jinja
- SQL

## Usage and explanation
The first function of the website was the login/ logout ' register system. Users can input a name and password. We store the user's username and a hash of his password in our database due to security concerns. 

You can add a media define name, status, type, and URL for an image of its cover. user's media are viewed as the status attribute. Then I store this media info in the database with the user id and date.

user can edit any media attribute and delete an entire media.

There is also an apology page that appears whenever the input is not correct or when an internal error occurs.

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

## Project structure and tree Explanation
- app.py
    - the part where main application is written, specifying the routes and handling the database.
- media.db
    - main database having two tables now, one that stores users data and other one to store media data with a user id that correlates both of them.
- schema.sql
    - database schema
- requirements.txt
    - main libs that are required for this project
- remove-media.sql
    - empties media table for dev purposes only
- .gitignore
    - files and directories to not push to git
- templates/
    - stores every page template 
        - main pages
            - index.html
            - register.html
            - login.html
            - planToWatch.html
            - watched.html
            - watching.html
        - helper pages
            - error.html
            - layout.html
            - TODO.html
- static/
    - stores static files like css, js and images
- static/sass
    - chose to use sass to make the development more organized
- static/sass/global
    - global rules, normalize, colors, typography helper classes and more
- static/sass/components
    - styles for each component used in the page
- static/sass/pages
    - to control the flow of components within a certain page
- static/sass/util
    - mixins




## expect to finish in: **4 days**

## TODO:
- [X] project set up
    - [X] python
    - [X] sass
    - [X] server
- [X] make a nav bar
- [X] design the database
- [X] connect database
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

### Notices
-  Cinema Photo by <a href="https://unsplash.com/@felixmooneeram?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Felix Mooneeram</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
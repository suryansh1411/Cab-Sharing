# Project Title

A Web application where students can come together and form groups for the purpose of sharing a ride. It uses Django framework in backend along with SQLite as database. HTML, CSS and Bootstrap is used to render the front-end to the user.

The project aims to provide the students with a much more organised platform to form groups and share cab rides from campus to city.

# Features

## Sign Up Page

If a user is not registered, he can sign-up using his/her iitg email-id and giving necessary information on the sign-up page. If a user with given email already exists, the app shows an error. Otherwise the user is logged in and a toast message is shown.

This information is then stored in the database.

![Demo](images\SignUp.png)



## Login Page


The information entered is validated with data in the database, if it is correct the user is directed to landing page. Otherwise an alert dialogue message is shown.

![Demo](images\Login.png)



## Home Page

This Page shows the groups which will be travelling in future, the informations like destination, members, date and time of the ride are also shown.

There is a filter panel on the left, using which the users can filter the groups according to destination, date, time, and gender preferences as well. 

![Demo](images\Home.png)



## MyBooking Page

This page lists all the future and past travels in which the user has participated. List is ordered from being latest to oldest.

![Demo](images\MyBooking.png)



## New Booking Page


This page contains a form, by giving informations like destination, date, time, maximum number of members and gender preference if any, a user can create a group. 

![Demo](images\NewBooking.png)



## Booking Detail Page

This page contains all the information regarding a travel. It displays the creator name, members' name, destination, date, time, starting position, gender preference of a travel.

![Demo](images\GroupDescription.png) 



## Group Chat Page

This page allows the user to interact with the creator and members of the group. They can enquire, discuss and negotiate about a travel here. 

![Demo](https://github.com/Geek-Wolf/Cab-Sharing/blob/master/images/Chatpage.png)



## Profile Page

This page displays the information about the person and if a user is viewing his own page, then he can update his information and profile picture.

![Demo](images\Profilepage.png)



## FeedBack Page

This page contains a form using which a user can give his/her suggestions, complains to the creator of the website.

![Demo](images\Feedback.png)




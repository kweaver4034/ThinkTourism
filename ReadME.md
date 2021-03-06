# Customized Tourism App
![Clarkson](https://i.imgur.com/dyc6ogY.png)

In the hospitality industry guests are unable to customize certain aspects of their stay. This application combines a simple to use SQL interface with an API for third-parties, in order to provide a foundation from which to ask questions and store responses, related to guest accommodations.

# Python Modules
Please ensure the following Python modules are installed:
- Pymysql
- Flask

# SQL Database
The database contains the following tables:
- Question Groups
    > Question Groups are used to organize questions. The name and date created of each group is stored.
- Questions
    > Contains questions as well as their respective class, type, and group ID.
- Choices
    > Choices are stored as text with an optional image url.  The respective question ID is also stored.
- Users
    > Stores information of users authorized to access the SQL interface.
- Respondents
    > Stores information about users who have responded to questions.
- Responses
    > Each entry tracks the Respondent, QuestionID, and ChoiceID of a given response.


# SQL Interface
This application comes with a lightweight interface for the attached SQL database that allows authorized users to conduct the following activities:
>- Create new question groups
>- Add new questions (with respective choices)
>- Query the database
>- View a sample questionnaire
>- Update their password

# Administrative Features
The application is equipped with the following:
>- Login System
>- Add new authorized users (admin only)
>- Reset user passwords (admin only)
>- Log file that tracks activities performed on SQL database

# Autogenerated Questionnaires
>The application also comes capable of automatically generating questionnaires for a given question group.

# API Functionality
> Additionally the application comes with the ability for third party users to obtain information about questions in JSON format through a 'GET' api. Third party users can then use the 'POST' api in order to submit responses into the Responses table of the SQL database.

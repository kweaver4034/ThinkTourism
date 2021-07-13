# Customized Tourism API
![Clarkson](https://i.imgur.com/dyc6ogY.png)

In the hospitality industry guests are unable to customize certain aspects of their stay. This application combines a simple to use SQL interface with an API for third-parties, in order to provide a foundation from which to ask questions and store responses, related to guest accommodations. For a given **question group** one can obtain the **questions** and their corresponding **choices**.

# API Functions
- GetQuestions
- GetNextQuestion
- SubmitResponse

# Get Questions
The endpoint for this function is /api/getquestions and used the GET method.  This function can be used to retrieve all **questions** from a given **question group** as well as their respective **choices**. The only argument for this GET link is the name of the **question group** that you are attempting to reference. The endpoint will return json in the following format:
Example:```http://127.0.0.1:5000/api/getquestions?QuestionGroup=QuestionnaireTestGroup```
![Screenshot](https://i.gyazo.com/6045eb02d2a8c5732bb57ba1467aefdc.png)

The JSON can be used to generate questionnaires with all **questions** and **choices** on the same page.  

# Get Next Question
The endpoint for this function is /api/getnextquestion and it uses the GET and POST methods.  This function can be used to retrieve the next **question** for a given **question group**.  Again the only GET argument is the name of the **question group** that you are attempting to reference, but this function also requires the previous question number to be submitted through POST.  It should be passed as QuestionNumber. If no QuestionNumber is passed, the endpoint will return the first question in the question group.  The endpoint will return JSON in the following format, similar to GetQuestions, but only one question's information will be returned.
Example:```http://127.0.0.1:5000/api/getnextquestion?QuestionGroup=QuestionnaireTestGroup```
![Screenshot](https://i.gyazo.com/1f04c775d3a23a1dc8620d385109df54.png)

This function can be used to generate questionnaires with each **question** on a different page.

# Submit Response (All)
This endpoint is /api/submitallresponses and it only uses POST. This function can be used to submit all the responses from a questionnaire at once (intended for use with single page questionnaires).  This endpoint requires 3 variables passed as JSON:

- Respondent
- ChoiceID
- QuestionID

**The endpoint accepts only JSON in the form of a list of dictionaries as shown here:**

```[ {"Respondent":"User123", "QuestionID":1, "ChoiceID":2 }, {"Respondent":"User123", "QuestionID":2, "ChoiceID":5 } ]```

**Please note that while respondent is not a required field it must be in the dictionary, if the questionnaire is answered anonymously simply put "Respondent":""**

# Submit Response (One)
This endpoint is /api/submitresponse and it also uses only POST.  This function can be used to submit user responses from a given questionnaire.  The endpoint requires 3 variables passed through POST: 

- Respondent
- ChoiceID
- QuestionID

# Explanation of Terms
>Respondent is the label for the user completing the questionnaire.  This could be a username or generated ID that is assigned by you.  The endpoint accepts Respondents of up to 50 characters in length. Respondent is not a required field.

>ChoiceID is the label for choices given through the GET API, which differentiates the choices for each question. ChoiceID is a required field.

>QuestionID is the label for the questions given through the GET API. QuestionID is a required field.

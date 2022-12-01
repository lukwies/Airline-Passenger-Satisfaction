<img width="500" src="https://cdn.cnn.com/cnnnext/dam/assets/210810173434-4-pan-am-707-economy-meals-credit-anne-sweeney-full-169.jpg">

# Project on flight ratings
An airline company is interested in how passengers rate their flight and aviation service.
Therefore they envolved a survey to figure out the satisfaction level of their customers.
Now that airline hired us for analysing the data to get better insights of the survey results.
For a detailed description of the dataset, [click here](#Dataset-Description).


## Business Questions
- What is the customer profile?
- What is the airline rating in general?
- Which services are rated best and which one worst?
- Is there a difference in the rating between males and females?
- What impact does the flightclass have on the rating?
- Is the rating worse for long distance flights?
- Do passengers rate better on private than on business flights?
- Does the age of a customer effect the rating?


## Dataset Description
The flight rating dataset has 24 columns and round about 120000 rows.<br>
Source: https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction

<pre>
Id                                : 1-129880
Gender                            : Male|Female
Customer Type                     : Loyal|Disloyal
Age                               : 7-85
Type of Travel                    : Private|Business
Class                             : Economic|Ecomomic plus|Business
Flight Distance                   : 31-4983 km
Inflight wifi service             : 0-5
Departure/Arrival time convenient : 0-5
Ease of Online booking            : 0-5
Gate location                     : 0-5
Food and drink                    : 0-5
Online boarding                   : 0-5
Seat comfort                      : 0-5
Inflight entertainment            : 0-5
On-board service                  : 0-5
Leg room service                  : 0-5
Baggage handling                  : 0-5
Checkin service                   : 0-5
Inflight service                  : 0-5
Cleanliness                       : 0-5
Departure Delay in Minutes        : 0-1592 min
Arrival Delay in Minutes          : 0-1584 min
satisfaction                      : neutral or dissatisfied|satisfied
</pre>


## Prediction
I wondered if it's possible to predict if a customer is satisfied with the airline services or not. Therefore I trained several models and was able to end up with an acceptable result. The implementation of these predictions
can be found
<a href='https://github.com/lukwies/final-bootcamp-project/blob/main/notebooks/predict_satisfaction.ipynb'>here</a>.
<br>
I also think it would be interesting for an airline to predict the customer type (Loyal/Disloyal).
An approach for that prediction can be found
<a href='https://github.com/lukwies/final-bootcamp-project/blob/main/notebooks/predict_customer_type.ipynb'>here</a>.


## Presentation
The presentation is done with tableau and can be found
<a href='https://public.tableau.com/app/profile/lara.falkensteiner/viz/FlightRatings/FlightRatings'>here</a>.


## Application
I also created an application using streamlit and plotly which can be found
<a hred='https://github.com/lukwies/final-bootcamp-project/tree/main/app'>here</a>.

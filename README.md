# tasnix
tasnix flask app

## API:

1) Clone the repository https://github.com/basaks/eb_flask_app

2) Add an API (task3) to return a list of people who reside in a state using the following dictionary.
people_state = {'act': 'allen',
                'nsw': 'sudipta, nikhil',
                'qld': 'brett'}
Your query should accept state as the parameter. 
4) What would be the corresponding CURL request for the above? – CURL http://127.0.0.1:5000/getName/<state>
5) Write a second API endpoint that will find the state of an individual from the dict above.  CURL http://127.0.0.1:5000/getState/<name>

6) A Pull Request will show us what you have done.


Notes:

## Packages to be installed:
1. Flask

## Run application

    python app.py
    
This message should appear:

     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

There are two endpoints exposed for the application.

#### @app.route('/getName/<State>')
This endpoint checks for the server status and version string.
On your browser go to http://127.0.0.1:5000/getName/nsw

You should get the following on your browser with the current timestamp:
    
sudipta, nikhil

Or one could use
    
    curl http://127.0.0.1:5000//getName/nsw

If state not present in the dictionary, “State not Found” will be returned.

#### @app.route('/getState/<name>')
This endpoint checks for the server status and version string.
On your browser go to http://127.0.0.1:5000/getState/sudipta

You should get the following on your browser with the current timestamp:
    
nsw

Or one could use
    
    curl http://127.0.0.1:5000//getState/sudipta

If name not present in the dictionary, “Name not Found” will be returned.



## SQL:
Please write a select statement to join these tables and show all runners with their winning events, if they have them. Order the list by the runner name.

sql> SELECT * FROM runners;
+----+--------------+
| id | name         |
+----+--------------+
|  1 | John Doe     |
|  2 | Jane Doe     |
|  3 | Alice Jones  |
|  4 | Bobby Louis  |
|  5 | Lisa Romero  |
+----+--------------+

sql> SELECT * FROM races;
+----+----------------+-----------+
| id | event          | winner_id |
+----+----------------+-----------+
|  1 | 100 meter dash |  2        |
|  2 | 500 meter dash |  3        |
|  3 | cross-country  |  2        |
|  4 | triathalon     |  NULL     |
+----+----------------+-----------+
 
 
### Below query will list all the runners (in sorted order) along with their winning races (if any)
SELECT NAME, EVENT FROM RUNNERS 
--LEFT JOIN RACES
ON RUNNERS.ID = WINNER_ID
ORDER BY NAME;
#### Result

Alice Jones|500 meter dash
Bobby Louis|
Jane Doe|100 meter dash
Jane Doe|cross-country
John Doe|
Lisa Romero|

### Below query will list only the runners (in sorted order) who have won any race along with their winning races
SELECT NAME, EVENT FROM RUNNERS 
JOIN RACES
ON RUNNERS.ID = WINNER_ID
ORDER BY NAME;

#### Result

Alice Jones|500 meter dash
Jane Doe|100 meter dash
Jane Doe|cross-country

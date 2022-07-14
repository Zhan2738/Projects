# MerckNLP2021-22
1. To run it on local machine:

Step1: Download 4 files are enough: app.py, rds_db.py, and two htmls (detail.html and index.html) under the folder templates. 

        app.py is the main file to go throught different routes. 
        rds_db.py is the file to connect with AWS RDS and make queries. 
        index.html is the homepage.
        detail.html is the page presenting different experimentail conditons.
      
Step2: Install Python 3 and Flask, and then run 'flask run' in the terminal directly. Then you can see the result in local machine: http://127.0.0.1:5000

2. To host it on heroku
   
   I followed this post: https://www.jcchouinard.com/deploy-a-flask-app-on-heroku/
   And other files (except 4 mentioned above) are used to set up an virtual environment and run lively in heroku or google app engine.
   The final result is here: https://merckproject.herokuapp.com/

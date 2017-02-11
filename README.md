# Movie-Matchmaker
Tartanhacks 2017 Project

Commands to Run Before Using:
---------
-$ pip install --upgrade watson-developer-cloud
or
-$ easy_install --upgrade watson-developer-cloud

Required Files:
------
- Main.py - main function that returns the top five relevant movies
  - change movie_limit to alter number of api calls and movie bank
- results.py - function using cgi to connect python backend and html frontend
- description_parser.py - python file that shows how to use Alchemy Language API
- Text2Emotion.py - class that can be imported, create an instance to translate text to emotion
- soup.py - contains parse function that separates movie titles from imdb top movies html file
- AlgoMachine.py - class that can imported, create an instance to get 5 relevant movies when given movie list and user input from quiz
- recommendations.html - html for recommendations page
- input.html - quiz form html

Other Files:
------------
- description_parser.py - API tester
- soup.html - html from imdb top movies page
- WebScraper.py - python file to get html in soup.html
 
How to Run:
-----------
- cd to cgi-bin, then "chmod +x results.py" command
- start server in terminal with "python3 -m http.server --bind localhost --cgi 8000"
- open input.html in brower
- fill out form and submit
- might have to use "cf.exe auth" to sign into bluemix
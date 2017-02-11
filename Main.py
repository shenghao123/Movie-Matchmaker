import Text2Emotion
import WebScraper
import MovieParser
import AlgoMachine

def main(user_input):
    web_scraper = WebScraper.WebScraper()
    movie_parser = MovieParser.MovieParser()
    text2emotion = Text2Emotion.Text2Emotion()
    algorithm_machine = AlgoMachine.AlgoMachine()

    url = ""

    scraped_data = web_scraper.scrape(url)
    movie_list = movie_parser.parse(scraped_data)
    for movie in movie_list:
        movie.emotion_dict = text2emotion.generate(movie.description)

    top_five = algorithm_machine.calculate(movie_list, user_input)
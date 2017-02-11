import Text2Emotion
import WebScraper # not done
import MovieParser # not done
import AlgoMachine

def main(user_emotions):
    web_scraper = WebScraper.WebScraper() # not done
    movie_parser = MovieParser.MovieParser() # not done
    text2emotion = Text2Emotion.Text2Emotion()
    algorithm_machine = AlgoMachine.AlgoMachine()

    url = ""

    scraped_data = web_scraper.scrape(url)
    movie_list = movie_parser.parse(scraped_data)
    for movie in movie_list:
        movie.emotion_dict = text2emotion.generate(movie.description)

    top_five = algorithm_machine.calculate(movie_list, user_emotions)

    return top_five
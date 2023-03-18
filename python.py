import requests

def get_weather(city):
    # Replace YOUR_API_KEY with your actual API key
    api_key = "41b57e87d8f501e3ff7964ec4c7a4466"
    # Set the API endpoint URL
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    # Set the API parameters
    api_params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    # Make the API request
    response = requests.get(api_url, params=api_params)
    # If the request was successful, return the weather data
    if response.status_code == 200:
        return response.json()
    # If the request failed, return an error message
    else:
        return "Error: Could not retrieve weather data"

# Test the function with a few different cities
print(get_weather("London"))
print(get_weather("Paris"))
print(get_weather("New York"))




# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# # Create a new chatbot
# chatbot = ChatBot("My Chatbot")

# # Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)

# # Train the chatbot on a selection of language resources
# trainer.train("chatterbot.corpus.english.greetings",
#               "chatterbot.corpus.english.conversations")

# # Start a conversation with the chatbot
# while True:
#     user_input = input("User: ")
#     response = chatbot.get_response(user_input)
#     print("Chatbot: ", response)


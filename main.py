import urllib.request
import json
from bs4 import BeautifulSoup

print("Make sure you have the AnkiConnect addon installed and anki is open!")
# url = "https://www.brainscape.com/flashcards/topic-8-particle-nuclear-7466676/packs/9913339" <-- example url
url = input("Please input your url to brainscape flashcards: ")

# making GET req
resp = urllib.request.urlopen(url)

# parsing it
soup = BeautifulSoup(resp, 'html.parser')

# searing for all h2's with class
flashcard_text_soup = soup.find_all('h2', {'class': 'card-question-text'})

# searing for all h3's with class
flashcard_answer_soup = soup.find_all('h3', {'class', 'card-answer-text'})


card_text = []
card_answer = []
# getting all the questions text
for item in flashcard_text_soup:
    card_text.append(item)


# gettings all the answer text
for item in flashcard_answer_soup:
    card_answer.append(item)


def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

# calling ankiConnect, must have anki open


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(
        urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


# create a new deck
new_deck = input("What would you like to call this new deck? :")
invoke('createDeck', deck=new_deck)
print(f"Created {new_deck}")

# create a new card using card_text and card_answer
for i in range(len(card_text)):
    invoke('addNote', note={'deckName': new_deck, 'modelName': 'Basic', 'fields': {
           'Front': str(card_text[i]), 'Back': str(card_answer[i])}})
    print(
        f"Added card number-{i+1} \n Front: {card_text[i].text} \n Back: {card_answer[i].text} ")
    print("-----------------------------------------------")

print(f"The end, check your anki now for the deck called {new_deck}")

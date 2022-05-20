
# Brainscape flashcards to Anki notes
## Setup
First run this line in the console or your own env to download necessary libraries.
```
pip install pip install beautifulsoup4 urllib3
```
<hr/>
After this you need to download AnkiConnect which is an Anki add-on that allows the script to add new decks/notes. This is done by going to <b>Anki -> tools -> Addons -> Get add-ons</b> and adding the following code to the input box.

```
2055492159
```
Note: You need to restart Anki for the add-on to work
<br/>
Now open Anki and keep it open as you need to keep it open for the script to work. Finally run the script and you should be good to go.
For the URL that you are rendering make sure it looks exactly like this: https://www.brainscape.com/flashcards/data-types-10411173/packs/18649624 
<hr />
Currently the script only does one topic at a time, in the future I'll implement it so that it can do the whole thing at one time.
<hr />
<h2>Error list</h2>
-If there are duplicates in the brainscape deck the script will stop <br/>
- If you put in the wrong url it won't work <br/>
- If you create an Anki deck that already exists

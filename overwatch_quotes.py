import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('overwatch')

# Reads Top 5 stories in 'Hot' category of /r/Overwatch
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to =[]
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

DOOMFIST_QUOTES = (
    'Rising above all!',
    'Rising Uppercut!',
    'Incoming!',
    "Only through conflict do we evolve.",
    "Doomfist here.",
    "My work is not done.",
    "Lose the battle, win the war.",
    "I'm not even close to done!",
    "I've been knocked down before.",
    "I'm not finished.",
    "The battle goes on.",
    "Defeat makes me stronger.",
    "I take it on the chin.",
    "Once the mission starts, no more messing around.",
    "The world changed after the crisis. It is overdue for a new test.",
    "It's not much.. and yet, so much blood has been spilled over it.",
    "This city is a powder keg that could ignite the world.. and Talon is the flame.",
    "Omnics will not be kept down forever. The ashes of the crisis still smolder..",
    "Now where's my hero's welcome?",
    "I think your flight may have been delayed.",
    "This time, I will make sure we do not fail.",
    "The world decided it didn't need Overwatch."
)

GENJI_QUOTES = (
    "Come on.",
    "I am ready.",
    "Ryūjin no ken wo kurae!",
    "The dragon becomes me!",
    "Mizu no yō ni nagare.",
    "Flow like water.",
    "Mi o sutete mo, myōri wa sutezu.",
    "Let us hope for a different outcome.",
    "I need healing.",
    "Senri no michi mo, hito ashi zutsu hakobunari.",
    "Yo.",
    "Measure twice, cut once.",
    "A steady blade balances the soul.",
    "You are only human.",
    "My Halloween costume? Cyborg ninja.",
    "Life and death balance on the edge of my blade.",
    "You seem nice. I hate to kill you.",
    "Waga tamashī wa kinkō o motomeru.",
    "Mada mada",
    "Hah! Simple.",
    "Yoshi!"
)

MCCREE_QUOTES = (
    "Justice ain't gonna dispense itself.",
    "The name's McCree.",
    "Back in the saddle again.",
    "This life's never uneventful.",
    "Let's start over at the beginning.",
    "Whoa there!",
    "Easy.",
    "Huh-ho, excuse me.",
    "It's high noon.",
    "Step right up.",
    "I feel like a man possessed!",
    "Much obliged.",
    "Watch and learn.",
    "You seem familiar. Ain't I killed you before?",
    "I'm your huckleberry",
    "I'm not good, not bad, but I sure as hell ain't ugly.",
    "Reach for the sky.",
    "Well, it's high noon somewhere in the world.",
    "I'm not much for standin' around.",
    "The hunt begins."
)

PHARAH_QUOTES = (
    "I will protect the innocent!",
    "Pharah reporting.",
    "Raptora systems online.",
    "Thunderbird online.",
    "Thunderbird systems online.",
    "Back into the fray.",
    "Clearing the area.",
    "Justice rains from above!",
    "Rocket barrage incoming!",
    "Put your security in my hands.",
    "Aerial superiority achieved.",
    "Rocket jump? That sounds dangerous.",
    "Play nice, play Pharah.",
    "Leave this to a professional.",
    "I've got you on my radar.",
    "I am the rocket queen.",
    "You have my thanks.",
    "I always get my prey.",
    "Death from above.",
    "Clearing the board.",
    "System check initiated. Green across the board, I'm ready for action.",
    "Remember your training, and we'll get through this just fine.",
    "All systems checked out, ready for combat maneuvers."
)

REAPER_QUOTES = (
    "Death walks among you.",
    "This… is my curse.",
    "That which doesn't kill you... makes you stronger.",
    "The grave cannot hold me.",
    "I will feast on their souls.",
    "Death comes.",
    "From the shadows.",
    "Repositioning.",
    "Die, die, die!",
    "Clearing the area.",
    "The darkness consumes.",
    "*Evil laughter*",
    "Nothing can stop death.",
    "Another one off the list.",
    "What are you looking at?",
    "Dead man walking.",
    "I'm not a psychopath. I'm a high-functioning psychopath.",
    "You look like you've seen a ghost.",
    "I work the graveyard shift.",
    "Just stay out of my way.",
    "Ready for combat operations.",
    "Death comes for all."
)

SOLDIER76_QUOTES = (
    "We're all soldiers now.",
    "Soldier: 76 reporting for duty.",
    "I'm not a young man anymore.",
    "Knock me down, and I'll keep getting back up.",
    "This old dog's learned a few tricks.",
    "Get over here and heal up!",
    "Come here and get stabilized.",
    "Anyone need some healing?",
    "I've got you in my sights!",
    "Tactical Visor activated!",
    "Young punks... Get off my lawn!",
    "I'm an army of one.",
    "I didn't start this war, but I'm damn well gonna finish it.",
    "Old soldiers never die, and they don't fade away.",
    "I'm the one who does his job. I'm thinkin'... You're the other one.",
    "Not on my watch.",
    "Are you trying to impress me?",
    "Back in my day, we’d have this payload delivered already!",
    "Age before beauty. I guess you're coming in third.",
    "Quit screwing around and get ready to move!",
    "Try not to get yourselves killed out there.",
    "Los Muertos is a cancer on this city.",
    "Lot of memories of this place. They weren't all bad."
)

SOMBRA_QUOTES = (
    "Everything can be hacked, and everyone.",
    "Sombra online.",
    "Ya estoy lista para ese trago.",
    "Podría haber salido mejor.",
    "Iniciando el hackeo.",
    "Initiating the hack.",
    "Here I am.",
    "¿Qué onda?",
    "¿Me extrañaste?",
    "Missed me?",
    "Always leave yourself a back door.",
    "See you later!",
    "¡Apagando las luces!",
    "EMP activated!",
    "So many targets, so little time.",
    "Hmm.. looks like I have time to do some research.",
    "I'm guessing there's no chance we can take care of this quietly, is there?",
    "Boop!",
    "I knew you were good for something.",
    "I know kung fu."
)

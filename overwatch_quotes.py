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

TRACER_QUOTES = (
    "Cheers, love! The cavalry’s here!",
    "Well, that just happened.",
    "And she's back in the game!",
    "Whee!",
    "Wicked!",
    "Ever get that feeling of déjà vu?",
    "Now, where were we?",
    "Here you go!",
    "Right on target!",
    "You got what's coming to ya!",
    "This time, stay down.",
    "The world could always use more heroes.",
    "Looks like you need a time out.",
    "I have this under control.",
    "Oi! This is no time for standin' around.",
    "Look out world! Tracer's here.",
    "Should we nip to the pub?",
    "Pub, anyone?",
    "I could murder a chip sarnie."
)

BASTION_QUOTES = (
    "Bwee, hoo hoo, bwoo.",
    "Woo, boo doo boo doo doo doo doo!",
    "Boo doo boo doo!",
    "Woo, wow!",
    "Beepleleleh.",
    "Bweeeeeeeeeeeoh.",
    "Bwoo chirr chirr chirr chirr chirr chirr chirr",
    "Zwee?"
    "Woop doo woo dun woop dun doo.",
    "Doo dun dun woo, doo dun wooo"
)

HANZO_QUOTES = (
    "With every death, comes honor. With honor, redemption.",
    "Hanzo at your service.",
    "I will not be defeated so easily.",
    "Start over at the beginning.",
    "A minor setback.",
    "I am not deterred!",
    "My arrow finds its mark.",
    "Strike at the heart!",
    "See through the dragon's eyes.",
    "Marked!",
    "Ryū Ga Waga Teki O Kurau!",
    "Let the dragon consume you!",
    "The dragon consumes.",
    "The dragon is sated.",
    "My aim is true.",
    "They fall before me, one after another.",
    "Flow like water.",
    "From one thing, know ten thousand things.",
    "The outcome was never in doubt.",
    "When the moon is full, it begins to wane.",
    "There is beauty in simplicity.",
    "Unacceptable!"
)

JUNKRAT_QUOTES = (
    "It's a perfect day for some mayhem.",
    "Junkrat, primed and ready!",
    "Well that's a fine how-do-you-do!",
    "You won't get rid of me that easily.",
    "Takes a lickin', keeps on tickin'!,
    "If at first you don’t succeed, blow it up again!",
    "This bomb's for you!",
    "Stop me if you’ve heard this one before.",
    "The hunter lays a trap for his prey.",
    "Hohoho....this'll be good.....",
    "You really stepped in it, mate!",
    "Fire in the hole!",
    "Ladies and gentlemen....start your engines!",
    "Everything's coming up.....EXPLODEY!",
    "And they said I'd never amount to anything!",
    "If it can’t handle the heat, stay out of my face!",
    "Brings a tear to me eyes.",
    "Someone better get a firey, because I'm on a roll!",
    "Come on, come on, come on! I hate waiting!",
    "It’s hard to just sit around knowing there’s someone out there that needs to be blown up!",
    "What a bunch of misfits and freaks we got here. I love it!",
    "I'm on fire! Usually that would not be a good thing."
)

MEI_QUOTES = (
    "Our world is worth fighting for.",
    "I have to get back in the fight.",
    "Everyone is counting on me!",
    "Let's see you get past this!",
    "Ice wall, coming up.",
    "Blocking them off",
    "Freeze! Don't move!",
    "I hope you learned your lesson.",
    "Sorry! Sorry, I'm sorry. Sorry.",
    "A-Mei-zing!",
    "You have to let it go.",
    "I love it here in the mountains! I wish I could go climbing",
    "I’m ready to start a blizzard.",
    "Anyone want a popsicle?",
    "I'm on fire! Well, you know what I mean."
    "Ooh, sorry about that.",
    "Oops, sorry!",
    "Mei checking in!"
)

TORBJORN_QUOTES = (
    "Build em up, break em down.",
    "Torbjörn ready to work!",
    "Back to the drawing board.",
    "Heh, time to roll up my sleeves.",
    "Heh heh, I have big plans for you!",
    "Oh, such potential!",
    "I foresee great things for you!",
    "Ha ha ha. Just wait and see what I have in mind!",
    "My masterpiece!",
    "Alright. Now do what you were built to do!",
    "My turret!",
    "Armor, come get it!",
    "Come get your armor.",
    "Molten Core!",
    "It's always better to be the hammer than the nail.",
    "If you want something done right, you gotta do it yourself.",
    "Don't get caught with your beard in the letter box.",
    "Hard work pays off!",
    "People always underestimate the engineers.",
    "Some assembly required."
)

WIDOWMAKER_QUOTES = (
    "One shot, one kill.",
    "Widowmaker here.",
    "C'est la vie.",
    "Rendez-vous avec la mort.",
    "I see you, do you see me?",
    "There you are.",
    "Ça pique, n'est ce pas?",
    "A single death can change everything.",
    "Cherchez la femme.",
    "Step into my parlor,' said the spider to the fly.",
    "What's an aimbot?",
    "You have my attention.",
    "Bonjour.",
    "A beautiful death.",
    "The enemies of Talon shall be eliminated.",
    "*chuckles* I think it's time for us to see other people.",
    "I am ready to kill.",
    "Enough waiting around."
)

DVA_QUOTES = (
    "I play to win!",
    "I'm too young to die!",
    "Ha! Jah Jin Nah!",
    "I'm not a good loser.",
    "Defense Matrix activated.",
    "I'm gonna have to shoot you down!",
    "Time to raise my APM!",
    "Bunny hop!",
    "MEKA activated!",
    "All systems checked out.",
    "Bailing out.",
    "Brb.",
    "Nerf this!",
    "Activating self-destruct sequence!",
    "MVP: D.Va!",
    "Here comes a new challenger!",
    "D.Va: 1, Bad Guys: 0",
    "Is this easy mode?",
    "Aw, yeah!",
    "GG!",
    "Annyeong!",
    "I'm ready to initiate self-destruct sequence!"
)

ORISA_QUOTES = (
    "Your safety is my primary concern.",
    "I am not ready to be deactivated.",
    "System restart initialized.",
    "Stop right there.",
    "You're not getting away.",
    "Defense mode activated.",
    "Fortifying defenses.",
    "Routing application systems to defense.",
    "For your own safety, get behind the barrier.",
    "You are advised to move behind my barrier.",
    "Cease your resistance!",
    "Team up for special attack!",
    "You are advised to cease your resistance.",
    "Fist bump!",
    "Archiving combat data.",
    "Was that the Iris?",
    "I still have a job to do.",
    "Not budging."
)

REINHARDT_QUOTES = (
    "Justice will be done.",
    "Reinhardt at your service.",
    "Back, and ready for more!",
    "Back into the fray!",
    "There is still more to my tale!",
    "Don't worry, my friends! I am your shield!",
    "Ah, get behind me!",
    "I will hold the line!",
    "Barrier won't hold forever!",
    "Hammer down!",
    "Ahh, I'm not as young as I used to be...",
    "Precision German engineering!",
    "I'm just getting started!",
    "When all you have is a hammer, everyone else is a nail.",
    "Do I have your attention yet?",
    "100% German power!",
    "What a performance!",
    "Bring me another!",
    "I'm the ultimate crushing machine.",
    "We shall prove ourselves in glorious combat!",
    "We fought a terrible battle here. Many Crusaders lost their lives.",
    "Aha! I live for a good fight!"
)

ROADHOG_QUOTES = (
    "I’m a one man apocalypse.",
    "Roadhog time.",
    "Roadhog rides again.",
    "Come here!",
    "Here, little piggy.",
    "I'm gonna make you squeal.",
    "Get down",
    "Eat! This!",
    "Bury them deep.",
    "No pain, no gain.",
    "Welcome to the apocalypse.",
    "Like taking candy from a baby.",
    "Bleeding like a stuck pig!",
    "Violence is usually the answer.",
    "Life is pain, so is death.",
    "What are you lookin at?",
    "We're all animals.",
    "Say 'bacon' one more time..."
)

WINSTON_QUOTES = (
    "Imagination is the essence of discovery.",
    "Once more unto the breach.",
    "Through the miracle of science!",
    "Onward and upward!",
    "Excuse me for.. dropping in.",
    "Coming through.",
    "This will protect us.",
    "I've seem to have lost my temper.",
    "How embarrassing",
    "Now you are the endangered species.",
    "Would you like to donate your body to science?",
    "Survival of the fittest.",
    "Buh-ahahahahaa... uh... excuse me.",
    "No, I do not want a banana.",
    "Did... someone say peanut butter?",
    "The power of science!",
    "Houston, uh... we have a problem.",
    "I'm looking forward to working with you all.",
    "Together, we can solve any problem.",
    "I can’t wait to see you all in action."
)

ZARYA_QUOTES = (
    "Together, we are strong.",
    "Zarya, ready for duty.",
    "Haha! Practice makes perfect.",
    "Nuh uh; I am not a good loser.",
    "Don’t be shy; hit me!",
    "Give me your best shot.",
    "Barrier's on you; go!",
    "Get in there.",
    "Is that all you've got?",
    "Just a scratch.",
    "Maximum charge!",
    "Fire at will!",
    "Ogon po gotovnosti!",
    "Do you even lift?",
    "From Russia, with love.",
    "Your team was depending on you.",
    "Strong as the mountain.",
    "In Russia, game plays you."
    "I want to hug you like big, fuzzy, Siberian bear.",
    "Welcome to the gun show!",
    "I can bench more than you."
)

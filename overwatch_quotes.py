import praw
import random
import pdb
import re
import os
import string

def authenticate():
    print('Logging in...\n')
    reddit = praw.Reddit('bot1', user_agent='Overbot 0.1')
    print('Logged in as {}\n'.format(reddit.user.me()))
    return reddit

def overwatch_quotes():
    reddit = authenticate()
    all_comments = reddit.subreddit('test').comments(limit=100)
    print("Checking each comment for")
    for comment in all_comments:
        check_comment_for_hero(comment, reddit)

def reply(hero, regex, reddit, facts, comment):
    text = ' '.join(word.strip(string.punctuation)
                    for word in comment.body.lower().split())
    text = ' ' + text + ' '
    match = re.findall(regex, text)
    if match:
        print(
            hero.upper() +
            " found in comment with ID: " +
            comment.id
            )
        try:
            message = random.choice(facts)
            message = "\"" + message + "\"" + " - " + hero.capitalize()
            comment.reply(message)
        except:
            print('Failed to comment - either timed out or deleted/locked comment')


def check_comment_for_hero(comment, reddit):
    reply('doomfist', '\sdoomfist?\s', reddit, DOOMFIST_QUOTES, comment)
    reply('genji', '\sgenji?\s', reddit, GENJI_QUOTES, comment)
    reply('hanzo', '\shanzo?\s', reddit, HANZO_QUOTES, comment)
    reply('reinhardt', '\sreinhardt?\s', reddit, REINHARDT_QUOTES, comment)
    reply('mercy', '\smercy?\s', reddit, MERCY_QUOTES, comment)
    reply('soldier 76', '\ssoldier 76?\s', reddit, SOLDIER76_QUOTES, comment)
    reply('dva', '\sdva?\s', reddit, DVA_QUOTES, comment)

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
    "Takes a lickin', keeps on tickin'!",
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

ANA_QUOTES = (
    "Never stop fighting for what you believe in.",
    "Captain Amari, reporting for duty.",
    "Heh, I've come back from worse.",
    "I wasn't cut out for retirement anyways.",
    "Old soldiers are hard to kill.",
    "Take your medicine.",
    "Get in there. I'll keep you patched up.",
    "I've seen worse. You're going to live.",
    "Walk it off.",
    "Healing enhanced.",
    "This will only hurt for a minute.",
    "This is going to hurt.",
    "Go to sleep.",
    "Aww, you look tired.",
    "It's quiet time.",
    "Nap time.",
    "Warīhum quwitik!",
    "You're powered up, get in there!",
    "I have empowered you, attack!",
    "Nano Boost administered.",
    "It takes a woman to know it.",
    "Children, behave.",
    "What are you thinking?"
)

LUCIO_QUOTES = (
    "Come on. Let’s bring it together!",
    "Lúcio coming at you!",
    "Back in the mix.",
    "Woo, time to change it up!",
    "I'm too young to die.",
    "This is gonna make you feel better.",
    "Feel the healing beat!",
    "Audio medic!",
    "Oh, oh, oh, time to accelerate!",
    "Time to accelerate!",
    "Speed boost!",
    "Amp it up!",
    "Oh, this is my jam!",
    "Wooh! You hear that?",
    "Let's up the tempo.",
    "Push off.",
    "Nothing’s gonna stop me!",
    "Let’s drop the beat!",
    "Oh, let’s break it down!",
    "Give yourself to the rhythm.",
    "Can’t stop, won’t stop.",
    "That’s how you get tinnitus.",
    "My ratings? 99 Patience, 99 dribbling, 99 making this look good.",
    "Ah, I’m in the groove!"
)

MERCY_QUOTES = (
    "I'll be watching over you.",
    "Mercy on call.",
    "The wonders of modern medicine.",
    "Die Wunder der modernen Medizin.",
    "Did someone call a doctor?",
    "Healing stream engaged.",
    "You’re fully healed, now get out there.",
    "Ich kümmere mich um dich.",
    "Damage boost engaged.",
    "You are ready to do some damage.",
    "Schaden verstärkt.",
    "You should be at peak performance levels.",
    "Right beside you.",
    "Mercy im Bereitschaftsdienst.",
    "Heroes never die!",
    "Helden sterben nicht!",
    "I will watch over you!",
    "Gemeinsam kämpfen wir!",
    "Get them off me!",
    "I could use some assistance!",
    "I have my eye on you.",
    "I'll send you my consultation fee.",
    "On a scale from 1 to 10, how is your pain?",
    "Take two and call me in the morning.",
    "Sprechstunde bei der Frau Doktor.",
    "How barbaric.",
    "A moment to enjoy some peace and quiet, probably just a moment though.",
    "Take a deep breath. Now, let's complete our objectives."
)

MOIRA_QUOTES = (
    "I will find the answers.",
    "Science will reveal the truth.",
    "The truth will be revealed.",
    "There was a flaw in my approach.",
    "When faced with a setback, we must challenge our assumptions.",
    "We must all make sacrifices in the name of science.",
    "Perhaps a new methodology is required.",
    "Regenerating your cellular structure.",
    "Táim i do leighis.",
    "This will improve your condition.",
    "I draw power from you.",
    "Power of destruction",
    "Your power is mine.",
    "Your strength ebbs.",
    "Allow me to repair the damage.",
    "Surrender to my will!",
    "Géill do mo thoil!",
    "What an interesting hypothesis.",
    "Idle hands are the devil's workshop.",
    "One hand gives, the other takes away.",
    "You're a chancer."
)

SYMMETRA_QUOTES = (
    "The true enemy of humanity is disorder.",
    "Symmetra reporting.",
    "Death is an illusion.",
    "I will correct my mistakes",
    "There is still much to be done.",
    "Turret deployed.",
    "From light into being.",
    "Aligning defense system.",
    "Intruder detected.",
    "You are shielded.",
    "Everyone is protected",
    "Photon Barrier deployed.",
    "Teleporter online. I have opened the path.",
    "Teleporter online. We move swiftly.",
    "Order will be restored.",
    "I will shape order from chaos.",
    "If everyone performs their function, victory is assured.",
    "Do not deviate from the plan and victory will soon be ours.",
    "Such a lack of imagination.",
    "Everything by design.",
    "Perfect harmony.",
    "Hard work and dedication pays off."
)

ZENYATTA_QUOTES = (
    "True self is without form.",
    "Zenyatta is everywhere.",
    "Adversity is an opportunity for change.",
    "Repetition is the path to mastery.",
    "Overconfidence is a flimsy shield.",
    "The outcome is not preordained.",
    "Pain is an excellent teacher.",
    "Gaze into the Iris.",
    "Embrace tranquility.",
    "Free your mind.",
    "There is disquiet in your soul.",
    "Bask in the shadow of doubt.",
    "You are your own worst enemy.",
    "Pass into the Iris.",
    "Experience tranquility.",
    "We are in harmony.",
    "I think, therefore I am.",
    "Do I think? Does a submarine swim?",
    "Peace and blessings be upon you all.",
    "I will not juggle.",
    "Life is more than a series of ones and zeroes."
)

overwatch_quotes()

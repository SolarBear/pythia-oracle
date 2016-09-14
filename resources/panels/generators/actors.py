# -*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
# Actor Generator Panel
#
# A set of tools to generate inspiring, interpretive (but not too interpretive) NPCs.
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    pass

def initPanel(self):

    actorsAItem = AccordionItem(title='Actors', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space="28dp")

    actorsMainBox = BoxLayout(orientation='vertical')

    actorsMainBox.add_widget(Label(text="Appearance", size_hint=(1,1)))

    actorsAgeBox = BoxLayout(orientation="horizontal")

    button = Button(text="Age - Adult", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorAgeAdult"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsAgeBox.add_widget(button)

    button = Button(text="Age - Any", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorAgeAny"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsAgeBox.add_widget(button)

    actorsMainBox.add_widget(actorsAgeBox)

    button = Button(text="Gender", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorGender"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Appearance Modifier", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorAppearanceModifier"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Visible Quirk", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorVisibleQuirk"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Non-Visible Quirk", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorNonvisibleQuirk"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    actorsMainBox.add_widget(Label(text="Motivations", size_hint=(1,1)))

    button = Button(text="Wheel (General Outlook)", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "wheelMotives"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Immediate Goals", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "dualMotives"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Relationship - Close", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = 0
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=relationshipRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Relationship - Group", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = 1
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=relationshipRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Relationship - General", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = 2
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=relationshipRoll)
    actorsMainBox.add_widget(button)

    actorsMainBox.add_widget(Label(text="Emotional Reaction"))

    actorsReactionBox = BoxLayout(orientation='horizontal')

    button = Button(text="Positive", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = "positive"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=reactionRoll)
    actorsReactionBox.add_widget(button)

    button = Button(text="Negative", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = "negative"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=reactionRoll)
    actorsReactionBox.add_widget(button)

    actorsMainBox.add_widget(actorsReactionBox)

    actorsAItem.add_widget(actorsMainBox)

    return actorsAItem

#-------------------------------------------------------------------------------------------------------------------------------------------
# actors & actor button functions
#-------------------------------------------------------------------------------------------------------------------------------------------

def miscChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = eval(args[0].function)()
    updateCenterDisplay(self, result)

def reactionRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = emotionalReaction(args[0].value)
    updateCenterDisplay(self, result)

def relationshipRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        try:
            item1, item2 = self.textInput.text.split(', ')
            if args[0].value == 0:
                result = actorRelationshipClose(item1, item2)
            if args[0].value == 1:
                result = actorRelationshipGroup(item1, item2)
            if args[0].value == 2:
                result = actorRelationshipGeneral(item1, item2)
            updateCenterDisplay(self, result)
        except:
            updateCenterDisplay(self, "Enter two values separated by a comma.")
    else:
        if args[0].value == 0:
            result = actorRelationshipClose()
        if args[0].value == 1:
            result = actorRelationshipGroup()
        if args[0].value == 2:
            result = actorRelationshipGeneral()
        updateCenterDisplay(self, result)

# logic
def actorGender():

    genderAppearance = random.choice(["male", "female"])
    return "[Gender Appearance] " + genderAppearance

def actorAppearanceModifier():

    modifier = random.choice(["Something is mysterious.", "Something is amiss.", "Is younger than appears.", "Is older than appears.", "Is in disguise.", "Wealthier than appears.", "Poorer than appears.", "Is not what they seem.", "Is exactly what they seem.", "Is impersonating someone else.", "Is more in some way than they appear.", "Is less in some way than they appear."])

    return "[Reality] " + modifier

def actorAgeAdult():

    chart = {
        2 : "Mid to late teens.",
        3 : "Nineteen or twenty.",
        4 : "Early twenties.",
        5 : "Mid-twenties.",
        6 : "Late twenties.",
        7 : "Thirties.",
        8 : "Forties.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[Age - Mature] " + chart[roll]

    return result

def actorAgeAny():

    chart = {
        2 : "Child.",
        3 : "Teen.",
        4 : "Young Adult.",
        5 : "Mature.",
        6 : "Middle-Aged.",
        7 : "Old.",
        8 : "Venerable.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[Age - Any] " + chart[roll]
    return result

def actorVisibleQuirk():

    chart = [
    "gap in front teeth", "unusual eye color", "unusual hair color", "very tall", "very short", "plump",
    "thin", "extremely average; they must work at it", "limping", "distinctive facial feature", "many hair braids", "very pale","smells like alcohol or drugs", "smells nice", "smells bad", "black eye", "light freckles", "heavy freckles", "clumsy", "looks tired", "mole", "clothes don't fit well", "clothes very tailored", "graceful", "intense eyes", "distant stare", "prominent birthmark", "prominent scar", "disfiguring scar", "faint scar", "tanned", "broken limb", "bite or claw mark scar", "paint or dye on hands", "flower or leaves in hair", "rubbing back of neck", "military bearing", "displays a totem", "has a pet", "sunburned", "paragon of their race", "exemplar of their race", "minor tattoo or mark", "many tattoos or marks", "untreated wound", "inappropriate attire", "beautiful", "plain", "ugly", "mark of special heritage", "unnaturally beautiful", "unnaturally ugly", "incredibly charismatic", "appealing", "disturbing demeanor", "repellent", "immobilizing injury", "minor birthmark", "mark of unnatural heritage", "mark of distasteful heritage", "stocky and/or wide", "tall and/or slender", "petite and/or curvy", "waifish", "lithe and/or muscular", "distinctive jewelry", "distinctive weapon", "distinctive clothes", "wearing an item of military gear", "looks tired", "carrying a wounded pet", "carrying a child", "carrying a wounded person", "carrying too little gear to be prepared for surroundings", "chewing on something", "barely remaining standing", "falls unconscious", "typical hair color for a group", "typical eye color for a group", "tall for gender", "short for gender", "robust for gender", "undersized for gender", "well-endowed in some fashion", "very long hair", "very short hair", "definite case of bed-head", "sweating heavily", "cool as a cucumber", "shrewd or piercing gaze", "constantly assessing", "completely covered in tattoos or marks", "carrying a dangerous animal", "has sharpened teeth", "mutation or power", "royal bearing", "haughty or arrogant bearing",
    ]

    return "[Visible Quirk] " + random.choice(chart)


def actorNonvisibleQuirk():

    chart = [
    "fond of rhetorical questions", "incorrigible gossip", "keeps secrets", "cusses like a sailor", "really bad cook", "really good cook", "taciturn", "gestures while talking", "physically very friendly", "stutters", "falls in love easily", "accent", "very perceptive", "very unperceptive", "chip on shoulder", "placid temperament", "volatile temperament", "paranoid", "explosive temper", "hard to rouse to anger", "holds grudges", "lets bygones be bygones", "superstitious", "conceited", "nods frequently", "has a pet", "carries a totem", "pouty", "vicious when crossed", "mixes up two languages in speech", "has a soft spot for children", "has a soft spot for orphans", "can't stand small children", "hates a common pet type", "loves a common pet type", "stuck up", "down to earth", "wistful for the past", "apprehensive about the future", "afraid of change", "loves variety", "pessimist", "optimist", "pauses frequently when speaking", "dry sense of humor", "slapstick sense of humor", "openly prejudiced", "rigorously prepared in area of expertise", "a very good friend", "values loyalty above all else", "values honor above all else", "values family above all else", "values self above all else", "emotionally damaged", "emotionally centered", "feels at peace", "feels guilty", "bad at small talk", "bad at flirtation", "bad at negotiation", "nervous when around object of attraction", "easily embarrassed", "has no shame", "easily distracted", "single-minded", "cannot read or write", "unfailingly polite", "extremely rude", "has a phobia", "very sophisticated", "jaded and cynical", "bad temper", "tends to negativity", "mutation or odd power", "prefers to wing it", "wasn't taught better", "was taught better but doesn't care", "rejects social mores", "ignores social mores", "upholds social mores", "dwells on past event", "is steered by past event", "never looks back", "fastidious", "a taker from or user of people", "very self-sacrificing", "very selfish", "bossy", "high maintenance", "low maintenance", "skittish and conflict averse", "not easily frightened", "skittish and prone to flee conflict", "arrogant", "supremely self-confident", "lacks self-confidence", "feels a particular skill or task is beyond them", "lecherous despite risks", "lecherous but discreet", "lecherous and proud of it", "discreetly chaste", "overtly prudish", "overtly chaste", "private with personal affairs", "boastful", "embodies a virtue", "embodies a vice", "embodies many virtues", "embodies many vices", "embodies a virtue and a vice", "has a particular type of person they feel it's dishonorable to strike at", "will fight anybody, any time", "boisterous",
    ]

    return "[Non-Visible Quirk] " + random.choice(chart)

def actorRelationshipClose(npc1="The first actor", npc2="the second actor"):

    closeChart = [
       "opposes every goal of", "is married/devoted to", "is close blood kin of", "is distand blood kin of",
       "hates but can't escape from", "is in love with", "is trying to ruin", "was childhood friends with",
       "grew up with", "was childhood rivals with", "came to blows with", "respects the opinion of", "disregards the value of", "finds everything objectionable about", "finds everything admirable about", "seeks out the advice of",
    ]

    overtly = random.choice(["overtly", "covertly"])
    actively = random.choice(["actively", "passively"])

    result = npc1 + " " + random.choice(closeChart) + " " + npc2 + " and expresses it " + overtly + " and " + actively + "."
    return result

def actorRelationshipGroup(npc1="The first actor", group1="the target group"):

    groupChart = [
       "is a member in good standing of", "is an escapee from", "is a lapsed member of", "is an ardent supporter of", "is a fanatic of", "seeks to undermine", "seeks to join", "seeks to disband",
       "wants to avoid contact with", "wants to be left alone by", "wants the counsel of", "is hunted by",
       "pays lip service to", "tithes regularly to", "is oppressed by", "was liberated by"
    ]

    overtly = random.choice(["overtly", "covertly"])
    actively = random.choice(["actively", "passively"])

    result = npc1 + " " + random.choice(groupChart) + " " + group1 + " and expresses it " + overtly + " and " + actively + "."
    return result

def actorRelationshipGeneral(npc1="The actor", object="the target"):

    generalChart =[
    "hates and fears", "is enraged by", "is happy with", "is thrilled by", "wants to avoid", "prefers to deal with", "wants to destroy", "wants to preserve", "wants to fight", "wants to make peace with", "wants to use", "wants to prevent others from using"
    ]

    result = npc1 + " " + random.choice(generalChart) + " " + object + "."
    return result

# various motive charts based on emotions
targetChart = [
    "chaos", "order", "right", "wrong", "skill", "secrets", "status", "power", "food", "freedom", "sex",
    "love", "nearby person", "far away person", "death", "alcohol", "danger", "honor", "pain", "ghosts",
    "the divine", "wealth", "physical struggle", "emotional struggle", "adventure", "the physical", "tax",
    "the intellectual", "the emotional", "change", "status quo", "duty", "family", "survival", "job", "hate", "illness", "lies", "mildy unsuitable target", "inappropriate target", "wildly inappropriate target",
    "death", "sex", "wealth",
]

degreesChart = [
    ["traces", "overwhelming"],
    ["slight", "great"],
    ["just a little", "quite a bit"],
    ["weak", "strong"],
    ["mild", "driving"],
    ["strong", "strong"],
    ["twinge", "driving"],
    ["mere whim", "powerful"],
    ["flirting with", "demanding"],
    ["ignorable", "nearly consuming"],
]

oddsChart = [
    ["1/8", "7/8"],
    ["1/4", "3/4"],
    ["1/3", "2/3"],
    ["1/2", "1/2"],
    ["2/3", "1/3"],
    ["3/4", "1/4"],
    ["7/8", "1/8"],
]

def getDegrees():
    degrees = degreesChart[random.randint(0,len(degreesChart)-1)]
    flip = random.choice(['same', 'flipped'])
    if flip == 'same':
        return degrees[0], degrees[1]
    else:
        return degrees[1], degrees[0]

def wheelMotives():

    emotionChart = ["interest", "curiosity", "attraction", "desire", "admiration", "surprise", "amusement", "alarm", "panic", "aversion", "disgust", "revulsion", "indifference", "familiarity", "comfort", "hope", "fear", "gratitude", "thankfulness", "joy", "elation", "triumph", "jubilation", "patience", "anger", "rage", "sorrow", "grief", "frustration", "disappointment", "humility", "pride", "charity", "sympathy", "avarice", "greed", "miserliness", "envy", "jealousy", "love", "hate", "optimistic", "serene", "joyful", "ecstatic", "loving", "accepting", "trusting", "admiring", "submissive", "apprehensive", "fearful", "terrified", "awe-filled", "distracted", "surprised", "amazed", "disapproving", "pensive", "sad", "grieving", "remorseful", "bored", "disgusted", "loathing", "contemptuous", "annoyed", "angry", "furious", "aggressive", "interested", "anticipating", "vigilant", "addicted", "apathetic", "lethargic", "lustful", "vengeful", "obsessed", "spiteful", "hateful", "jealous", "scheming", "forthright", "fatalistic", "generous", "creative", "proud", "craving", "desiring", "bitter", "driven", "ambition", "concerned", "greedy", "enthusiastic", "consumed by", "protective", "numb"]

    degree, oppdegree = getDegrees()
    degree1, oppdegree1 = getDegrees()

    emotionList = random.sample(emotionChart, 4)
    item1 = emotionList[0]
    item2 = emotionList[1]
    item3 = emotionList[2]
    item4 = emotionList[3]

    emotionPatterns = {
    1 : "[" + degree.capitalize() + "] " + item1 + ", [" + oppdegree + "] " + item2,
    2 : "[" + degree.capitalize() + "] " + item1 + ", [" + degree1 + "] " + item2,
    3 : "[" + degree.capitalize() + "] " + item1 + ", [" + degree1 + "] " + item2 + ", [" + oppdegree + "] " + item3,
    4 : "[" + degree.capitalize() + "] " + item1,
    }

    roll = random.randint(1,2)
    targetList = random.sample(targetChart, roll)

    priorityList = random.sample(["primary", "secondary"], 2)

    if roll == 2:
        target = targetList[0] + " [" + priorityList[0] + "], " +  targetList[1] + " [" + priorityList[1] + "]"
    else:
        target = targetList[0]

    result = emotionPatterns[random.randint(1,4)] + "\n[Focus] " + target

    result = "[Wheel]\n" + result
    return result

# inspired by http://goblinpunch.blogspot.com/2014/11/what-mermaids-want.html
def dualMotives():

    goalChart = [
        "to consume out of necessity", "to trade gossip", "to protect home", "to make a new friend",
        "to serve a master", "to preserve beauty", "to pass on a curse out of spite",
        "to maintain silence", "to consume endlessly", "to seduce to ruin", "to procreate",
        "to lure into a trap", "to make a living", "to find meaning in life",
        "to placate an object of worship", "to sacrifice suitable targets", "to stop the invaders",
        "to preserve life", "to hoard shiny things", "to pass on a curse and thus be rid of it",
        "to protect offspring", "to deceive for personal gain", "to deceive for the greater good",
        "to stop a greater evil", "to gain an edge over", "to avoid passing on a curse",
        "to watch over a ward", "to learn about the world", "to explore new places", "to fall in love",
        "to conquer", "to ensnare", "to see the world burn", "to find excitement", "to stir up mischief",
        "to gain resources for the tribe", "to get revenge for a petty slight",
        "to get revenge for a serious matter", "to test someone's mettle", "to test the limits of skill",
        "to create something of lasting value", "to perfect a physical being",
        "to secure their safety", "to experience the thrill of the forbidden", "to seduce for pleasure", "to seduce for nefarious purposes", "to be entertained", "to be flattered and praised",
        "to seduce to a cause or mission or betrayal", "to seduce away from a cause or mission",
        "to seduce out of duty", "to increase food stores against hardship", "to increase weapons",
        "to find a companion", "to find a cause", "to be the best at something",
        "to gain ridiculous levels of wealth", "to obtain someone else's loved one",
        "to love 'em and leave 'em", "to cuckold or embarrass a rival", "to be a hero",
        "to scout out opportunities", "to find the truth", "to find true love",
        "to destroy out of necessity", "to bully the weak", "to live like a tyrant",
        "to live like a king", "to taste a delicacy", "to perform a great deed",
        "to perform a masterwork", "to escape a prison", "to imprison someone",
        "to enjoy solitude", "to avoid others", "to learn how to socialize", "to learn a secret",
        "to perform an appointed duty", "to subvert an appointed duty", "to shirk a duty"
        "to feel alive", "to ruin someone more powerful", "to murder",
        "to steal from by stealth or trickery", "to take from by force or guile", "to discredit",
        "to break free from", "to destroy out of malice", "to overthrow a ruler",
        "to repair a great wrong", "to make things right", "to create something creative",
        "to rebuild that which is destroyed", "to mend that which is broken", "to have a polite chat",
        "to learn news of the outside world", "to acquire something simply to have it",
        "to have an intelligent conversation", "to earn freedom", "to enslave as labor or cannon fodder",
        "to get to the other side", "to acquire magic for magic's sake", "to solve a puzzle or anomaly",
        "to experience other ways of life", "to entice to a dangerous task",
        "to embark on a perilous journey", "to get someone else to assume the risk",
        "to encourage bravery", "to encourage cowardice", "to encourage love", "to encourage lust",
        "to scare off interlopers", "to acquire knowledge for knowledge's sake",
        "to trap interlopers to meet basic needs", "to trade for treasure", "to trade for exotic wares",
        "to sell fruits of someone else's labors", "to help someone else"
        "to sell someone else", "to buy someone else", "to prove worthy of an honor", "to find a way in",
        "to find a way out", "to achieve success", "to atone for a sin of omission",
        "to achieve power peacefully and rightfully", "to achieve power through force and guile",
        "to atone for a transgression", "to locate the missing", "to buy just a little more time",
        "to indulge an addiction or craving", "to transmit a disease, contagion, or state of being",
        "to achieve status", "to retrieve a mark of status", "to express the pinnacle of an art",
        "to improve beauty", "to capture beauty", "to find literal immortality",
        "to find figurative immortality", "to be youthful", "to be wise",
        "to create more", "to destroy someone's creations", "to undo a terrible mistake",
        "to find a great treasure", "to prove the ends justify the means",
        "to have a civilized conversation", "to be tutored in the ways of another culture",
        "to bestow a boon", "to bestow a curse", "to be followed somewhere", "to spite someone",
        "to be free of a curse",

    ]

    goals = random.sample(goalChart, 2)

    focusChart = {
        2 : "everyone",
        3 : "race",
        4 : "kin",
        5 : "enemy",
        6 : "myself",
        7 : "hero",
        8 : "ally",
        9 : "enemy",
        10 : "kin",
        11 : "heritage",
        12 : "anyone",
    }

    modifierChart = [
        "hero's",
        "my",
        "nearby",
        "potential",
    ]

    roll1 = random.randint(1,6) + random.randint(1,6)
    roll2 = random.choice([0, 0, 0, 0, 1, 1, 1, 2, 2, 3])

    roll3 = random.randint(1,6) + random.randint(1,6)
    roll4 = random.choice([0, 0, 0, 0, 1, 1, 1, 2, 2, 3])

    focus = []
    focus1 = focusChart[roll1]
    focus2 = focusChart[roll3]

    if (roll1 > 2 and roll1 < 6) or (roll1 > 6 and roll1 < 12):
        focus1 = modifierChart[roll2] + " " + focus1
    if (roll3 > 2 and roll3 < 6) or (roll3 > 6 and roll3 < 12):
        focus2 = modifierChart[roll4] + " " + focus2

    degree, oppdegree = getDegrees()

    goal1 = "\n[" + degree.capitalize() + "] " + goals[0] + " [" + focus1 + "] "
    goal2 = "\n[" + oppdegree.capitalize() + "] " + goals[1] + " [" + focus2 + "] "

    return "[Goals]" + goal1 + goal2

def emotionalReaction(reaction="positive"):

    negativeChart = [
    ["negative active", "anger", "annoyance", "contempt", "disgust", "irritation"],
    ["negative out of control", "anxiety", "embarrassment", "fear", "helplessness", "powerlessness", "worry"],
    ["negative", "pride", "doubt", "envy", "frustration", "guilt", "shame"],
    ["negative passive", "boredom", "despair", "disappointment", "hurt", "sadness"],
    ["agitation", "stress", "shock", "tension"],
    ]

    positiveChart = [
    ["positive active", "amusement", "delight", "elation", "excitement", "happiness", "joy", "pleasure"],
    ["positive caring", "affection", "empathy", "friendliness", "love"],
    ["positive", "courage", "hope", "humility", "satisfaction", "trust"],
    ["positive passive", "calmness", "contentment", "relaxation", "relief", "serenity"],
    ["reactive", "interest", "politeness", "surprise"],
    ]

    if reaction == "positive":
        chart = positiveChart
        oppchart = negativeChart
    else:
        chart = negativeChart
        oppchart = positiveChart

    degree, oppdegree = getDegrees()
    degree1, oppdegree1 = getDegrees()

    emotion1Chart = random.choice(chart)
    roll1 = random.randint(1, len(emotion1Chart)-1)
    emotion1 = emotion1Chart[roll1]

    emotion2Chart = random.choice(chart)
    roll2 = random.randint(1, len(emotion2Chart)-1)
    emotion2 = emotion2Chart[roll2]

    emotion3Chart = random.choice(oppchart)
    roll3 = random.randint(1, len(emotion3Chart)-1)
    emotion3 = emotion3Chart[roll3]

    emotion4Chart = random.choice(oppchart)
    roll4 = random.randint(1, len(emotion4Chart)-1)
    emotion4 = emotion4Chart[roll4]

    patterns = {
        1 : emotion1.capitalize() + " [" + degree + "]",
        2 : emotion1.capitalize() + " [" + degree + "] hidden by " + emotion3 + " [" + oppdegree + "]",
        3 : emotion1.capitalize() + " [" + degree + "], " + emotion2 + " [" + oppdegree + "]",
        4 : emotion1.capitalize() + " [" + degree + "], " + emotion2 + " [" + oppdegree + "] hidden behind " + emotion3 + " [" + degree1 + "], " + emotion4 + " [" + oppdegree1 + "]",
        5 : emotion1.capitalize() + " [" + degree + "], " + emotion2 + " [" + oppdegree + "] tinged with " + emotion3,
    }

    roll = random.randint(1,5)
    result = patterns[roll]
    return "[Reaction] " + result
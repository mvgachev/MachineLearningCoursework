import codecs
import re
import pandas as pan
import spellchecker
import display_methods as dm

from langdetect import detect
from textblob import TextBlob

from profanity_check import predict
from spellchecker import SpellChecker


def createTrainingCsv(textFile="mediaeval-2015-trainingset.txt", csvFile="training_set.csv"):
    with codecs.open(textFile, "r", encoding="utf8") as txtFileToCsv:
        with codecs.open(csvFile, 'w', encoding="utf8") as newCsvFile:
            input_txt = txtFileToCsv.readlines()
            for line in input_txt:
                record = line.replace("\t", "x0x")
                newCsvFile.write(record)
    print("Finished converting ", textFile, " into a csv")



languages = []
polarityScores = []
polarityClasses = []
subjectivityScores = []
subjectivityClasses = []
exclCounts = []
quesCounts = []
comaCounts = []
periCounts = []
quotCounts = []

errorMessage = "error"


def generateUpgradedTrainingSet(trainingSet):
    for index, row in trainingSet.iterrows():
        findTweetTextLanguage(row[1])
        findTweetTextPolarity(row[1])
        findTweetTextSubjectivity(row[1])
        getPunctuationNumbers(row[1])
    

    # trainingSet["language"] = languages
    # trainingSet["polarity"] = polarityClasses
    # trainingSet["subjectivity"] = subjectivityClasses
    # trainingSet["char_count"] = trainingSet["tweetText"].apply(lambda t: len(t)) 
    # trainingSet["word_count"] = trainingSet["tweetText"].apply(lambda t: len(t.split()))
    trainingSet["exclamation_count"] = exclCounts
    trainingSet["question_count"] = quesCounts
    trainingSet["coma_count"] = comaCounts
    trainingSet["period_count"] = periCounts
    trainingSet["quotations_count"] = quotCounts

def getPosTagCount(tweet, chosenTag):

    posTags = {
    "adjective" : ["JJ","JJR","JJS"],
    "adverb" : ["RB","RBR","RBS","WRB"],
    "noun" :  ["NN","NNS","NNP","NNPS"],
    "pronoun" : ["PRP","PRP$","WP","WP$"],
    "verb" : ["VB","VBD","VBG","VBN","VBP","VBZ"]
    }
    tagCount = 0
    blob = TextBlob(tweet)
    tweetPosTags = blob.tags
    for tweetTag in tweetPosTags:
        if tweetTag[1] in posTags[chosenTag]:
            tagCount = tagCount + 1
    return tagCount


def findTweetTextLanguage(tweet):
    try:
        language = detect(tweet)
        languages.append(language)
    except:
        print("Error: " + str(tweet))
        languages.append(errorMessage)

def findTweetTextPolarity(tweet):
    try:
        blob = TextBlob(tweet)
        polarityScore = blob.polarity
        polarityScores.append(polarityScore)

        if polarityScore < 0:
            polarityClass = "negative"
        elif polarityScore > 0:
            polarityClass = "positive"
        elif polarityScore == 0:
            polarityClass = "neutral"
        else:
            polarityClass = errorMessage

        polarityClasses.append(polarityClass)
    except:
        print("Error: " + str(tweet))
        polarityClasses.append(errorMessage)

def findTweetTextSubjectivity(tweet):
    try:
        blob = TextBlob(tweet)
        subjectivityScore = blob.subjectivity
        subjectivityScores.append(subjectivityScore)

        if subjectivityScore < 0.5:
            subjectivityClass = "negative"
        elif subjectivityScore > 0.5:
            subjectivityClass = "positive"
        elif subjectivityScore == 0.5:
            subjectivityClass = "neutral"
        else:
            subjectivityClass = errorMessage

        subjectivityClasses.append(subjectivityClass)
    except:
        print("Error: " + str(tweet))
        subjectivityClasses.append(errorMessage)


def getPunctuationNumbers(tweet):
    exclCount = 0
    quesCount = 0
    comaCount = 0
    periCount = 0
    quotCount = 0

    for i in range (0, len(tweet)):
        if tweet[i] == '!':
            exclCount = exclCount + 1
        elif tweet[i] == '?':
            quesCount = quesCount + 1
        elif tweet[i] == ',':
            comaCount = comaCount + 1
        elif tweet[i] == '.':
            periCount = periCount + 1
        elif tweet[i] == '"':
            quotCount = quotCount + 1
    
    exclCounts.append(exclCount)
    quesCounts.append(quesCount)
    comaCounts.append(comaCount)
    periCounts.append(periCount)
    quotCounts.append(quotCount)

def getNumberOfEmoticons(tweet):
    return len(re.findall(ru'[\U0001f600-\U0001f650]', tweet))

def getNumberOfHashtags(tweet):
    return len(re.findall("^#"), tweet)

def getNumberOfURLs(tweet):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return len(re.findall(regex,tweet))

def getNumberOfOffensiveWords(tweet):
    return predict(tweet)

def getNumberOfMisspelledWords(tweet):
    wordList = tweet.split()
    spellChecker = SpellChecker()
    return len(list(spellChecker.unknown(wordList)))

createTrainingCsv()
trainingSet = pan.read_csv("training_set.csv", encoding="utf8", delimiter="x0x")
generateUpgradedTrainingSet(trainingSet)
# dm.displayLanguageComposition(trainingSet)
# dm.displayLabelComposition(trainingSet)
# dm.displayPolarity(trainingSet)
# dm.displaySubjectivity(trainingSet)
# dm.displayMeanWordCount(trainingSet)
# dm.displayMeanCharacterCount(trainingSet)
dm.displayPunctuationCounts(trainingSet)
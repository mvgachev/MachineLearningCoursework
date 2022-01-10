from matplotlib import colors
import matplotlib.pyplot as plot
import numpy as np

# Shows composition of labels in training data set
def displayLabelComposition(trainingSet):
    labelComposition = trainingSet["label"].value_counts()
    labelCount = trainingSet["label"].count()
    labelTypes = trainingSet["label"].value_counts().index
    print(labelComposition)
    for counter, label in enumerate(labelTypes):
        print(label, " ", str((labelComposition[counter] / labelCount) * 100), "%")

    plot.figure()
    plot.pie(labelComposition, labels = labelTypes)
    plot.title("Labels in Training dataset")
    plot.savefig(fname="Charts/Labels-Training dataset.png")
    plot.show()

def displayLanguageComposition(trainingSet):
    languageComposition = trainingSet["language"].value_counts()
    languageCount = trainingSet["language"].count()
    languageTypes = trainingSet["language"].value_counts().index

    for counter, language in enumerate(languageTypes):
        print(language, " ", str((languageComposition[counter] / languageCount) * 100), "%")

    plot.figure()
    plot.pie(languageComposition, labels = languageTypes)
    plot.title("Languages in Training dataset")
    plot.savefig(fname="Charts/Languages-Training-dataset.png")
    plot.show()

def displayPolarity(trainingSet):
    polarityTypes = trainingSet["polarity"].value_counts().index

    realTweets = trainingSet[trainingSet["label"] == "real"]
    fakeTweets = trainingSet[trainingSet["label"] == "fake"]
    humourTweets = trainingSet[trainingSet["label"] == "humor"]

    realTweetsPolarities = realTweets["polarity"].value_counts()
    fakeTweetsPolarities = fakeTweets["polarity"].value_counts()
    humourTweetsPolarities = humourTweets["polarity"].value_counts()

    width = 0.25
    count = np.arange(len(polarityTypes))

    figures, axes = plot.subplots()
    axes.bar(count - width, realTweetsPolarities, width, label='Real')
    axes.bar(count, fakeTweetsPolarities, width, label='Fake')
    axes.bar(count + width, humourTweetsPolarities, width, label='Humor')

    axes.set_ylabel("Tweet records")
    axes.set_title("Polarity for different tweet labels")
    axes.set_xticks(count)
    axes.set_xticklabels(polarityTypes)
    axes.legend()


    figures.tight_layout()
    plot.savefig(fname="Charts/Polarity.png")

    plot.show()

def displaySubjectivity(trainingSet):
    subjectivityTypes = trainingSet["subjectivity"].value_counts().index

    realTweets = trainingSet[trainingSet["label"] == "real"]
    fakeTweets = trainingSet[trainingSet["label"] == "fake"]
    humourTweets = trainingSet[trainingSet["label"] == "humor"]

    realTweetsSubjectivities = realTweets["subjectivity"].value_counts()
    fakeTweetsSubjectivities = fakeTweets["subjectivity"].value_counts()
    humourTweetsSubjectivities = humourTweets["subjectivity"].value_counts()

    width = 0.25
    count = np.arange(len(subjectivityTypes))

    figures, axes = plot.subplots()
    axes.bar(count - width, realTweetsSubjectivities, width, label='Real')
    axes.bar(count, fakeTweetsSubjectivities, width, label='Fake')
    axes.bar(count + width, humourTweetsSubjectivities, width, label='Humor')

    axes.set_ylabel("Tweet records")
    axes.set_title("Subjectivity for different tweet labels")
    axes.set_xticks(count)
    axes.set_xticklabels(subjectivityTypes)
    axes.legend()
    figures.tight_layout()
    plot.savefig(fname="Charts/Subjectivity.png")
    plot.show()

def displayMeanWordCount(trainingSet):

    labelTypes = ["Real", "Fake", "Humour"]

    realTweets = trainingSet[trainingSet["label"] == "real"]
    fakeTweets = trainingSet[trainingSet["label"] == "fake"]
    humourTweets = trainingSet[trainingSet["label"] == "humor"]

    realTweetsMeanWordCount = realTweets["word_count"].mean()
    fakeTweetsMeanWordCount = fakeTweets["word_count"].mean()
    humourTweetsMeanWordCount = humourTweets["word_count"].mean()

    plot.figure()
    allMeanWordCounts = [realTweetsMeanWordCount, fakeTweetsMeanWordCount, humourTweetsMeanWordCount]
    arangement = np.arange(len(labelTypes))

    plot.title("Mean word counts for different tweet labels")
    plot.bar(arangement, allMeanWordCounts, align='center', color=['blue', 'red', 'orange'] )
    plot.xticks(arangement, labelTypes)
    plot.ylabel("Mean word count")
    plot.savefig(fname="Charts/Mean-word-count.png")
    plot.show()

def displayMeanCharacterCount(trainingSet):

    labelTypes = ["Real", "Fake", "Humour"]

    realTweets = trainingSet[trainingSet["label"] == "real"]
    fakeTweets = trainingSet[trainingSet["label"] == "fake"]
    humourTweets = trainingSet[trainingSet["label"] == "humor"]

    realTweetsMeanWordCount = realTweets["char_count"].mean()
    fakeTweetsMeanWordCount = fakeTweets["char_count"].mean()
    humourTweetsMeanWordCount = humourTweets["char_count"].mean()

    plot.figure()
    allMeanWordCounts = [realTweetsMeanWordCount, fakeTweetsMeanWordCount, humourTweetsMeanWordCount]
    arangement = np.arange(len(labelTypes))

    plot.title("Mean character counts for different tweet labels")
    plot.bar(arangement, allMeanWordCounts, align='center', color=['blue', 'red', 'orange'] )
    plot.xticks(arangement, labelTypes)
    plot.ylabel("Mean character count")
    plot.savefig(fname="Charts/Mean-character-count.png")
    plot.show()

def displayPunctuationCounts(trainingSet):
    punctuationTypes = ["exclamations", "questions", "comas", "periods", "quotes"]

    realTweets = trainingSet[trainingSet["label"] == "real"]
    fakeTweets = trainingSet[trainingSet["label"] == "fake"]
    humourTweets = trainingSet[trainingSet["label"] == "humor"]

    realTweetsExclamations = realTweets["exclamation_count"].mean()
    fakeTweetsExclamations = fakeTweets["exclamation_count"].mean()
    humourTweetsExclamations = humourTweets["exclamation_count"].mean()
    realTweetsQuestions = realTweets["question_count"].mean()
    fakeTweetsQuestions = fakeTweets["question_count"].mean()
    humourTweetsQuestions = humourTweets["question_count"].mean()
    realTweetsComas = realTweets["coma_count"].mean()
    fakeTweetsComas = fakeTweets["coma_count"].mean()
    humourTweetsComas = humourTweets["coma_count"].mean()
    realTweetsPeriods = realTweets["period_count"].mean()
    fakeTweetsPeriods = fakeTweets["period_count"].mean()
    humourTweetsPeriods = humourTweets["period_count"].mean()
    realTweetsQuotations = realTweets["quotations_count"].mean()
    fakeTweetsQuotations = fakeTweets["quotations_count"].mean()
    humourTweetsQuotations = humourTweets["quotations_count"].mean()

    exclamationData = [realTweetsExclamations, fakeTweetsExclamations, humourTweetsExclamations]
    questionData = [realTweetsQuestions, fakeTweetsQuestions, humourTweetsQuestions]
    comaData = [realTweetsComas, fakeTweetsComas, humourTweetsComas]
    periodData = [realTweetsPeriods, fakeTweetsPeriods, humourTweetsPeriods]
    quotationData = [realTweetsQuotations, fakeTweetsQuotations, humourTweetsQuotations]

    realData = [realTweetsExclamations, realTweetsQuestions, realTweetsComas, realTweetsPeriods, realTweetsQuotations]
    fakeData = [fakeTweetsExclamations, fakeTweetsQuestions, fakeTweetsComas, fakeTweetsPeriods, fakeTweetsQuotations]
    humourData = [humourTweetsExclamations, humourTweetsQuestions, humourTweetsComas, humourTweetsPeriods, humourTweetsQuotations]

    width = 0.15
    count = np.arange(len(punctuationTypes))

    figures, axes = plot.subplots()
    axes.bar(count - width, realData, width, label='Real', color = 'blue')
    axes.bar(count, fakeData, width, label='Fake', color = 'red')
    axes.bar(count + width, humourData, width, label='Humor', color = 'orange')

    axes.set_ylabel("Mean number of occurrence")
    axes.set_title("Mean punctuation numbers")
    axes.set_xticks(count)
    axes.set_xticklabels(punctuationTypes)
    axes.legend()
    figures.tight_layout()
    plot.savefig(fname="Charts/Punctuation.png")
    plot.show()
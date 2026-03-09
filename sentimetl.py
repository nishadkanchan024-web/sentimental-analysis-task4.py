from textblob import TextBlob

# sentences for analysis
texts = [
    "I love this product",
    "This is the worst service",
    "The movie was average",
    "I am very happy today",
    "I feel sad about this",
    "This product is very good and useful",
    "I am happy with the service",
    "The quality is excellent",
    "Very bad experience",
    "Worst product ever",
    "I am not satisfied",
    "The product is okay",
    "Average quality",
    "Nothing special",
    "Amazing performance and good quality",
    "Poor service and bad support",
    "I love this product",
    "It is disappointing",
    "Not bad but not good",
    "Highly recommended",
    "Waste of money",
    "Very happy and satisfied",
    "Terrible experience",
    "The product works fine",
    "Excellent value for money",

]

for text in texts:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("Text:", text)
    print("Sentiment:", sentiment)
    print("----------------------")
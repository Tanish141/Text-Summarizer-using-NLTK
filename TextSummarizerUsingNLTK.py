# Import Libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download stopwards (only needed once)
nltk.download('punkt')
nltk.download('stopwords')

# Example text for summarization
text = """ 
Artifical Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think humans and mimic their action.

The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and probelm-solving.
"""

# Function to generate a frequence-based summary
def summary_text(text, num_sentences=2):
    # Tokenize text into sentence and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Filter out stopwords and non-alphabetic words
    stop_words = set(stopwords.words('english'))
    word_frequencies = {}

    for word in words:
        if word.isalpha() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Score each based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Sort sentences by score and select the top 'num_sentences'
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = "".join(summary_sentences)
    return summary

# Generate and print the summary
summary = summary_text(text, num_sentences=2)
print("Original Text : \n", text)
print("\nSummary :\n", summary)   

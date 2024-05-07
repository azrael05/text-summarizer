import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.summarization import summarize

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into words, remove stopwords and punctuation, and convert to lowercase
    stop_words = set(stopwords.words('english'))
    preprocessed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
        preprocessed_sentences.append(" ".join(filtered_words))
    
    return preprocessed_sentences

# Function to generate summary
def generate_summary(text, summary_ratio=0.2):
    preprocessed_text = preprocess_text(text)
    full_text = " ".join(preprocessed_text)
    
    # Use gensim's summarize function to generate the summary
    summary = summarize(full_text, ratio=summary_ratio)
    
    return summary

# Example usage
input_text = """
   The sun cast its golden rays across the lush green meadow, painting a picturesque scene that seemed straight out of a dream. Birds chirped merrily in the trees, their songs harmonizing with the gentle rustle of leaves in the breeze. A small brook gurgled nearby, its crystal-clear waters babbling happily as they meandered through the landscape. The air was filled with the sweet scent of wildflowers, mingling with the earthy aroma of the forest. In the distance, majestic mountains loomed, their snow-capped peaks towering against the azure sky. It was a moment of perfect serenity, a fleeting glimpse of nature's boundless beauty.
"""

summary = generate_summary(input_text)
print("Summary:")
print(summary)

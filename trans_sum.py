from transformers import pipeline

classifier = pipeline("summarization",  model="Falconsai/text_summarization")
def get_summary(text):
   response = classifier(text)
   return response 

if __name__ == "__main__":
   input_text = """
   The sun cast its golden rays across the lush green meadow, painting a picturesque scene that seemed straight out of a dream. Birds chirped merrily in the trees, their songs harmonizing with the gentle rustle of leaves in the breeze. A small brook gurgled nearby, its crystal-clear waters babbling happily as they meandered through the landscape. The air was filled with the sweet scent of wildflowers, mingling with the earthy aroma of the forest. In the distance, majestic mountains loomed, their snow-capped peaks towering against the azure sky. It was a moment of perfect serenity, a fleeting glimpse of nature's boundless beauty.
   """
   print(classifier(input_text))

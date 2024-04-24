from collections import Counter
import nltk 

def remove_stopwords(text, stop_words):
  """Removes stop words from the given text."""
  words = text.lower().split() 
  filtered_words = [word for word in words if word not in stop_words]
  print("the filtered words :")
  print( " ".join(filtered_words))
  return  " ".join(filtered_words)  

def main():
  try:
    with open("random_paragraphs.txt", "r") as file:
      text = file.read()
  except FileNotFoundError:
    print("Error: File 'random_paragraphs.txt' not found.")
    return

  stop_words = nltk.corpus.stopwords.words('english')

 
  processed_text = remove_stopwords(text, stop_words)

  
  word_counts = Counter(processed_text.split())

 
  print("Word Frequency Count:")
  for word, count in word_counts.items():
    print(f"{word}: {count}")


if __name__ == "__main__":
  main()


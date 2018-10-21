## About NLTK 
------------
NLTK is a set of libraries, a whole platform for natural language processing. With the help of NLTK, you can process and analyze text in a variety of ways, tokenize and tag it, extract information, etc. NLTK is also used for prototyping and building research systems.

```python
sent_tokenize # Separação do texto pelos pontos finais e segmentação(paragrafos)
#So it knows what punctuation and characters mark the end of a sentence and the beginning of a new sentence.

word_tokenize #Separa palavra a palavra

<pos_tag #Identifica por palavra se se trata de um adjetivo, verbo, adverbio,etc 
#The process of classifying words into their parts of speech, also known as word classes or lexical categories.

```

Termos:
Sentence boundary disambiguation (SBD) -> quando temos pontos finais a sinalizar data ou pontos, o que pode levar ao algoritmo pensar que se trata do final da frase.


## About texblot
------------
TextBlob is a Python text mining tool, based on NLTK, Pattern and other NLP Tools.
https://textminingonline.com/getting-started-with-textblob 

1. blob = TextBlob(text)
```python

blob.words # Seperates text by words
blob.tags # same NLTK
blob.noun_phrases  #you can get noun phrases
blob.sentences  # same as sent_tokenize
blob.translate(to=”fr”) #tradutor
blob.sentiment #Sentiment Analysis
    Sentiment(polarity=-0.1, subjectivity=0.475) #result
blob.sentiment.polarity
blob.sentiment.subjectivity

```
And this more:
* Word Singular Pluralize
* Words Lemmatization
* Spelling Correction
* Translation and Language Detection



## About pattern
------------
Pattern is not only one of Text Processing Python NLP Tools, but a text data mining tool which including crawler, parser and etc. 

```python

```
------------
Refs:
https://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk
https://www.nltk.org/book/ch05.html 
http://textanalysisonline.com/ 
https://medium.com/activewizards-machine-learning-company/top-20-python-libraries-for-data-science-in-2018-2ae7d1db8049 
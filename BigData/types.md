# BIG DATA

# Top refs: 
https://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization 

## 5 Vs EVERYONE MUST KNOW
------------
* Volume
* Velocity
* Variety
* Veracity
* Value (The most important one, turn unless data to useless value)

## HOW TO WORK? Izyyyy:
------------
1. SEE A LOT OF VIDEOS TO LEARN MORE ABOUT IT!
2. Google it and kick explanation to save
3. Pratice one concepts analysed

## Topics that will be explained
* Text Classification
* Text Similarity
* Text Summarization
* Sentiment Analysis

## Text Classification
------------
The goal is to automatically classify the text documents into one or more defined categories
Examples:
* Understanding audience sentiment from social media,
* Detection of spam and non-spam emails,
* Auto tagging of customer queries, and
* Categorization of news articles into defined topics.

### Steps:
1. Importing Libraries
2. Importing The dataset
3. Text Preprocessing
4. Converting Text to Numbers
5. Training and Test Sets
6. Training Text Classification Model and Predicting Sentiment
7. Evaluating The Model
8. Saving and Loading the Model

### Stemming vs Lemmatization
The goal of both stemming and lemmatization is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form. For instance:
```
am, are, is -> be 
car, cars, car's, cars' -> car
```
<b> Stemming </b> usually refers to a crude heuristic process that chops off the ends of words.

<b> Lemmatization </b>usually refers to doing things properly with the use of a vocabulary and morphological analysis of words

## Text Similarity
------------
* Removing any punctuation mark.
* Transform all letters to lower cases.
* Convert extra white space as a single blank, and remove white spaces up front and at the end.
* Split the text string into separate words.

### Example:
* Input: "The sky is blue and the sun is bright."
* Output: "The sun in the sky is bright."

### Example of the processes:
* Original:
```
"The sky is blue and the sun is bright."
```
* Shingled:
```
"the sky is"    "sky is blue"   "is blue and"   "blue and the" 
"and the sun"   "the sun is"    "sun is bright"

```
## Text Summarization
------------
### Main types of how to summarize text:
* Extraction-based summarization
* Abstraction-based summarization

```
Source text: Joseph and Mary rode on a donkey to attend the annual event in Jerusalem. In the city, Mary gave birth to a child named Jesus.

Extractive summary: Joseph and Mary attend event Jerusalem. Mary birth Jesus.

Abstractive summary: Joseph and Mary came to Jerusalem where Jesus was born.
```

## Sentiment Analysis
------------
### Main types:
* Facts
* Opinions

### Processes:
* Data acquisition
* Pre-processing 
* Mining 
* Analytic Applications

To complete sentiment analyses, we need to have a dictionary of words or word list. The dictionary includes a set of standard words that depicts positive and negative words within a context. It identifies sarcasm words, innuendos, slang terms, new vocabulary, characters, and smileys that are often used in social media. These word lists can be obtained from the Internet, updated regularly, and integrated into our sentiment analyses logic.

### Examples:
```
Review classification from a movie
What features of the ThinkPad T43 do costumers like/dislike?
Tracking sentiments toward topics over time
Predictions
```

------------
#### Refs: 
https://www.linkedin.com/pulse/20140306073407-64875646-big-data-the-5-vs-everyone-must-know/
https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/ - 
https://stackabuse.com/text-classification-with-python-and-scikit-learn/
https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html

https://ethen8181.github.io/machine-learning/clustering_old/text_similarity/text_similarity.html
https://towardsdatascience.com/a-quick-introduction-to-text-summarization-in-machine-learning-3d27ccf18a9f 
https://www.ibm.com/developerworks/library/ba-sentiment-analysis-big-data/index.html 
https://pt.slideshare.net/MichelBruley/big-data-sentiment-analysis 

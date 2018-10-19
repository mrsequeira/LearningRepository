# BIG DATA

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

## Text Classification
------------
The goal is to automatically classify the text documents into one or more defined categories
Examples:
* Understanding audience sentiment from social media,
* Detection of spam and non-spam emails,
* Auto tagging of customer queries, and
* Categorization of news articles into defined topics.

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
https://ethen8181.github.io/machine-learning/clustering_old/text_similarity/text_similarity.html
https://towardsdatascience.com/a-quick-introduction-to-text-summarization-in-machine-learning-3d27ccf18a9f 
https://www.ibm.com/developerworks/library/ba-sentiment-analysis-big-data/index.html 
https://pt.slideshare.net/MichelBruley/big-data-sentiment-analysis 

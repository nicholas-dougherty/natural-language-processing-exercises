```
  _   _       _                   _               
 | \ | | __ _| |_ _   _ _ __ __ _| |              
 |  \| |/ _` | __| | | | '__/ _` | |              
 | |\  | (_| | |_| |_| | | | (_| | |              
 |_| \_|\__,_|\__|\__,_|_|  \__,_|_|              
 | |    __ _ _ __   __ _ _   _  __ _  __ _  ___   
 | |   / _` | '_ \ / _` | | | |/ _` |/ _` |/ _ \  
 | |__| (_| | | | | (_| | |_| | (_| | (_| |  __/  
 |_____\__,_|_| |_|\__, |\__,_|\__,_|\__, |\___|  
 |  _ \ _ __ ___   |___/__  ___ ___(_)___/   __ _ 
 | |_) | '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |
 |  __/| | | (_) | (_|  __/\__ \__ \ | | | | (_| |
 |_|   |_|  \___/ \___\___||___/___/_|_| |_|\__, |
                                            |___/                                              
```
***


Natural language processing (NLP) is the ability of a computer program to understand human language as it is spoken and written. As such it uses programming & machine learning techniques to interpretively exploit large amounts of text data.      
***
#### Common Use Cases and Applications of NLP

- __Voice of Customer Analytics:__ Improve products and services through analysis of customer interactions--support emails, social media posts, online comments, telephone transcriptions, et cetera fit the domain--to discover which factors drive positive and negative experiences en masse. 
    - For example: extracting key phrases and topics by summarizing blocks of text from open-ended survey responses IOT extract central ideas which craft actionable insights.

- __Semantic Search:__ Improve searchability by enabling search engine indexing of key phrases, entities, and sentimentalities. 
    - Enables narrowing a search to capture intent and context of resultant articles instead of merely the basic keywords.  

- __Knowledge Management & Discovery:__ Organize and categorize documents by topic to ease access. One may personalize content recommendations for readers by recommending relatable content. May also use to ensure security of files by closely monitoring those documents containing sensitive materials (Topic Modeling).
***

#### Methods

1. Text Classification:

- Tag/categorize text according to its content.
- Applications: 
    - sentiment analysis
    - topic labeling
    - spam detection
    - intent detection.
- Similar to topic modeling, but is supervised learning, so the set of possible classes are known/defined in advance.     
- Like topic modeling except as a supervised learning technique; hence, there is advance knowledge of possible classes defined/labeled in advance. 

2. Topic Modeling:

- Discover the abstract “topics” that occur in a collection of documents.
- Latent Dirichlet Allocation (LDA) is a commonly used algorithm.
- Similar to text classification but is unsupervised, like clustering, so the set of possible topics are unknown prior. The topics are defined during topic model generation.
***
##### The General Process Flow

1. Processing & Understanding Text
2. Feature Engineering & Text Representation
3. Supervised Learning Models for Text Data
4. Unsupervised Learning Models for Text Data
5. Advanced Topics

##### Vocabulary

- Entities: Identify the type of entity extracted, such as a person, place or organization using Named Entity.
- Stemming: Reduce words to their root, or stem. For example, 'running','runs', and 'runned' become 'run'.
- Lemmatization: Return the base or dictionary form of a word, which is the lemma. For example 'better' becomes 'good' and 'walking' becomes 'walk'. Lemmatization trys to use context to choose the lemma (truncated form), where stemming just chops down to the root form of the word.
- Tokenization: Breaking text up into linguistic units such as words or n-grams.
- Corpus: Set of documents, dataset, sample, etc.
- Document: A single observation, like the body of an email.

```
01001110110000101110100111010101110010110000101101100                         
01001100110000101101110110011101110101011000010110011101100101                
01010000111001011011110110001101100101011100110111001101101001011011101100111 
```


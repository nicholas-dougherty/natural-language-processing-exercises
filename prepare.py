#------------------------------------------------
# IMPORTS
import pandas as pd
import unicodedata
import re
import json
import acquire
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
#------------------------------------------------
#------------------------------------------------

def basic_clean(string):
    """
    receives a string, processes it and then returns its normalized version.
    Normalization via standard NKFD unicode, fed into an asii encoder and
    decoded back into UTF-8.
    """
    # .lower converts all alphabetic characters to lower-case
    string = string.lower()
    # Return the normal form for the Unicode string.
    # Return a utf-8 encoded version of the string in ascii.
    # If an error occurs, ignores the unencodable unicode from the result.
    # decodes the string using the codec registered for encoding: utf-8.
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8')
    # Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement. 
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string

#------------------------------------------------


def tokenize(string):
    """
    This function takes in a string and
    returns it in its tokenized form.  
    """
    # Create the tokenizer
    # The tok-tok tokenizer is a simple, general tokenizer, where the input has 
    # one sentence per line; thus only the final period is tokenized.
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # Use the tokenizer's tokenization to the inputted string, ensure it returns as a string.
    tokenized_string = tokenizer.tokenize(string, return_str = True)
    return tokenized_string


def stem(text):
    """
    Stemmers remove morphological affixes from words, leaving only the word stem.
    As such, this UDF is applied on a word-by-word basis, deciding what the conjugation
    is doing which aspect should be cut off. Looping or list-comprehension is 
    needed to handle multiple texts in a single executable line, and is included here.
    """
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    # use list-comprehension +> stem each word for the words inside the entire document
    # split by the default, which is a single space. 
    stems = [ps.stem(word) for word in text.split()]
    # glue it back together with spaces, as it was before. 
    # Join our lists of words into a string again; assign to a variable to save changes
    text_stemmed = ' '.join(stems)
    return text_stemmed

#------------------------------------------------

def lemmatize(text):
    """
    Lemmatization in linguistics is the process of grouping together the inflected forms
    of a word so they can be analysed as a single item, identified by the word's lemma, or dictionary form.
    This UDF algorithmically processes string and determine the lemma of a word based on its intended meaning.
    It then returns the lemmas.
    """
    # Create the Lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    # use list-comprehension to lemmatize every word.
    # string.split() => output a list of every token in the document
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    # Join our list of words into a string again; assign to a variable to save alterations.
    text_lemmatized = ' '.join(lemmas)
    
    return text_lemmatized

#------------------------------------------------

def remove_stopwords(text, extra_words = [], exclude_words = []):
    '''
    This function takes in some text, optional extra_words and exclude_words parameters
    with default empty lists and returns the text after removing all stop words.
    An alternate version of this can be created/used without the inclusion of casting to set-type. 
    (A lot is going on under the hood here, and so code-commenting is extensive.) 
    '''
    # Create stopword_list by assigning our stopwords from nltk as a list variable. 
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    # casting as a set-type, removes the order, takes away duplication 
    # (which can be unfavorable if repeated information is desired), and 
    # captures the values in {} instead of []
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Utilizing set casting, add in 'extra_words' to stopword_list
    # .union is like .append, and is the go-to option for interacting with set
    # .union establishes that every element should be unique. More technically correct and efficient. 
    stopword_list = stopword_list.union(set(extra_words))
    
    # Split document by spaces. 
    words = text.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    # Every word in our document, IFF that word is not in our stopwords.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    # Re-glued with spaces; the beginning is the end is the beginning. 
    string_sans_stopwords = ' '.join(filtered_words)
    # Gimmee shelter. 
    return string_sans_stopwords

#------------------------------------------------
    
def prep_article_data(df, column, extra_words=[], exclude_words=[]):
    '''
    This UDF processes a DataFrame and string name for a text column;  
    optionally passes lists for extra_words and exclude_words.
    Returns a DataFrame with the following aspects for the text article:
    title; the original text; and the text stemmed, lemmatized,cleaned, tokenized,
    & with stopwords removed.
    '''
    # create a column called 'clean' with the previously established UDFs.
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    # create a column called 'stemmed' with the previously established UDFs.
    df['stemmed'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(stem)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    # create a column called 'lemmatize' with the previously established UDFs.
    df['lemmatized'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(lemmatize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    return df[['title', column,'clean', 'stemmed', 'lemmatized']]

# -----------------------------------------------

def prepare_data(df, column, additional_stopwords=[]):
    '''
    This function take in a df and the name (in string) for the text column 
    with and option to pass lists for additional stopwords
    returns a df with the  original text, cleaned (tokenized and stopwords removed),
    stemmed text, lemmatized text.
    '''
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   additional_stopwords=additional_stopwords)
    
    df['stemmed'] = df['clean'].apply(stem)
    
    df['lemmatized'] = df['clean'].apply(lemmatize)
    
    return df
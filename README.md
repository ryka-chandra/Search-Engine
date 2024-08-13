# Search-Engine

## Overview

This project implements a basic search engine that uses the term frequency–inverse document frequency (tf-idf) statistic to retrieve the most relevant documents for a given query. The search engine is composed of two main components: the `Document` class, representing individual web pages or documents, and the `SearchEngine` class, which aggregates and processes a corpus of documents.

## Features

### 1. **Document Class**
Represents a single document within the corpus.

### 2. **SearchEngine Class**
Manages the corpus of documents and performs search queries using tf-idf.

## How TF-IDF Works

### Term Frequency (TF)
- **Definition**: Measures how frequently a term appears in a document.
- **Formula**: \( TF = \frac{\text{Number of times term } t \text{ appears in a document}}{\text{Total number of terms in the document}} \)

### Inverse Document Frequency (IDF)
- **Definition**: Measures how important a term is within the entire corpus.
- **Formula**: \( IDF = \log \frac{\text{Total number of documents}}{\text{Number of documents containing term } t} \)

### TF-IDF Score
- **Definition**: Combines TF and IDF to give a balanced measure of a term's relevance to a specific document within a corpus.
- **Formula**: \( \text{TF-IDF} = TF \times IDF \)

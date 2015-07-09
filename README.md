# ebertWrites
## What is it?
An algorithm that generates random text using a Markov chain. Given a training input, it parses the text into continual chains of prefixes and suffixes. The process of randomly choosing a suffix given the previous n-word prefix is repeated until a sentence has been produced. 

The idea originated from using the large movie review dataset provided by A. Mass from the Artificial Intelligence Laboratory at Stanford, hence the name ebertWrites after the famous movie critic Roger Ebert. http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
# ebertWrites
## What is it?
An algorithm that generates random text using a Markov chain. Given a training input, it parses the text into continual chains of prefixes and suffixes. It randomly chooses a suffix given a n-word prefix from the data. It then drops the first word from the previous prefix and appends the found suffix to form a new prefix. This process is repeated until a sentence has been produced.

The idea originated from making use of the large movie review dataset provided by A. Mass from the Artificial Intelligence Laboratory at Stanford. Hence, ebertWrites is named after the late Roger Ebert. http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
import re
import random
import os
import cPickle as pickle
from urllib import *

def mapText(text, prefix=2, dic={}):
	noRemove = " .'"
	text = re.sub('<[^<]+?>', '', text)
	words = re.sub(r'[^\w\s'+noRemove+']+', ' ',text).split()
	if len(words) < prefix:
		return
	for i in range(len(words)-prefix):
		pre = ()
		for j in range(prefix):
			pre += (words[i+j],)
		if pre in dic:
			dic[pre].append(words[i+prefix])
		else:
			dic[pre] = [words[i+prefix]] 
	return dic

def getChain(dic, startWords=None, prefix=2):
	minLength = 70
	maxLength = 140
	if not startWords:
		startWords = [i for i in dic.keys() if i[0][0].isupper()]
	ebertWrites = " ".join(random.choice(startWords))
	while ebertWrites[-1] != "." and ebertWrites[-1] != "!" and ebertWrites[-1] != "?":
		pre = tuple(ebertWrites.split()[-prefix:])
		if pre in dic:
			ebertWrites += " " + random.choice(dic[pre])
		else:
			if len(ebertWrites) > minLength and len(ebertWrites) <= maxLength:
				break
			getChain(dic, prefix=prefix)
	if len(ebertWrites) > minLength and len(ebertWrites) <= maxLength:
		return ebertWrites
	return getChain(dic, prefix=prefix)
	# return ebertWrites

def train(file_dic, prefix=2, txtname=None):
	train_dic = {}
	for dir_name in file_dic:
		files = file_dic[dir_name]
		for filename in files:
			f = open(dir_name + "\\" + filename, 'r')
			train_dic = mapText(f.read(), prefix=prefix, dic=train_dic)
	if not txtname:
		txtname = "dic_pre" + str(prefix) + ".txt"
	with open(txtname, 'wb') as myFile:
		pickle.dump(train_dic, myFile)
	return txtname

if __name__ == '__main__':
	"""Example from local text file
	"""
	# f = open("DeclarationOfIndependence.txt", 'r')
	# doi_dic = mapText(f.read())
	# print getChain(doi_dic)

	"""Example from online text file under Project Gutenberg License
	"""
	# sample_url = "https://www.gutenberg.org/cache/epub/27827/pg27827.txt"
	# text = urlopen(sample_url).read()
	# dic = mapText(text, prefix=2, dic={})
	# print getChain(dic, prefix=2)

	
	"""Example from Stanford Large Movie Review Dataset
	@InProceedings{maas-EtAl:2011:ACL-HLT2011,
	author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
	title     = {Learning Word Vectors for Sentiment Analysis},
	booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
	month     = {June},
	year      = {2011},
	address   = {Portland, Oregon, USA},
	publisher = {Association for Computational Linguistics},
	pages     = {142--150},
	url       = {http://www.aclweb.org/anthology/P11-1015}}
	"""
	train_bool = False
	prefix = 2
	if train_bool:
		file_dic = {}

		locations = []
		locations.append(".\\aclImdb\\train\\neg")
		locations.append(".\\aclImdb\\train\\pos")
		# locations.append(".\\aclImdb\\train\\unsup")

		for location in locations:
			file_dic[location] = os.listdir(location)
		filename = train(file_dic, prefix=prefix, txtname="dic_pre"+str(prefix)+".txt")
		# dic_pre2.txt
	saveFile = "dic_pre"+str(prefix)+".txt"
	with open(saveFile, 'rb') as myFile:
		dic = pickle.load(myFile)
	print getChain(dic, prefix=prefix)

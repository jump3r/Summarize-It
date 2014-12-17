
import gensim
from gensim import *

class Summarizer(object):

	def __init__(self):
		pass
	
	def CleanStopWords(self,text):
		#if 1: return text # TRY!!!
		fd = open("stopwords.txt", "r")
		for w in fd:
			text = text.replace(" "+w.strip()+" ", " ")
		return text	

	def ProcessArticleText(self, text):
		original_text = text
		
		#text = self.CleanStopWords(text)

		mycorp = MyCorpus(text.split("."))
		mycorp.dictionary.save("d.dict")
		corpora.MmCorpus.serialize("c.mm", mycorp)

		dic = corpora.Dictionary.load("d.dict")
		corp = corpora.MmCorpus("c.mm")

		lsi = models.LsiModel(corp, id2word = dic, num_topics=200)
		index = similarities.MatrixSimilarity(lsi[corp])

		sims = 0
		for t in [text.replace(".", " ")]:
		        t = t.strip()
		        vec_bow = dic.doc2bow(t.split(" "))
		        vec_lsi = lsi[vec_bow]

		        sims = index[vec_lsi]


		top_sorted = self.SortSimilarities(sims)
		
		highest_index = -1
		top_list_pos = 0
		summary = ""
		for k in top_sorted:
		        for i in range(len(top_sorted)):

                		if top_sorted[i][0]> highest_index:
		                        highest_index = top_sorted[i][0]
		                        top_list_pos = i

		        top_sorted[top_list_pos]=[0,0]
		        summary = original_text.split(".")[highest_index].strip() +". "+ summary
		        highest_index = -1
		
		return summary

		
	def SortSimilarities(self,sims, top = 5): # sort sims and keep index of original position within text
		if len(sims) < top:
			top = len(sims)

		top_sims = []
		for i in range(top):
		        top_sims.append([0,0])

		for i in range(len(sims)):
		        smallest = top_sims[0]
		        pos = 0
		        for p in range(len(top_sims)):

                		if top_sims[p][1]<smallest[1]:
		                        smallest = top_sims[p]
                		        pos = p
		        if sims[i]>smallest[1]:
                		top_sims[pos]=[i,sims[i]]

		return top_sims

	
class MyCorpus(gensim.corpora.TextCorpus):

	def get_texts(self):
		for sentence in self.input:
			sentence = sentence.strip()
			yield sentence.split(" ")	

s = Summarizer()
s.ProcessArticleText("Hello. World. How are you world.")
'''
star = Summarizer()
hh = star.RetrieveSectionLinks("http://www.Summarizer.com/business.html")
print len(hh)
hh = {"Divorced, $570,000 saved, but worried about retirement" : "http://www.Summarizer.com/business/personal_finance/2013/03/17/divorced_570000_saved_but_worried_about_retirement.html"}
for i in hh:
	beg = hh[i].find("2013")
	date = hh[i][beg:beg+11]
	
	s = ""
	#text = star.ParseArticleText(hh[i])
        #s = star.ProcessArticleText(text)

	
	try:
		text = star.ParseArticleText(hh[i])
		s = star.ProcessArticleText(text)
	except Exception, e:
		 print e
	
	print len(hh[i])*"="	
	print hh[i], date
	print i
        print s 

#print star.ProcessArticleText(text)
'''
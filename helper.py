import gensim as gm
import pandas as pd
df=pd.read_json('my_data.json')
similarity_object=gm.similarities.Similarity.load('sim.pkl')
dictonary=gm.corpora.Dictionary.load('dic')
my_model=gm.models.TfidfModel.load('mymodel.pkl')
def rem(index):
	
	query_doc_vec=my_model[dictonary.doc2bow(gm.utils.simple_preprocess(df.iloc[index].at['description']))]
	scores=similarity_object[query_doc_vec]
	#scores=similarity_object.similarity_by_id(1)
	sorted_scores=sorted(zip(range(scores.shape[0]),scores),reverse=True,key=lambda a: a[1])
	lt=[]
	for i,_ in sorted_scores[:100]:
		lt.append({'title':df.iloc[i].at['title'],'url':df.iloc[i].at['coverImg']})
	return lt

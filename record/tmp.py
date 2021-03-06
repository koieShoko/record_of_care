

#2つの文の品詞情報の比較をしたいけど
#MeCabは同時に複数のTaggerを持てない（上書きされる）ので
#タプルのリストとして情報を保管しておいて使う
class WordInfo():
	def __init__(self,text):
		import sys
		import MeCab
		chasen=MeCab.Tagger("-chasen -u /usr/local/lib/mecab/dic/ipadic/original.dic")
		#ノードに入っていたデータのリストを作る
		#例　[単語1の("surface","feature"),(単語2の同)…]
		node=chasen.parseToNode(text)
		self.infoTupleList=[]
		while node:
			infoStr=node.feature
			surfaceStr=node.surface
			self.infoTupleList.append((surfaceStr,infoStr))
			node=node.next
		


class IikaeTango():
	def __init__(self,t1,t2): 
		#文章を2つ用意して、品詞分解する
		w1=WordInfo(t1).infoTupleList
		w2=WordInfo(t2).infoTupleList
		self.iikaeDict={}
		count=0
		self.words=[]
		#2つの文章のcount番目の単語の情報を比較
		for x,y in zip(w1,w2):
			#辞書登録の条件①～④を満たしているときに処理
			#条件①：形態素のsurfaceが違っている
			if x[0] != y[0] :
				count+=1
				#条件②：featureの品詞部分が共通
				if x[1].split(",")[0]==y[1].split(",")[0]:
					#条件③：featureが"名詞,一般,*,*,*,*,*"じゃない
					if x[1]!='名詞,一般,*,*,*,*,*': 
						#条件④：助詞じゃない
						if x[1].split(",")[0]!="助詞":
							#全条件を満たした場合の処理
							#辞書登録の候補にする
							self.words.append((x[1],y[0]))
		#相違点が1カ所の場合だけ辞書に本登録する
		if count==1:
			self.iikaeDict=dict(self.words)
		with open('/home/jinisuke55/record_of_care/record//iikae_dict.csv','w') as f:
			writer=csv.writer(f)
			writer.writerow(['{0},{1}'.format(x.values(),x.keys()) for x in self.iikaeDict])



class Yomikomi():
	def __init__(self,path):
		import sys
		import csv
		self.iikaeDict={}
		with open(path) as f:
			rows=csv.reader(f)
			eraseSet=set()
			for row in rows:
				if row[1]!=row[2]:
					#「たずねる：尋ねる/訪ねる」系は削除
					newDict=IikaeTango(row[1],row[2]).iikaeDict
					if newDict!={}:
						iikaeKey=list(newDict.keys())[0]
						iikaeValue=newDict[iikaeKey]
						if (iikaeKey in self.iikaeDict):
							#キーが同じなら何もしない
							#キーが同じかつ値が違うなら加えず消去予定リストへ
							if (iikaeValue != self.iikaeDict[iikaeKey]):
								eraseSet.add(iikaeKey)
								#pass
						else:
							self.iikaeDict.update(newDict)
			for x in list(eraseSet):
				del self.iikaeDict[x]



#text="所により大雨によって"
class Translater(WordInfo):
	def  __init__(self,text):
		super().__init__(text)
		i=0
		textInfo=self.infoTupleList
		
		import csv
		import sys
		#介護用語のサ変リスト
		path1="/home/jinisuke55/record_of_care/record/sahenList.csv"
		sahenList=[]
		with open(path1) as f:
			rows=csv.reader(f)
			sahenList+=["".join(x)  for x in rows]
		#介護用語のサ変辞書
		
		#介護の一般名詞辞書
		path2="/home/jinisuke55/record_of_care/record/kaigoDict.csv"
		kaigoDict={}
		with open(path2) as f:
			rows=csv.reader(f)
			kaigoDict.update(dict([row  for row in rows]))
		
		
		#言いかえ
		while i < len(textInfo)-1:#最後から二番目まで
			f1=textInfo[i][1]#feature
			f2=textInfo[i+1][1]
			s1=textInfo[i][0]
			s2=textInfo[i+1][0]
			####!!!!ここは独立した分岐
			#「訪室・する」を「訪室する」にする
			if (s1 in sahenList) and ("サ変・スル" in f2):
				s1=s1+s2
				#「する」は消す
				del self.infoTupleList[i+1]
			elif (s1 in sahenList) and ("。" in f2):
				s1=s1+"する"
				del self.infoTupleList[i+1]
			else:
				if s1 in kaigoDict:
					self.infoTupleList[i]=(kaigoDict[s1],"名詞,一般,*,*,*,*,-,-,-")
				elif "助詞,副助詞,*,*,*,*,のみ,ノミ,ノミ" in f1:
					self.infoTupleList[i]=("だけ","助詞,副助詞,*,*,*,*,だけ,ダケ,ダケ")
				elif "助詞,格助詞,一般,*,*,*,にて,ニテ,ニテ" in f1:
					self.infoTupleList[i]=('によって', '助詞,格助詞,連語,*,*,*,によって,ニヨッテ,ニヨッテ' )
				elif ('動詞,自立,*,*,五段・ラ行,連用形,なる,ナリ,ナリ' == f1) and ( "、" in f2):
					self.infoTupleList[i]=('なっ', '動詞,自立,*,*,五段・ラ行,連用タ接続,なる,ナッ,ナッ')
					self.infoTupleList.insert (i+1,('て', '助詞,接続助詞,*,*,*,*,て,テ,テ'))
				elif ('名詞,非自立,助動詞語幹,*,*,*,よう,ヨウ,ヨー' in f1) and not("に" in f2) and not("だ" in f2):
					self.infoTupleList[i]=('よう','名詞,非自立,助動詞語幹,*,*,*,よう,ヨウ,ヨー')
					self.infoTupleList.insert (i+1,('に', '助詞,副詞化,*,*,*,*,に,ニ,ニ'))
				elif ('助詞,格助詞,連語,*,*,*,により,ニヨリ,ニヨリ' in f1):
					self.infoTupleList[i]=('によって', '助詞,格助詞,連語,*,*,*,によって,ニヨッテ,ニヨッテ' )
			i+=1
		self.translatedText=""
		for x in self.infoTupleList:
			self.translatedText+=x[0]

	






class Kaigokiroku():
	translatedWords=""
	def __init__(self,text):
		path1="/home/jinisuke55/record_of_care/record/nagaoka.csv"
		myDict=Yomikomi(path1).iikaeDict
		translatedWords=""
		import MeCab
		chasen=MeCab.Tagger("-chasen -u /usr/local/lib/mecab/dic/ipadic/original.dic")
		words=chasen.parseToNode(text)
		while words.next!=None:
			if words.feature in myDict:
				translatedWords+=myDict[words.feature]
			else:
				translatedWords+=words.surface
			words=words.next
		##さらに言いかえ
		translatedWords=Translater(translatedWords).translatedText
		self.translatedWords+=translatedWords				

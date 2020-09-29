
class Translater():
	translated_text=""
	def __init__(self,text):
		t_translated_text    = Technical_term_translater(text).translated_text
		g_translated_text    = General_term_ranslater(t_translated_text).translated_text
		u_translated_text    = Users_term_ranslater(). translate_by_users_dict(g_translated_text)
		self.translated_text = u_translated_text
	




#2つの文の品詞情報の比較をしたいけど
#MeCabは同時に複数のTaggerを持てない（上書きされる）ので
#タプルのリストとして情報を保管しておいて使う
class WordInfo():
	def __init__(self,text):
		import sys
		import MeCab
		chasen=MeCab.Tagger("-chasen -u /usr/local/lib/mecab/dic/ipadic/original.dic")
		#ノードに入っていたデータのリストを作り、これをインスタンス変数として持つ
		#例　[単語1の("surface","feature"),(単語2の同)…]
		node=chasen.parseToNode(text)
		self.surface_feature_TL=[]
		while node:
			featureStr=node.feature
			surfaceStr=node.surface
			self.surface_feature_TL.append((surfaceStr,featureStr))
			node=node.next
		




class Technical_term_translater():
	def  __init__(self,text):
		self.translated_text=""#インスタンス変数
		surface_feature_TL=WordInfo(text).surface_feature_TL.copy()	
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
		i=0
		f2=""
		while not ('BOS/EOS'in f2):
			f1=surface_feature_TL[i][1]
			f2=surface_feature_TL[i+1][1]
			s1=surface_feature_TL[i][0]
			s2=surface_feature_TL[i+1][0]
			####!!!!ここは独立した分岐
			#「訪室・する」を「訪室する」にする
			if (s1 in sahenList) and ("サ変・スル" in f2):
				s1=s1+s2
				#「する」は消す
				del surface_feature_TL[i+1]
			elif (s1 in sahenList) and ("。" in f2):
				s1=s1+"しました"
				del surface_feature_TL[i+1]
			else:
				pass
			if s1 in kaigoDict:
				surface_feature_TL[i]=(kaigoDict[s1],"名詞,一般,*,*,*,*,-,-,-")
			elif "助詞,副助詞,*,*,*,*,のみ,ノミ,ノミ" in f1:
				surface_feature_TL[i]=("だけ","助詞,副助詞,*,*,*,*,だけ,ダケ,ダケ")
			elif "助詞,格助詞,一般,*,*,*,にて,ニテ,ニテ" in f1:
				surface_feature_TL[i]=('によって', '助詞,格助詞,連語,*,*,*,によって,ニヨッテ,ニヨッテ' )
			elif ('動詞,自立,*,*,五段・ラ行,連用形,なる,ナリ,ナリ' == f1) and ( "、" in f2):
				surface_feature_TL[i]=('なっ', '動詞,自立,*,*,五段・ラ行,連用タ接続,なる,ナッ,ナッ')
				surface_feature_TL.insert (i+1,('て', '助詞,接続助詞,*,*,*,*,て,テ,テ'))
			elif ('名詞,非自立,助動詞語幹,*,*,*,よう,ヨウ,ヨー' in f1) and not("に" in f2) and not("だ" in f2):
				surface_feature_TL[i]=('よう','名詞,非自立,助動詞語幹,*,*,*,よう,ヨウ,ヨー')
				surface_feature_TL.insert (i+1,('に', '助詞,副詞化,*,*,*,*,に,ニ,ニ'))
			elif ('助詞,格助詞,連語,*,*,*,により,ニヨリ,ニヨリ' in f1):
				surface_feature_TL[i]=('によって', '助詞,格助詞,連語,*,*,*,によって,ニヨッテ,ニヨッテ' )


			####文章を短くする####

			####ですます調####
			##3形態素にまたがる処理
#			elif (i <len(textInfo)-2):
#				f3=textInfo[i+2][1]
#				s3=textInfo[i+2][0]
#				
#過去形はまだできてない				if ('動詞' in s1) and ('た' in s2) and ('。' in s3):#勝った→勝ちました
#					if ('っ' in s1 ) and ('連用タ接続' in f1):
#						surface_feature_TL[i] = (s1[0:-1]+chr(ord(s1[-1])-2),f1.replace('連用タ接続','連用形'))
#					surface_feature_TL.insert (i+1,'まし', '助動詞,*,*,*,特殊・マス,連用形,ます,マシ,マシ')		
			elif ('。' in f2):
				print(s1+s2)
				if ('動詞,自立' in f1):
					if ('五段・タ行' in f1) :#勝つ→勝ちました
						surface_feature_TL[i] = (s1[0:-1]+chr(ord(s1[-1])-3),f1.replace('基本','連用'))
						## 本当は形態素情報のうちの読みの部分も書き換えないといけない。						
						## 現状は実害ないけどのちのちバグの温床になる可能性があるので
						# 余裕があれば直す事
					elif ("五段・ワ行促音便" in f1) or ("五段・サ行" in f1) or ('五段・カ行促音便' in  f1) :
						surface_feature_TL[i] = (s1[0:-1]+chr(ord(s1[-1])-2),f1.replace('基本','連用'))					
					elif ("五段" in f1) :#出す→出しました
						surface_feature_TL[i] = (s1[0:-1]+chr(ord(s1[-1])-1),f1.replace('基本','連用'))
					elif ("一段" in f1):#見る→見ました
						surface_feature_TL[i] = (s1[0:-1],f1.replace('基本','連用'))
					elif ('サ変' in f1 ):
						surface_feature_TL[i] = ('し','し', '動詞,自立,*,*,サ変・スル,連用形,する,シ,シ')
					elif ("カ変・クル" in f1):
						surface_feature_TL[i] =("き",'動詞,自立,*,*,カ変・クル,連用形,くる,キ,キ')
					elif ("カ変・来ル" in f1):
						surface_feature_TL[i] =("来",'動詞,自立,*,*,カ変・来ル,連用形,来る,キ,キ')
					surface_feature_TL.insert(i+1,('ます', '助動詞,*,*,*,特殊・マス,基本形,ます,マス,マス'))

				####サ変名詞止めをやめさせる####
				elif ('名詞,サ変接続' in f1 ):
					surface_feature_TL.insert(i+1,('し', '動詞,自立,*,*,サ変・スル,連用形,する,シ,シ'))
					surface_feature_TL.insert(i+2,('ます','助動詞,*,*,*,特殊・マス,基本形,ます,マス,マス'))					
				####体言止めをやめさせる####
				elif ('名詞' in f1 ) and not('サ変' in f1):
					surface_feature_TL.insert(i+1,('です', '助動詞,*,*,*,特殊・デス,基本形,です,デス,デス'))
				####形容詞止めをやめさせる####
				elif ('形容詞' in f1 ):
					surface_feature_TL.insert(i+1,('です', '助動詞,*,*,*,特殊・デス,基本形,です,デス,デス'))	
			i+=1
		for x in surface_feature_TL:
			self.translated_text+=x[0]

	
class General_term_ranslater():
	translated_text=""
	general_term_dict={}
	def __init__(self,text):
		#非専門用語の辞書を読み込む
		#(1)この場で新しく辞書を作って読み込む場合
		#self.make_general_term_dict_now()
		#(2)あらかじめ作って置いたのを読み込む場合
		path="/home/jinisuke55/record_of_care/record/iikae_dict.csv"
		self.make_general_term_dict_from_existing_csv(path)

		self.translate(text)
		
	def make_general_term_dict_from_existing_csv(self,path):
		#介護用語の辞書を読み込む（あらかじめ作って置いたのを読み込むパターン）
		import csv
		with open(path)  as f:
			rows=csv.reader(f,delimiter="\t")
			self.general_term_dict.update(dict([row  for row in rows]))

	def make_general_term_dict_now(self):
		#まずは、｛難しい非専門用語：やさしい日本語｝の対を1組作る関数を定義
		def make_proposed_general_term_dict(t1,t2):
			#文章を2つ用意して、品詞分解する
			w1=WordInfo(t1).surface_feature_TL
			w2=WordInfo(t2).surface_feature_TL
			proposed_general_term_dict={}
			count=0
			words=[]
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
								words.append((x[1],y[0]))
			#相違点が1カ所の場合だけ辞書に本登録する
			if count==1:
				proposed_general_term_dict=dict(words)
			return proposed_general_term_dict

		#上記の関数を使って、文例のcsvから非専門用語辞書を作っていく
		path="/home/jinisuke55/record_of_care/record/nagaoka.csv"
		import sys
		import csv
		with open(path) as f:
			rows=csv.reader(f)
			eraseSet=set()
			for row in rows:
				if row[1]!=row[2]:
					#「たずねる：尋ねる/訪ねる」系は削除
					newDict=make_proposed_general_term_dict(row[1],row[2])
					if newDict!={}:
						iikaeKey=list(newDict.keys())[0]
						iikaeValue=newDict[iikaeKey]
						if (iikaeKey in self.general_term_dict):
							#キーが同じなら何もしない
							#キーが同じかつ値が違うなら加えず消去予定リストへ
							if (iikaeValue != self.general_term_dict[iikaeKey]):
								eraseSet.add(iikaeKey)
						else:
							self.general_term_dict.update(newDict)
			for x in list(eraseSet):
				del self.general_term_dict[x]
		#結果のログを残す
		with open('/home/jinisuke55/record_of_care/record/iikae_dict.csv','w') as f:
			writer=csv.writer(f, delimiter="\n")
			writer.writerow(['{0}\t{1}'.format(x,y) for x,y in self.general_term_dict.items()])
	
	def translate(self,text):
		import MeCab
		chasen=MeCab.Tagger("-chasen -u /usr/local/lib/mecab/dic/ipadic/original.dic")
		translated_words=""
		words=chasen.parseToNode(text)
		while words.next!=None:
			if words.feature in self.general_term_dict:
				translated_words+=self.general_term_dict[words.feature]
			else:
				translated_words+=words.surface
			words=words.next
		self.translated_text=translated_words				


def wakatigaki(text):
	import MeCab
	wakati=MeCab.Tagger("-Owakati -u /usr/local/lib/mecab/dic/ipadic/original.dic")
	words=wakati.parse(text)
	wakatigaki_words="".join(words)
	return wakatigaki_words			






class Users_term_ranslater():
	def translate_by_users_dict(self,text):
		from record.models import Technical_noun
		technical_nouns = Technical_noun.objects.all()
		for technical_noun in technical_nouns:
			if technical_noun.before in text and technical_noun.necessity_of_translate == True:
				text = text.replace(technical_noun.before, technical_noun.after)
		return text
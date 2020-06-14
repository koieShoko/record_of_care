
class wordKatuyou:
	def __init__(self):
		# 結果用
		self.wordDic = []
		# 入力単語用
		self.word = ''
		self.word_br = ''
		self.word_bs = ''
		self.word_gc = ''
		self.word_gp = ''
		self.word_gq = ''
		# 読み仮名用
		self.yomi = '*'
		self.yomi_br = '*'
		self.yomi_bs = '*'
		# 活用検索用
		self.char_A = ["あ","か","が","さ","ざ","た","だ","な","は","ば","ぱ","ま","や","ら","わ"]
		self.char_I = ["い","き","ぎ","し","じ","ち","ぢ","に","ひ","び","ぴ","み","－","り","い"]
		self.char_U = ["う","く","ぐ","す","ず","つ","づ","ぬ","ふ","ぶ","ぷ","む","ゆ","る","う"]
		self.char_E = ["え","け","げ","せ","ぜ","て","で","ね","へ","べ","ぺ","め","－","れ","え"]
		self.char_O = ["お","こ","ご","そ","ぞ","と","ど","の","ほ","ぼ","ぽ","も","よ","ろ","お"]
		self.char_T = ["ん","っ"]
		self.num_X = self.num_Y = 0

	def Katuyou(self, word, yomi='*'):
		# 入力単語
		self.word = word
		self.word_br = word[:-1]
		self.word_bs = word[:-2]
		self.word_gc = word[-1:]
		self.word_gp = word[-2:-1]
		self.word_gq = word[-3:-2]
		# 読み仮名
		if yomi != '*':
			self.yomi = yomi
			self.yomi_br = yomi[:-1]
			self.yomi_bs = yomi[:-2]

		for n in range(0, 15):
			if self.word_gc == self.char_U[n]:
				self.num_X = n
			if self.word_gp == self.char_I[n] or self.word_gp == self.char_E[n]:
				self.num_Y = n

		if word == '来る' or word == 'くる':
			print('カ変変格活用')
		elif self.word_gp == 'す' and self.word_gc == 'る':
			print ('さ行変格活用')
			self.wordDic.append(word+',*,*,*,動詞,自立,*,*,サ変,基本形,'+word+','+yomi+','+yomi+',独自辞書-動詞')
			self.wordDic.append(self.word_bs+'さ,*,*,*,動詞,自立,*,*,サ変,未然形,'+word+','+self.yomi_bs+'サ,'+self.yomi_bs+'サ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'し,*,*,*,動詞,自立,*,*,サ変,未然形,'+word+','+self.yomi_bs+'シ,'+self.yomi_bs+'シ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'せ,*,*,*,動詞,自立,*,*,サ変,未然形,'+word+','+self.yomi_bs+'セ,'+self.yomi_bs+'セ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'し,*,*,*,動詞,自立,*,*,サ変,連用形,'+word+','+self.yomi_bs+'シ,'+self.yomi_bs+'シ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'する,*,*,*,動詞,自立,*,*,サ変,終止形,'+word+','+self.yomi_bs+'スル,'+self.yomi_bs+'スル,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'する,*,*,*,動詞,自立,*,*,サ変,連体形,'+word+','+self.yomi_bs+'スル,'+self.yomi_bs+'スル,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'すれ,*,*,*,動詞,自立,*,*,サ変,仮定形,'+word+','+self.yomi_bs+'スレ,'+self.yomi_bs+'スレ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'しろ,*,*,*,動詞,自立,*,*,サ変,命令形,'+word+','+self.yomi_bs+'シロ,'+self.yomi_bs+'シロ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'せよ,*,*,*,動詞,自立,*,*,サ変,命令形,'+word+','+self.yomi_bs+'セヨ,'+self.yomi_bs+'セヨ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'せる,*,*,*,動詞,自立,*,*,サ変,可能動詞,'+word+','+self.yomi_bs+'セル,'+self.yomi_bs+'セル,独自辞書-動詞')
		elif (self.word_gp == 'じ' or self.word_gp == 'ず') and self.word_gp == 'る':
			print ('ざ行変格活用')
			self.wordDic.append(word+',*,*,*,動詞,自立,*,*,ザ変,基本形,'+word+','+yomi+','+yomi+',独自辞書-動詞')
			self.wordDic.append(self.word_bs+'じ,*,*,*,動詞,自立,*,*,ザ変,未然形,'+word+','+self.yomi_bs+'ジ,'+self.yomi_bs+'ジ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'ぜ,*,*,*,動詞,自立,*,*,ザ変,未然形,'+word+','+self.yomi_bs+'ゼ,'+self.yomi_bs+'ゼ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'じ,*,*,*,動詞,自立,*,*,ザ変,連用形,'+word+','+self.yomi_bs+'ジ,'+self.yomi_bs+'ジ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'じる,*,*,*,動詞,自立,*,*,ザ変,終止形,'+word+','+self.yomi_bs+'ジル,'+self.yomi_bs+'ジル,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'ずる,*,*,*,動詞,自立,*,*,ザ変,終止形,'+word+','+self.yomi_bs+'ズル,'+self.yomi_bs+'ズル,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'じる,*,*,*,動詞,自立,*,*,ザ変,連体形,'+word+','+self.yomi_bs+'ジル,'+self.yomi_bs+'ジル,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'ずる,*,*,*,動詞,自立,*,*,ザ変,連体形,'+word+','+self.yomi_bs+'ズル,'+self.yomi_bs+'ズル,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'じれ,*,*,*,動詞,自立,*,*,ザ変,仮定形,'+word+','+self.yomi_bs+'シレ,'+self.yomi_bs+'ジレ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'ずれ,*,*,*,動詞,自立,*,*,ザ変,仮定形,'+word+','+self.yomi_bs+'ズレ,'+self.yomi_bs+'ズレ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'じろ,*,*,*,動詞,自立,*,*,ザ変,命令形,'+word+','+self.yomi_bs+'ジロ,'+self.yomi_bs+'ジロ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'ぜよ,*,*,*,動詞,自立,*,*,ザ変,命令形,'+word+','+self.yomi_bs+'ゼヨ,'+self.yomi_bs+'ゼヨ,独自辞書-動詞')
			self.wordDic.append(self.word_bs+'ぜる,*,*,*,動詞,自立,*,*,ザ変,可能動詞,'+word+','+self.yomi_bs+'ゼル,'+self.yomi_bs+'ゼル,独自辞書-動詞')
		elif word == '行く' or word == 'いく' or word == 'ける' or word == '競る' or word == 'てる':
			print ('五段')
			self.wordDic.append(self.word_br+'っ,*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,連用形,'+self.word+','+self.yomi_br+'ッ,'+self.yomi_br+'ッ,独自辞書-動詞')
			self.KatuyouGodan()
		elif not ('あ' <= self.word_gp <= 'ん' or 'ア' <= self.word_gp <= 'ン') and self.word_gc == 'る':
			m = self.char_A[self.num_Y]
			self.char_A[self.num_Y] = 'O'
			self.KatuyouIchidan()
			self.char_A[self.num_Y] = m
		elif self.word_gc == 'る' and self.num_Y >= 0:
			self.KatuyouIchidan()
		elif word == 'ぬ':
			print ('打ち消し助動詞')
			self.wordDic.append(word+',*,*,*,打消助動詞,自立,*,*,*,基本形,'+word+','+yomi+','+yomi+',独自辞書-助動詞')
			self.wordDic.append('ず,*,*,*,打消助動詞,自立,*,*,*,連用形,'+word+',ズ,ズ,独自辞書-助動詞')
			self.wordDic.append('ぬ,*,*,*,打消助動詞,自立,*,*,*,終止形,'+word+',ヌ,ヌ,独自辞書-助動詞')
			self.wordDic.append('ん,*,*,*,打消助動詞,自立,*,*,*,終止形,'+word+',ン,ン,独自辞書-助動詞')
			self.wordDic.append('ぬ,*,*,*,打消助動詞,自立,*,*,*,連体形,'+word+',ヌ,ヌ,独自辞書-助動詞')
			self.wordDic.append('ん,*,*,*,打消助動詞,自立,*,*,*,連体形,'+word+',ン,ン,独自辞書-助動詞')
			self.wordDic.append('ね,*,*,*,打消助動詞,自立,*,*,*,仮定形,'+word+',ネ,ネ,独自辞書-助動詞')
		elif word == 'う' or word == 'よぅ' or word == 'まい':
			print ('意思助動詞系')
			self.wordDic.append(word+',*,*,*,意志助動詞,自立,*,*,*,基本形,'+word+','+yomi+','+yomi+',独自辞書-助動詞')
			self.wordDic.append(word+',*,*,*,意志助動詞,自立,*,*,*,終止形,'+word+','+yomi+','+yomi+',独自辞書-助動詞')
			self.wordDic.append(word+',*,*,*,意志助動詞,自立,*,*,*,連体形,'+word+','+yomi+','+yomi+',独自辞書-助動詞')
		elif word == 'です' or word == 'ます':
			print ('丁寧助動詞系')
			self.wordDic.append(word+',*,*,*,丁寧動詞,自立,*,*,*,基本形,'+word+','+yomi+','+yomi+',独自辞書-助動詞')
			self.wordDic.append(self.word_br+'しょ,*,*,*,丁寧動詞,自立,*,*,*,未然形,'+word+','+self.yomi_br+'ショ,'+self.yomi_br+'ショ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'し,*,*,*,丁寧動詞,自立,*,*,*,連用形,'+word+','+self.yomi_br+'シ,'+self.yomi_br+'シ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'す,*,*,*,丁寧動詞,自立,*,*,*,終止形,'+word+','+self.yomi_br+'ス,'+self.yomi_br+'ス,独自辞書-助動詞')
		elif self.char_A[self.num_X] == 'あ' or self.char_A[self.num_X] == 'た' or self.char_A[self.num_X] == 'ら' or self.char_A[self.num_X] == 'わ':
			print ('五段')
			self.wordDic.append(self.word_br+'っ,*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,連用形,'+self.word+','+self.yomi_br+'ッ,'+self.yomi_br+'ッ,独自辞書-動詞')
			self.KatuyouGodan()
		elif self.char_A[self.num_X] == 'ま' or self.char_A[self.num_X] == 'は' or self.char_A[self.num_X] == 'な':
			print ('五段')
			self.wordDic.append(self.word_br+'ん,*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,連用形,'+self.word+','+self.yomi_br+'ン,'+self.yomi_br+'ン,独自辞書-動詞')
			self.KatuyouGodan()
		elif self.char_A[self.num_X] == 'か' or self.char_A[self.num_X] == 'が':
			print ('五段')
			self.wordDic.append(self.word_br+'い,*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,連用形,'+self.word+','+self.yomi_br+'イ,'+self.yomi_br+'イ,独自辞書-動詞')
			self.KatuyouGodan()
		elif self.char_A[self.num_X] == 'さ':
			print ('五段')
			self.wordDic.append(self.word_br+self.char_I[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,連用形,'+self.word+','+self.yomi_br+self.char_I[self.num_X]+','+self.yomi_br+self.char_I[self.num_X]+',独自辞書-動詞')
			self.KatuyouGodan()
		elif self.word_gc == 'い':
			print ('形容詞活用')
			self.wordDic.append(word+',*,*,*,形容詞,自立,*,*,*,基本形,'+word+','+yomi+','+yomi+',独自辞書-助動詞')
			self.wordDic.append(self.word_br+'く,*,*,*,形容詞,自立,*,*,*,未然形,'+word+','+self.yomi_br+'ク,'+self.yomi_br+'ク,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'かろ,*,*,*,形容詞,自立,*,*,*,未然形,'+word+','+self.yomi_br+'カロ,'+self.yomi_br+'カロ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'く,*,*,*,形容詞,自立,*,*,*,連用形,'+word+','+self.yomi_br+'ク,'+self.yomi_br+'ク,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'かっ,*,*,*,形容詞,自立,*,*,*,連用形,'+word+','+self.yomi_br+'カッ,'+self.yomi_br+'カッ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'い,*,*,*,形容詞,自立,*,*,*,終止形,'+word+','+self.yomi_br+'イ,'+self.yomi_br+'イ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'い,*,*,*,形容詞,自立,*,*,*,連体形,'+word+','+self.yomi_br+'イ,'+self.yomi_br+'イ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'けれ,*,*,*,形容詞,自立,*,*,*,仮定形,'+word+','+self.yomi_br+'ケレ,'+self.yomi_br+'ケレ,独自辞書-助動詞')
		elif self.word_gc == 'だ':
			print ('形容動詞系')
			self.wordDic.append(word+',*,*,*,形容動詞,自立,*,*,*,基本形,'+word+','+yomi+','+yomi+',独自辞書-助動詞')
			self.wordDic.append(self.word_br+'で,*,*,*,形容動詞,自立,*,*,*,未然形,'+word+','+self.yomi_br+'デ,'+self.yomi_br+'デ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'だろ,*,*,*,形容動詞,自立,*,*,*,未然形,'+word+','+self.yomi_br+'ダロ,'+self.yomi_br+'ダロ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'で,*,*,*,形容動詞,自立,*,*,*,連用形,'+word+','+self.yomi_br+'デ,'+self.yomi_br+'デ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'だっ,*,*,*,形容動詞,自立,*,*,*,連用形,'+word+','+self.yomi_br+'ダッ,'+self.yomi_br+'ダッ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'に,*,*,*,形容動詞,自立,*,*,*,連用形,'+word+','+self.yomi_br+'ニ,'+self.yomi_br+'ニ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'だ,*,*,*,形容動詞,自立,*,*,*,終止形,'+word+','+self.yomi_br+'ダ,'+self.yomi_br+'ダ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'だ,*,*,*,形容動詞,自立,*,*,*,連体形,'+word+','+self.yomi_br+'ナ,'+self.yomi_br+'ナ,独自辞書-助動詞')
			self.wordDic.append(self.word_br+'なら,*,*,*,形容動詞,自立,*,*,*,仮定形,'+word+','+self.yomi_br+'ナラ,'+self.yomi_br+'ナラ,独自辞書-助動詞')
		else:
			print ('良く分かりませんでしたとさ･･･。\n基本形で、入力しなおしてください＼(＾o＾)／')
		return self.wordDic

	def KatuyouIchidan(self):
		self.wordDic.append(self.word+',*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,基本形,'+self.word+','+self.yomi+','+self.yomi+',独自辞書-動詞')
		self.wordDic.append(self.word_br+',*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,未然形,'+self.word+','+self.yomi_br+','+self.yomi_br+',独自辞書-動詞')
		self.wordDic.append(self.word_br+',*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,連用形,'+self.word+','+self.yomi_br+','+self.yomi_br+',独自辞書-動詞')
		self.wordDic.append(self.word_br+'る,*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,終止形,'+self.word+','+self.yomi_br+'ル,'+self.yomi_br+'ル,独自辞書-動詞')
		self.wordDic.append(self.word_br+'る,*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,連体形,'+self.word+','+self.yomi_br+'ル,'+self.yomi_br+'ル,独自辞書-動詞')
		self.wordDic.append(self.word_br+'れ,*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,仮定形,'+self.word+','+self.yomi_br+'レ,'+self.yomi_br+'レ,独自辞書-動詞')
		self.wordDic.append(self.word_br+'ろ,*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,命令形,'+self.word+','+self.yomi_br+'ロ,'+self.yomi_br+'ロ,独自辞書-動詞')
		self.wordDic.append(self.word_br+'よ,*,*,*,動詞,自立,*,*,一段・'+self.char_A[self.num_Y]+'行,命令形,'+self.word+','+self.yomi_br+'ヨ,'+self.yomi_br+'ヨ,独自辞書-動詞')

	def KatuyouGodan(self):
		self.wordDic.append(self.word+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,基本形,'+self.word+','+self.yomi+','+self.yomi+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_A[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,未然形,'+self.word+','+self.yomi_br+self.char_A[self.num_X]+','+self.yomi_br+self.char_A[self.num_X]+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_O[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,未然形,'+self.word+','+self.yomi_br+self.char_O[self.num_X]+','+self.yomi_br+self.char_O[self.num_X]+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_I[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,連用形,'+self.word+','+self.yomi_br+self.char_I[self.num_X]+','+self.yomi_br+self.char_I[self.num_X]+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_U[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,終止形,'+self.word+','+self.yomi_br+self.char_U[self.num_X]+','+self.yomi_br+self.char_U[self.num_X]+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_U[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,連体形,'+self.word+','+self.yomi_br+self.char_U[self.num_X]+','+self.yomi_br+self.char_U[self.num_X]+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_E[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,仮定形,'+self.word+','+self.yomi_br+self.char_E[self.num_X]+','+self.yomi_br+self.char_E[self.num_X]+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_E[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,命令形,'+self.word+','+self.yomi_br+self.char_E[self.num_X]+','+self.yomi_br+self.char_E[self.num_X]+',独自辞書-動詞')
		self.wordDic.append(self.word_br+self.char_E[self.num_X]+',*,*,*,動詞,自立,*,*,五段・'+self.char_A[self.num_X]+'行,可能動詞,'+self.word+','+self.yomi_br+self.char_E[self.num_X]+','+self.yomi_br+self.char_E[self.num_X]+',独自辞書-動詞')

if __name__ == '__main__':
	w = wordKatuyou()
	while True:
		word = input('INPUT WORD (finish = n) > ')
		yomi = input('INPUT YOMI (finish = n) > ')
		if word == 'n' or yomi == 'n':
			break
		for k in w.Katuyou(word,yomi):
			print(k)
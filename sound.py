import pyttsx3 #テキストを読み上げることができるライブラリ
engine = pyttsx3.init()

#参照した言葉
words = ["黒より黒く、闇より暗き漆黒に、我が深紅の混淆を望みたもう。",
        "覚醒のとき来たれり。無謬の境界に落ちしことわり。無行の歪みとなりて現出せよ！",
        "踊れ、踊れ、踊れ。我が力の奔流に望むは崩壊なり。並ぶ者なき崩壊なり。",
        "万象等しくかいじんに帰し、深淵よりきたれ！",
        "これが、人類最大の威力の攻撃手段。これこそが、究極の攻撃魔法。",
        "エクスプロージョン！"
        ]



rate = engine.getProperty("rate")
engine.setProperty("rate",150)

volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)

#参照した言葉の出力
for word in words:
    engine.say(word) #読み込み

engine.runAndWait()  #出力










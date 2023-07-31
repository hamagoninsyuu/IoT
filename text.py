import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile("test.wav") as source: #音声ファイル呼び出し
  audio = r.record(source) #音声ファイルをr.recordにセット
  
text = r.recognize_google(audio, language='ja-JP') #変換
print(text) #出力


#テキスト化したやつをファイルに保存する
with open('voice.txt', 'w') as f:
  f.write(text)





import pyaudio  #録音機能を使うためのライブラリ
import wave     #wavファイルを扱うためのライブラリ

RECORD_SECONDS = 10 #録音する時間の長さ（秒）
WAVE_OUTPUT_FILENAME = "test.wav" #音声を保存するファイル名
iDeviceIndex = 0 #録音デバイスのインデックス番号（マイクに付けられている番号）

#基本情報の設定
FORMAT = pyaudio.paInt16 #音声のフォーマット 16ビットバイナリ文字列　音量の解像度65536段階で音量をデータ化　CD基準
CHANNELS = 1             #モノラル(右からも左からも同じ音。) ステレオ
RATE = 44100             #サンプルレート(時間軸で見た音の解像度) 1秒間で44100回録音 CD基準　
CHUNK = 2**10            #データ点数 良く分からん 1回読み込むときのデータサイズ？？ 区切り？ 参考サイトは2**11やったけど 他のサイトは2**10が多かったから変えてみた
audio = pyaudio.PyAudio() #pyaudio.PyAudio() 

stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index = iDeviceIndex, #録音デバイスのインデックス番号
        frames_per_buffer=CHUNK)

#--------------録音開始---------------
print ("recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)


print ("finished recording")

#--------------録音終了---------------

stream.stop_stream() 
stream.close() 
audio.terminate()



#多分wavファイルに録音した情報を保存
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()



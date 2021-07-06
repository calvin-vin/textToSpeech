import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import PyPDF2
from gtts import gTTS
import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty


class MyGrid(Widget):
	word = ObjectProperty(None)

	def play_sound(self):
		output = gTTS(text=self.word.text, lang='id', slow=False)
		output.save("output.mp3")
		sound = SoundLoader.load('output.mp3')

		if sound:
			sound.play()

class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == '__main__':
	MyApp().run()
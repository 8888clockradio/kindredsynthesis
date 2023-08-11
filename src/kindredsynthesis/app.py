"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


from elevenlabs import clone, generate, play


class KindredSynthesis(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
        voice = clone(
            name="Alex",
            description="An old American male voice with a slight hoarseness in his throat. Perfect for news", # Optional
            files=["./sample_0.mp3", "./sample_1.mp3", "./sample_2.mp3"],
        )

        audio = generate(text="Hi! I'm a cloned voice!", voice=voice)

        play(audio)


def main():
    return KindredSynthesis()

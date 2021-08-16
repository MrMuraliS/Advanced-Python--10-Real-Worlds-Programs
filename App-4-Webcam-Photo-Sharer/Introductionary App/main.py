import wget
import wikipedia
import requests
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get User query
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        # Download the image
        # wget.download(image_link, './images/image.jpg')

        req = requests.get(image_link)
        img_path = 'images/image.jpg'

        with open(img_path, 'wb') as file:
            file.write(req.content)

        self.manager.current_screen.ids.img.source = './images/image.jpg'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()

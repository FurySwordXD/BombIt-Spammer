from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from spammer import Spammer


class SpammerGridLayout(GridLayout):

    def bomb(self, mobile, delay, count):
        if mobile and delay and count:
            try:
                print("Mobile: " + mobile + "\nDelay: " + delay + "\nSpam count: " + count)
                Spammer(mobile, delay, count).spam()
            except Exception as e:
                print(str(e))


class SimpleKivy(App):

    def build(self):
        return SpammerGridLayout()


if __name__ == "__main__":
    SimpleKivy().run()


#delay = input('Enter the delay: ')
#mobile = input('Enter the mobile number: ')
#count = input('Enter the number of blasts: ')
#Spammer(mobile, count, delay).spam()

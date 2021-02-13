from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
from kivy.lang import Builder
from src.home import HomePage
from kivymd.theming import ThemeManager
from kivymd.uix.picker import MDThemePicker, MDTimePicker

########   Variables   ########
#theme_clr = 'Blue'
page = HomePage
#theme_cls = ThemeManager()

class WalletApp(MDApp):
    
    def build(self):
        #self.theme_cls.primary_palette = theme_clr
        screen = Builder.load_string(HomePage)
        #self.load_kv("main.kv")
        return screen
    
    def navigateDrawer(self):
        print("Navigates Here")
        
    def showHomePage(self):
        print("Navigates Here")
        
    def showAnalyticsPage(self):
        print("Navigates Here")
        
    def showWallet(self):
        print("Navigates Here")
        
    def showProfile(self):
        print("Navigates Here")
        
    def setThemeColor(self, x_cr):
        theme_clr = x_cr
        
    def setPage(self, page_String):
        page = page_String
        
    def changeTheme(self):
        theme_Window2 = MDThemePicker()
        theme_Window2.open()
        
    def show_time_picker(self):
        time_Window = MDTimePicker()
        time_Window.open()
        
WalletApp().run()
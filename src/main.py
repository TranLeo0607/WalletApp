from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
from kivy.lang import Builder

HomePage = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            left_action_items: [["menu", lambda x: app.nagivateDrawer()]]
            right_action_items: [["calendar", lambda x: app.navigateDrawer()]]
            
            
        MDBottomAppBar:
            MDToolbar:
                type: "bottom"
                left_action_items: [["menu", lambda x: app.nagivateDrawer()]]
                right_action_items: [["calendar", lambda x: app.navigateDrawer()]]
                mode: "free-end"
                icon: "palette-outline"
        MDLabel:
            text: 'Welcome'
            halign: 'center'
        
"""

class WalletApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        screen = Builder.load_string(HomePage)
        return screen
    
    def navigateDrawer(self):
        print("Navigates Here")
        
WalletApp().run()
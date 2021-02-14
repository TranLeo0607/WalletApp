HomePage = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Home"
        MDBottomAppBar:
            MDToolbar:
                type: "bottom"
                left_action_items: [["chart-bar", lambda x: app.showAnalyticsPage()], ["wallet", lambda x: app.showWallet()]]
                right_action_items: [["account", lambda x: app.showProfile()], ["palette", lambda x: app.changeTheme()]] 
                icon: "home"
                on_action_button: app.showHomePage()
                
        MDLabel:
            text: 'Welcome'
            halign: 'center'
        
'''
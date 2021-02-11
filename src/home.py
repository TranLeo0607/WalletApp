HomePage = '''
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
                on_action_button: app.changeTheme()
                
        MDRaisedButton:
            text: "Open time picker"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_time_picker()
            
        MDRaisedButton:
            text: "Open theme"
            pos_hint: {'center_x': .8, 'center_y': .8}
            on_release: app.changeTheme()
        
        MDLabel:
            text: 'Welcome'
            halign: 'center'
        
'''
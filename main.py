from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRaisedButton
from kivy.properties import ColorProperty

nominal_colors = [[0, 0, 0, 1],  # black
                  [0.3, 0.3, 0, 1],  # brown
                  [1, 0, 0, 1],  # red
                  [1, 0.7, 0, 1],  # orange
                  [1, 1, 0, 1],  # yellow
                  [0, 1, 0, 1],  # green
                  [0, 0.8, 1, 1],  # blue
                  [1, 0.3, 1, 1],  # purple
                  [0.1, 0.1, 0.2, 1],  # grey
                  [1, 1, 1, 1],  # white
                  ]


class MainApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(MDRectangleFlatButton(text='placeholder'))
        grid = MDGridLayout(cols=5, rows=15)

        # button.bind(on_press=self.on_press_button)
        for rown in range(10):
            for coln in range(5):
                btn = MDRaisedButton(text=str(rown),
                                     size_hint=(0.5, 0.1),
                                     pos_hint={'center_x': .5, 'center_y': .5},
                                     md_bg_color=nominal_colors[rown],
                                     )
                grid.add_widget(btn)
        layout.add_widget(grid)
        return layout

    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')


if __name__ == '__main__':
    app = MainApp()
    app.run()

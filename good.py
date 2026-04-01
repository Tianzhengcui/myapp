from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


Window.size = (960, 540)


class Player(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x_pos = 400
        self.y_pos = 220
        self.size_px = 60
        self.color_state = (0, 1, 0)

        with self.canvas:
            self.color = Color(*self.color_state)
            self.rect = Rectangle(pos=(self.x_pos, self.y_pos), size=(self.size_px, self.size_px))

        Clock.schedule_interval(self.update_graphics, 1 / 30.0)

    def update_graphics(self, dt):
        self.rect.pos = (self.x_pos, self.y_pos)

    def move(self, dx, dy):
        self.x_pos += dx
        self.y_pos += dy

    def action_a(self):
        self.color.rgb = (1, 0, 0)

    def action_b(self):
        self.color.rgb = (0, 0, 1)

    def reset_color(self):
        self.color.rgb = (0, 1, 0)


class GameRoot(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.player = Player()
        self.add_widget(self.player)

        self.info = Label(
            text="Simple Kivy Game",
            size_hint=(1, 0.1),
            pos_hint={"center_x": 0.5, "top": 1},
            font_size="24sp",
        )
        self.add_widget(self.info)

        # 左边方向键
        btn_left = Button(text="LEFT", size_hint=(0.14, 0.12), pos_hint={"x": 0.03, "y": 0.08})
        btn_right = Button(text="RIGHT", size_hint=(0.14, 0.12), pos_hint={"x": 0.19, "y": 0.08})
        btn_up = Button(text="UP", size_hint=(0.14, 0.12), pos_hint={"x": 0.11, "y": 0.22})
        btn_down = Button(text="DOWN", size_hint=(0.14, 0.12), pos_hint={"x": 0.11, "y": 0.00})

        btn_left.bind(on_press=lambda x: self.move_player(-20, 0, "LEFT"))
        btn_right.bind(on_press=lambda x: self.move_player(20, 0, "RIGHT"))
        btn_up.bind(on_press=lambda x: self.move_player(0, 20, "UP"))
        btn_down.bind(on_press=lambda x: self.move_player(0, -20, "DOWN"))

        self.add_widget(btn_left)
        self.add_widget(btn_right)
        self.add_widget(btn_up)
        self.add_widget(btn_down)

        # 右边 A/B 键
        btn_a = Button(text="A", size_hint=(0.14, 0.14), pos_hint={"right": 0.95, "y": 0.14})
        btn_b = Button(text="B", size_hint=(0.14, 0.14), pos_hint={"right": 0.78, "y": 0.04})

        btn_a.bind(on_press=lambda x: self.press_a())
        btn_a.bind(on_release=lambda x: self.release_action())
        btn_b.bind(on_press=lambda x: self.press_b())
        btn_b.bind(on_release=lambda x: self.release_action())

        self.add_widget(btn_a)
        self.add_widget(btn_b)

    def move_player(self, dx, dy, name):
        self.player.move(dx, dy)
        self.info.text = f"Pressed {name}"

    def press_a(self):
        self.player.action_a()
        self.info.text = "Pressed A"

    def press_b(self):
        self.player.action_b()
        self.info.text = "Pressed B"

    def release_action(self):
        self.player.reset_color()
        self.info.text = "Ready"


class MyApp(App):
    def build(self):
        return GameRoot()


if __name__ == "__main__":
    MyApp().run()
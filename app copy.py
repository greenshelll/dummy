from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

KV = '''
<Main>:
    orientation: "vertical"

    MDRaisedButton:
        text: 'Click'
        on_press: root.callit()

    MDLabel:
        id: age_lab
        size_hint_y: 0.1
        text: root.str_age

<OpenDialog>:
    title: 'InputDialog'
    size_hint: None, None
    size: 400, 120
    auto_dismiss: False

    BoxLayout:
        orientation: 'vertical'
        pos: self.pos
        size: root.size

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Enter Value'

            MDTextField:
                id: input
                multiline: False
                hint_text: 'Age'
                input_filter: 'int'

        BoxLayout:
            orientation: 'horizontal'
            MDRaisedButton:
                text: 'Enter'
                on_press: root._enter()

            MDRaisedButton:
                text: 'Cancel'
                on_press: root._cancel()

        Label:
            id: er
            size_hint_y: None
            height: 0
            text: root.error
'''


class Main(BoxLayout):
    age = NumericProperty()
    str_age = StringProperty("None")

    def callit(self):
        obj = OpenDialog()
        obj.bind(_age=self.setter('age'))
        obj.open()

    def on_age(self, *args):
        self.str_age = "Age: {}".format(self.age)


class OpenDialog(Popup):
    _age = NumericProperty()
    error = StringProperty()

    def on_error(self, inst, text):
        if text:
            self.ids.er.height = 30
            self.height = 150
        else:
            self.ids.er.height = 0
            self.height = 120

    def _enter(self):
        if not self.ids.input.text:
            self.error = "Error: enter age"
        else:
            self._age = int(self.ids.input.text)
            self.dismiss()

    def _cancel(self):
        self.dismiss()


class SriPop(MDApp):
    def build(self):
        return Main()


if __name__ == '__main__':
    SriPop().run()

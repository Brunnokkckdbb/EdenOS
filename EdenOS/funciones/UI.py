# UI.py
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from datetime import datetime

kivy.require('2.0.0')

class PantallaCompletaApp(App):
    def build(self):
        #Window.fullscreen = True

        self.layout = FloatLayout()

        botones_info = [
            {'text': 'Izquierda Centro', 'pos_hint': {'x': 0.05, 'y': 0.43}},
            {'text': 'Izquierda 3/4',    'pos_hint': {'x': 0.05, 'y': 0.13}},
            {'text': 'Izquierda arriba', 'pos_hint': {'x': 0.05, 'y': 0.75}},
            {'text': 'Centro Centro',    'pos_hint': {'x': 0.4,  'y': 0.30}},
            {'text': 'Derecha Centro',   'pos_hint': {'x': 0.75, 'y': 0.43}},
            {'text': 'Derecha 3/4',      'pos_hint': {'x': 0.75, 'y': 0.13}},
        ]

        # Crear y añadir los botones
        for info in botones_info:
            boton = Button(
                text=info['text'],
                size_hint=(0.2, 0.1),
                pos_hint=info['pos_hint'],
                font_size=22
            )
            boton.bind(on_press=self.accion_boton)
            self.layout.add_widget(boton)

        # Crear el "botón-reloj"
        self.boton_reloj = Button(
            text=self.obtener_hora(),
            size_hint=(0.2, 0.1),
            pos_hint={'x': 0.75, 'y': 0.75},
            font_size=28,
            background_color=(0.2, 0.2, 0.2, 1),  # Un gris oscuro
            color=(1, 1, 1, 1)  # Texto blanco
        )
        self.boton_reloj.bind(on_press=self.accion_reloj)
        self.layout.add_widget(self.boton_reloj)

        # Actualizar el texto del reloj cada segundo
        Clock.schedule_interval(self.actualizar_reloj, 1)

        return self.layout

    def obtener_hora(self):
        return datetime.now().strftime('%H:%M:%S')

    def actualizar_reloj(self, dt):
        self.boton_reloj.text = self.obtener_hora()

    def accion_boton(self, instance):
        print(f'¡{instance.text} presionado!')

    def accion_reloj(self, instance):
        print("¡Reloj presionado! Puedes hacer algo aquí si quieres.")

if __name__ == '__main__':
    PantallaCompletaApp().run()

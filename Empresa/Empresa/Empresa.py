"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import copy
from .results import results
from typing import Any
from typing import List

question_style = {
    "bg": "white",
    "padding": "2em",
    "border_radius": "25px",
    "w": "100%",
    "align_items": "left",
}


class State(rx.State):
    """The app state."""

    default_answers = [None, None, [False, False, False, False, False]]
    answers: List[Any]
    answer_key = ["Misionero", "[b y c]", [False,False,True,True,True]]
    score: int

    def onload(self):
        self.answers = copy.deepcopy(self.default_answers)

    def set_answers(self, answer, index, sub_index=None):
        if sub_index is None:
            self.answers[index] = answer
        else:
            self.answers[index][sub_index] = answer

    def submit(self):
        total, correct = 0, 0
        for i in range(len(self.answers)):
            if self.answers[i] == self.answer_key[i]:
                correct += 1
            total += 1
        self.score = int(correct / total * 100)
        return rx.redirect("/result")

    @rx.var
    def percent_score(self):
        return f"{self.score}%"


def header():
    return rx.chakra.vstack(
        rx.chakra.heading("CUANTAS POSIBILIDADES TENES CON LA MAMA DEL MATI"),
        rx.chakra.divider(),
        rx.chakra.text("Aca se determinar las probabilidades que tienes para salir este 14 de febrero con la mamá del Mati."),
        rx.chakra.text("Por favor tomarlo con precaución."),
        style=question_style,
    )


def question1():
    """The main view."""
    return rx.chakra.vstack(
        rx.chakra.heading("Pregunta #1"),
        rx.chakra.text(
            "¿Cual es la pose favorita de la Mamá de Mati?"
        ),
        rx.chakra.divider(),
        rx.chakra.radio_group(
            ["69", "Misionero"],
            default_value=State.default_answers[0],
            default_checked=True,
            on_change=lambda answer: State.set_answers(answer, 0),
        ),
        style=question_style,
    )


def question2():
    return rx.chakra.vstack(
        rx.chakra.heading("Pregunta #2"),
        rx.chakra.text("¿Como se le dice a la Mamá de Reichichotas y Nico El enano petero?"),
        rx.chakra.code_block(
            """a = Sumisa
b = Puta de mierda
c = Contenedor de semen
""",
            language="python",
        ),
        rx.chakra.radio_group(
            ["[b y c]", "[Todas las anteriores]"],
            default_value=State.default_answers[1],
            default_check=True,
            on_change=lambda answer: State.set_answers(answer, 1),
        ),
        style=question_style,
    )


def question3():
    return rx.chakra.vstack(
        rx.chakra.heading("Pregunta #3"),
        rx.chakra.text(
            "Marca las maneras que llamamos a la mamá de Franco ",
            rx.chakra.code("Sabiendo"),
            " Su pasado y presente:",
        ),
        rx.chakra.vstack(
            rx.chakra.checkbox(
                rx.chakra.code("Promiscua"),
                on_change=lambda answer: State.set_answers(answer, 2, 0),
            ),
            rx.chakra.checkbox(
                rx.chakra.code("Puto el que lee"),
                on_change=lambda answer: State.set_answers(answer, 2, 1),
            ),
            rx.chakra.checkbox(
                rx.chakra.code("Merca viviente"),
                on_change=lambda answer: State.set_answers(answer, 2, 2),
            ),
            rx.chakra.checkbox(
                rx.chakra.code("Sali de aca yegua inmunda me gusta tu hermana ahora, CARLITOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS"),
                on_change=lambda answer: State.set_answers(answer, 2, 3),
            ),
            rx.chakra.checkbox(
                rx.chakra.code("Tu madre tiene una pollaaaa"),
                on_change=lambda answer: State.set_answers(answer, 2, 4),
            ),
            align_items="left",
        ),
        style=question_style,
    )


def index():
    """The main view."""
    return rx.chakra.center(
        rx.chakra.vstack(
            header(),
            question1(),
            question2(),
            question3(),
            rx.chakra.button(
                "¡¡Que tocas!!",
                bg="black",
                color="white",
                width="6em",
                padding="1em",
                on_click=State.submit,
            ),
            spacing="1em",
        ),
        padding_y="2em",
        height="100vh",
        align_items="top",
        bg="#ededed",
        overflow="auto",
    )


def result():
    return results(State)


app = rx.App()
app.add_page(index, title="Mama del mati", on_load=State.onload)
app.add_page(result, title="Quiz Results")
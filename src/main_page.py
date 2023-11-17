from functools import partial

import justpy as jp

from gui import Gui, Mode

LEFT_MARGIN, RIGHT_MARGIN = " margin-left: 10px; ", " margin-right: 20px; "

TITLE_DIV_CLASS = "grid justify-between gap-2 grid-cols-3"
TITLE_DIV_STYLE = "grid-template-columns: auto auto auto; margin-top: 15px;" + LEFT_MARGIN + RIGHT_MARGIN

TITLE_TEXT_DIV_STYLE = "font-size: 80px; text-align: center; text-weight: bold;"

DESCRIPTION_STYLE = "margin-top: 15px; font-size: 20px;" + LEFT_MARGIN + RIGHT_MARGIN
DESCRIPTION_TEXT = """
Travelling demo: this demo allows you to create and navigate a map.
Some text to the left of the buttons take a single number (like Add Locations, Remove Locations, Set Start and Set Destination).
The other texts take 2 numbers separated by a comma.
Their usage should be pretty trivial.
You can also press randomize to get a random graph with the given number of location and the given number of edges
"""
SINGLE_DESCRIPTION_STYLE = LEFT_MARGIN + RIGHT_MARGIN


MAIN_BODY_DIV_CLASS = "grid justify-between grid-cols-3 gap-7"
# MAIN_BODY_DIV_STYLE = "grid-template-columns: minmax(max-content, 25%) minmax(max-content, 25%) 10px minmax(max-content, 33%); width: 100vw; margin-top: 15px;" + LEFT_MARGIN + RIGHT_MARGIN
MAIN_BODY_DIV_STYLE = "grid-template-columns: max-content minmax(0, 33%) auto; column-gap: 15px; margin-top: 15px;" + LEFT_MARGIN + RIGHT_MARGIN

ACTIONS_DIV_CLASS = "grid"
# Setting height to 0 it'sa trick to solve the problem of the goal div changing size
ACTIONS_DIV_STYLE = f"grid-template-columns: auto auto; font-size: 30px; font-weight: semibold; height: 0px;"

SINGLE_ACTION_P_CLASS = ""
SINGLE_ACTION_P_STYLE = "font-weight: normal; font-size: 20px; margin-top: 15px;"

ADD_BUTTON_CLASS = "bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2"
ADD_BUTTON_STYLE = "font-weight: semibold; font-size: 20px; width: 250px;"

GOALS_DIV_CLASS = ""
GOALS_DIV_STYLE = "font-size: 30px; font-weight: semibold;"


GOALS_CONTAINER_DIV_CLASS = ""
GOALS_CONTAINER_DIV_STYLE = ""

CLEAR_SOLVE_BUTTONS_DIV_CLASS = "flex grid-cols-2"
CLEAR_SOLVE_BUTTONS_DIV_STYLE = ""

CLEAR_SOLVE_BUTTONS_CLASS = ADD_BUTTON_CLASS
CLEAR_SOLVE_BUTTONS_STYLE = "font-weight: semibold; font-size: 20px;"

PLAN_DIV_CLASS = ""
PLAN_DIV_STYLE = f"font-size: 30px; font-weight: semibold;"

PLAN_PART_P_CLASS = ""
PLAN_PART_P_STYLE = f"font-weight: normal; font-size: 20px;"

CLEAR_PLAN_BUTTON_CLASS = ADD_BUTTON_CLASS
CLEAR_PLAN_BUTTON_STYLE = "font-weight: semibold; font-size: 20px;"


def main_page(gui: Gui):
    wp = jp.WebPage(delete_flag = False)
    wp.page_type = 'main'
    title_div = jp.Div(
        a=wp,
        classes=TITLE_DIV_CLASS,
        style=TITLE_DIV_STYLE,
    )
    fbk_logo_div = jp.Div(
        a=title_div,
        # text="FBK LOGO",
        # style="font-size: 30px;",
        style="height: 160px;",
    )
    fbk_logo = jp.Img(
        src="/static/logos/fbk.png",
        a=fbk_logo_div,
        classes="w3-image",
        # style="height: 100%; length: auto;",
    )
    title_text_div = jp.Div(
        a=title_div,
        text="TSB-SPACE",
        style=TITLE_TEXT_DIV_STYLE,
    )
    trasys_logo_div = jp.Div(
        a=title_div,
        # text="TRASYS LOGO",
        style="height: 160px;",
    )
    trasys = jp.Img(
        src="/static/logos/trasys.png",
        a=trasys_logo_div,
        classes="w3-image",
        # style="height: 10px; length: 10px;"
    )

    description_div = jp.Div(
        a=wp,
        style=DESCRIPTION_STYLE,
    )
    for single_desc in DESCRIPTION_TEXT.split("\n"):
        description_paragraph = jp.P(
            a=description_div,
            style=SINGLE_DESCRIPTION_STYLE,
            text=single_desc,
        )

    main_body_div = jp.Div(
        a=wp,
        classes=MAIN_BODY_DIV_CLASS,
        style=MAIN_BODY_DIV_STYLE,
    )

    actions_div = jp.Div(
        a=main_body_div,
        text="ACTIONS:",
        classes=ACTIONS_DIV_CLASS,
        style=ACTIONS_DIV_STYLE,
    )

    # Useless paragprah, added just as a place-holder
    _ = jp.P(
        a=actions_div,
        text="",
    )

    # Add Locations
    ADD_LOCATIONS_TEXT_PLACEHOLDER = "_"
    add_locations_text = jp.Input(
        a=actions_div,
        placeholder= ADD_LOCATIONS_TEXT_PLACEHOLDER,
        classes=SINGLE_ACTION_P_CLASS,
        style=SINGLE_ACTION_P_STYLE,
    )
    add_locations_button = jp.Input(
        a=actions_div,
        value="Add Locations",
        type="submit",
        classes=ADD_BUTTON_CLASS,
        style=ADD_BUTTON_STYLE,
    )
    def add_locations_button_click(add_locations_text: jp.Input, gui: Gui, component, msg):
        text = add_locations_text.value
        gui.logger.info("Clicked add_locations: " + text + f"with mode: {gui.mode}")
        try:
            value = int(text)
            if value > 0:
                add_locations_text.value = ADD_LOCATIONS_TEXT_PLACEHOLDER
                if gui.mode == Mode.GENERATING_PROBLEM:
                    gui.add_locations_to_graph(value)
            else:
                add_locations_text.value = "Error: insert a number > 0"
        except ValueError:
            add_locations_text.value = "Error: not a number"
    add_locations_button.on('click', partial(add_locations_button_click, add_locations_text, gui))

    # Remove Locations
    REMOVE_LOCATIONS_TEXT_PLACEHOLDER = "_"
    remove_locations_text = jp.Input(
        a=actions_div,
        placeholder= REMOVE_LOCATIONS_TEXT_PLACEHOLDER,
        classes=SINGLE_ACTION_P_CLASS,
        style=SINGLE_ACTION_P_STYLE,
    )
    remove_locations_button = jp.Input(
        a=actions_div,
        value="Remove Locations",
        type="submit",
        classes=ADD_BUTTON_CLASS,
        style=ADD_BUTTON_STYLE,
    )
    def remove_locations_button_click(remove_locations_text: jp.Input, gui: Gui, component, msg):
        text = remove_locations_text.value
        gui.logger.info("Clicked remove_locations: " + text + f"with mode: {gui.mode}")
        try:
            graph = gui.graph
            defined_locations = len(graph)
            value = int(text)
            if value > 0:
                if value <= defined_locations:
                    remove_locations_text.value = REMOVE_LOCATIONS_TEXT_PLACEHOLDER
                    if gui.mode == Mode.GENERATING_PROBLEM:
                        gui.remove_locations_from_graph(value)
                else:
                    remove_locations_text.value = f"Error: insert number <= {defined_locations}"
            else:
                remove_locations_text.value = "Error: insert a number > 0"
        except ValueError:
            remove_locations_text.value = "Error: not a number"
    remove_locations_button.on('click', partial(remove_locations_button_click, remove_locations_text, gui))

    # Add Connection
    ADD_CONNECTION_TEXT_PLACEHOLDER = "_"
    add_connection_text = jp.Input(
        a=actions_div,
        placeholder= ADD_CONNECTION_TEXT_PLACEHOLDER,
        classes=SINGLE_ACTION_P_CLASS,
        style=SINGLE_ACTION_P_STYLE,
    )
    add_connection_button = jp.Input(
        a=actions_div,
        value="Add Connection",
        type="submit",
        classes=ADD_BUTTON_CLASS,
        style=ADD_BUTTON_STYLE,
    )
    def add_connection_button_click(add_connection_text: jp.Input, gui: Gui, component, msg):
        text = add_connection_text.value
        gui.logger.info("Clicked add_connection: " + text + f"with mode: {gui.mode}")
        try:
            graph = gui.graph
            defined_locations = len(graph)
            value_1, value_2 = map(int, text.split(",", maxsplit=1))
            if value_1 > 0:
                if value_1 > defined_locations:
                    add_connection_text.value = f"Error: first value > {defined_locations}"
                    return
            else:
                add_connection_text.value = "Error: first number < 0"
                return

            if value_1 > 0:
                if value_1 > defined_locations:
                    add_connection_text.value = f"Error: first value > {defined_locations}"
                    return
            else:
                add_connection_text.value = "Error: first value < 0"
                return

            if value_2 > 0:
                if value_2 > defined_locations:
                    add_connection_text.value = f"Error: second value > {defined_locations}"
                    return
            else:
                add_connection_text.value = "Error: second value < 0"
                return

            if gui.mode == Mode.GENERATING_PROBLEM:
                gui.graph.add_edge(f"L_{value_1}", f"L_{value_2}")
            gui.display_graph()
            add_connection_text.value = ADD_CONNECTION_TEXT_PLACEHOLDER

        except ValueError:
            add_connection_text.value = "Error: specify 2 comma separated numbers"
    add_connection_button.on('click', partial(add_connection_button_click, add_connection_text, gui))

    # Remove Connection
    REMOVE_CONNECTION_TEXT_PLACEHOLDER = "_"
    remove_connection_text = jp.Input(
        a=actions_div,
        placeholder= REMOVE_CONNECTION_TEXT_PLACEHOLDER,
        classes=SINGLE_ACTION_P_CLASS,
        style=SINGLE_ACTION_P_STYLE,
    )
    remove_connection_button = jp.Input(
        a=actions_div,
        value="Remove Connection",
        type="submit",
        classes=ADD_BUTTON_CLASS,
        style=ADD_BUTTON_STYLE,
    )
    def remove_connection_button_click(remove_connection_text: jp.Input, gui: Gui, component, msg):
        text = remove_connection_text.value
        gui.logger.info("Clicked remove_connection: " + text + f"with mode: {gui.mode}")
        try:
            graph = gui.graph
            defined_locations = len(graph)
            value_1, value_2 = map(int, text.split(",", maxsplit=1))
            if value_1 > 0:
                if value_1 > defined_locations:
                    remove_connection_text.value = f"Error: first value > {defined_locations}"
                    return
            else:
                remove_connection_text.value = "Error: first number < 0"
                return

            if value_1 > 0:
                if value_1 > defined_locations:
                    remove_connection_text.value = f"Error: first value > {defined_locations}"
                    return
            else:
                remove_connection_text.value = "Error: first value < 0"
                return

            if value_2 > 0:
                if value_2 > defined_locations:
                    remove_connection_text.value = f"Error: second value > {defined_locations}"
                    return
            else:
                remove_connection_text.value = "Error: second value < 0"
                return
            try:
                if gui.mode == Mode.GENERATING_PROBLEM:
                    gui.graph.remove_edge(f"L_{value_1}", f"L_{value_2}")
            except Exception as e:
                pass

            gui.display_graph()
            remove_connection_text.value = REMOVE_CONNECTION_TEXT_PLACEHOLDER

        except ValueError:
            remove_connection_text.value = "Error: specify 2 comma separated numbers"
    remove_connection_button.on('click', partial(remove_connection_button_click, remove_connection_text, gui))


    # Set Start
    SET_START_TEXT_PLACEHOLDER = "_"
    set_start_text = jp.Input(
        a=actions_div,
        placeholder=SET_START_TEXT_PLACEHOLDER,
        classes=SINGLE_ACTION_P_CLASS,
        style=SINGLE_ACTION_P_STYLE,
    )
    set_start_button = jp.Input(
        a=actions_div,
        value="Set Start",
        type="submit",
        classes=ADD_BUTTON_CLASS,
        style=ADD_BUTTON_STYLE,
    )

    def set_start_button_click(set_start_text: jp.Input, gui: Gui, component, msg):
        text = set_start_text.value
        gui.logger.info("Clicked set_start: " + text + f" with mode: {gui.mode}")
        try:
            graph = gui.graph
            defined_locations = len(graph)
            value = int(text)
            if value > 0:
                if value <= defined_locations:
                    set_start_text.value = SET_START_TEXT_PLACEHOLDER
                    if gui.mode == Mode.GENERATING_PROBLEM:
                        gui.start = f"L_{value}"
                        gui.display_graph()
                else:
                    set_start_text.value = f"Error: insert number <= {defined_locations}"
            else:
                set_start_text.value = "Error: insert a number > 0"
        except ValueError:
            set_start_text.value = "Error: not a number"

    set_start_button.on('click', partial(set_start_button_click, set_start_text, gui))

    # Set Destination
    SET_DESTINATION_TEXT_PLACEHOLDER = "_"
    set_destination_text = jp.Input(
        a=actions_div,
        placeholder=SET_DESTINATION_TEXT_PLACEHOLDER,
        classes=SINGLE_ACTION_P_CLASS,
        style=SINGLE_ACTION_P_STYLE,
    )
    set_destination_button = jp.Input(
        a=actions_div,
        value="Set Destination",
        type="submit",
        classes=ADD_BUTTON_CLASS,
        style=ADD_BUTTON_STYLE,
    )

    def set_destination_button_click(set_destination_text: jp.Input, gui: Gui, component, msg):
        text = set_destination_text.value
        gui.logger.info("Clicked set_destination: " + text + f" with mode: {gui.mode}")
        try:
            graph = gui.graph
            defined_locations = len(graph)
            value = int(text)
            if value > 0:
                if value <= defined_locations:
                    set_destination_text.value = SET_DESTINATION_TEXT_PLACEHOLDER
                    if gui.mode == Mode.GENERATING_PROBLEM:
                        gui.destination = f"L_{value}"
                        gui.display_graph()
                else:
                    set_destination_text.value = f"Error: insert number <= {defined_locations}"
            else:
                set_destination_text.value = "Error: insert a number > 0"
        except ValueError:
            set_destination_text.value = "Error: not a number"

    set_destination_button.on('click', partial(set_destination_button_click, set_destination_text, gui))

    # Randomize Graph
    RANDOMIZE_TEXT_PLACEHOLDER = "_"
    randomize_text = jp.Input(
        a=actions_div,
        placeholder= RANDOMIZE_TEXT_PLACEHOLDER,
        classes=SINGLE_ACTION_P_CLASS,
        style=SINGLE_ACTION_P_STYLE,
    )
    randomize_button = jp.Input(
        a=actions_div,
        value="Randomize Graph",
        type="submit",
        classes=ADD_BUTTON_CLASS,
        style=ADD_BUTTON_STYLE,
    )
    def randomize_button_click(randomize_text: jp.Input, gui: Gui, component, msg):
        text = randomize_text.value
        gui.logger.info("Clicked randomize: " + text + f"with mode: {gui.mode}")
        try:
            graph = gui.graph
            defined_locations = len(graph)
            value_1, value_2 = map(int, text.split(",", maxsplit=1))
            if value_1 <= 0:
                randomize_text.value = "Error: first number <= 0"
                return

            if value_2 <= 0:
                randomize_text.value = "Error: second value <= 0"
                return
            try:
                if gui.mode == Mode.GENERATING_PROBLEM:
                    gui.randomize_graph_click(value_1, value_2)
            except Exception as e:
                pass

            gui.display_graph()
            randomize_text.value = RANDOMIZE_TEXT_PLACEHOLDER

        except ValueError:
            randomize_text.value = "Error: specify 2 comma separated numbers"
    randomize_button.on('click', partial(randomize_button_click, randomize_text, gui))

    goals_div = jp.Div(
        a=main_body_div,
        text="GOALS:",
        classes=GOALS_DIV_CLASS,
        style=GOALS_DIV_STYLE,
    )

    graph_image_div = jp.Div(
        a=goals_div,
        classes="",
        style="",
    )
    gui.graph_image_div = graph_image_div

    gui.display_graph()

    clear_solve_buttons_div = jp.Div(
        a=goals_div,
        classes=CLEAR_SOLVE_BUTTONS_DIV_CLASS,
        style=CLEAR_SOLVE_BUTTONS_DIV_STYLE,
    )

    clear = jp.Input(
        a=clear_solve_buttons_div,
        value="CLEAR",
        type="submit",
        classes=CLEAR_SOLVE_BUTTONS_CLASS,
        style=CLEAR_SOLVE_BUTTONS_STYLE,
    )
    clear.on('click', gui.clear_activities_click)
    solve = jp.Input(
        a=clear_solve_buttons_div,
        value="SOLVE",
        type="submit",
        classes=CLEAR_SOLVE_BUTTONS_CLASS,
        style=CLEAR_SOLVE_BUTTONS_STYLE,
    )
    solve.on('click', gui.generate_problem_click)

    plan_div = jp.Div(
        a=main_body_div,
        text="PLAN:",
        classes=PLAN_DIV_CLASS,
        style=PLAN_DIV_STYLE,
    )
    gui.plan_div = plan_div

    gui.update_planning_execution()

    # if gui.plan is None:
    #     single_p = jp.P(
    #         a=plan_div,
    #         text="No plan found yet.",
    #         classes=PLAN_PART_P_CLASS,
    #         style=PLAN_PART_P_STYLE,
    #     )
    # else:
    #     for plan_activity in gui.plan:
    #         text = activity_str(plan_activity)
    #         single_p = jp.P(
    #             a=plan_div,
    #             text=text,
    #             classes=PLAN_PART_P_CLASS,
    #             style=PLAN_PART_P_STYLE,
    #         )
    #     single_p = jp.P(
    #         a=plan_div,
    #         text=f"It reaches {gui.reached_goals} goals.",
    #         classes=PLAN_PART_P_CLASS,
    #         style=PLAN_PART_P_STYLE,
    #     )

    return wp
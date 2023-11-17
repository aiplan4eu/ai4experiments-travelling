
import asyncio
import networkx as nx
import matplotlib.pyplot as plt
from enum import Enum, auto
from networkx import Graph, dense_gnm_random_graph
from random import randint

import random
import logging
import os
import queue
import justpy as jp
# FOR FUTURE PROJECTS: check out the justpy.react functionality: https://justpy.io/blog/reactivity/


import unified_planning as up
from unified_planning.shortcuts import *


DEBUG = False
N_STARTING_LOCATIONS = 4
BUTTON_CLASS = 'bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2'
# BUTTON_CLASS = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
ACTIVITY_DIV_STYLE = "color:blue;"
PLAN_DIV_STYLE = "color:blue;"

GRAPH_IMAGE_LOCATION = "/logos/generated/graph"
GRAPH_IMAGE_DIMENSIONS = "height: 200px; length: 200px;"

FIGSIZE = 6, 6


DIV_CLASS = "margin: auto; width: 50%;"
class Mode(Enum):
    GENERATING_PROBLEM = auto()
    OPERATING = auto()


curr_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(curr_dir, 'models')

class Gui():
    def __init__(self):
        # a queue where the interface waits the start
        self.start_queue = queue.Queue()

        self.mode = Mode.GENERATING_PROBLEM
        self.graph = Graph()

        self.plan = None
        self.plan_expected: bool = False

        self.plan_div: Optional[jp.Div] = None
        self.graph_image_div: Optional[jp.Img] = None

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s %(message)s')
        self.logger.setLevel(logging.INFO)
        self.total_planning_goals = -1
        self.reached_planning_goals = -1

        assert N_STARTING_LOCATIONS > 1
        self.add_locations_to_graph(N_STARTING_LOCATIONS, display_graph=False)

        self.start = "L_1"
        self.destination = f"L_{N_STARTING_LOCATIONS}"

    def add_locations_to_graph(self, number_of_locations: int, display_graph: bool = True):
        assert number_of_locations > 0
        defined_locations = len(self.graph)
        locations_to_add = [f"L_{i}" for i in range(defined_locations+1, defined_locations+number_of_locations+1)]
        self.graph.add_nodes_from(((l, {"label": l}) for l in locations_to_add))

        last_defined_location = f"L_{defined_locations}" if defined_locations > 0 else None
        if last_defined_location is not None:
            self.graph.add_edge(last_defined_location, locations_to_add[0])
        self.graph.add_edges_from(zip(locations_to_add[:-1], locations_to_add[1:]))
        self.display_graph()

    def remove_locations_from_graph(self, number_of_locations: int):
        defined_locations = len(self.graph)
        assert number_of_locations > 0 and number_of_locations <= defined_locations
        locations_to_remove = [f"L_{i}" for i in range(defined_locations-number_of_locations+1, defined_locations+1)]
        self.graph.remove_nodes_from(locations_to_remove)
        if self.start not in self.graph:
            self.start = f"L_{random.randint(1, len(self.graph))}"
        if self.destination not in self.graph:
            self.destination = f"L_{random.randint(1, len(self.graph))}"
        self.display_graph()

    def randomize_graph_click(self, n_nodes, n_edges):
        random_graph = dense_gnm_random_graph(n_nodes, n_edges)
        nodes = [f"L_{i}" for i in range(1, n_nodes+1)]
        node_mapping = dict(zip(random_graph, nodes))
        self.graph = Graph()
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from(map(lambda x: (node_mapping.get(x[0]), node_mapping.get(x[1])), random_graph.edges))
        self.start = f"L_{random.randint(1, len(self.graph))}"
        self.destination = f"L_{random.randint(1, len(self.graph))}"
        self.display_graph()

    def display_graph(self):
        if self.graph_image_div is None:
            return

        # from main_page import PLAN_PART_P_CLASS, PLAN_PART_P_STYLE
        # self.graph_image_div.delete_components()
        # texts = [f"Locations: {', '.join(self.graph.nodes)}."]
        # texts.append(f"Start: {self.start}.")
        # texts.append(f"Destination: {self.destination}.")
        # for node, nbrdict in self.graph.adjacency():
        #     texts.append(f"{node} connected to: {', '.join(map(str, nbrdict.keys()))}.")

        # for t in texts:
        #     _ = jp.P(
        #         a=self.graph_image_div,
        #         text=t,
        #         classes=PLAN_PART_P_CLASS,
        #         style=PLAN_PART_P_STYLE,
        #     )
        pos = nx.nx_agraph.graphviz_layout(self.graph, prog="twopi")
        fig = plt.figure(figsize = FIGSIZE)
        ax = fig.add_subplot()
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', ax=ax)
        image_id = randint(0, 2000)
        img_loc = f"{GRAPH_IMAGE_LOCATION}_{image_id}.png"
        # fig.savefig(f".{GRAPH_IMAGE_LOCATION}_{image_id}.png")
        fig.savefig(f".{img_loc}")

        self.graph_image_div.delete_components()

        _ = jp.Img(
            a=self.graph_image_div,
            src=f"static{img_loc}",
            style='max-width: 100%; height: auto;'
        )

        # try:
        #     asyncio.run(self.graph_image_div.update())
        # except RuntimeError:
        #     self.graph_image_div.update()

        # try:
        #     asyncio.run(reload_page)
        # except RuntimeError:
        #     reload_page()



        # try:
        #     asyncio.run(reload_page)
        # except:
        #     reload_page()

    def reset_execution(self):
        self.mode = Mode.GENERATING_PROBLEM

    def update_planning_execution(self):
        from main_page import PLAN_PART_P_CLASS, PLAN_PART_P_STYLE
        if self.plan_div is not None:
            self.plan_div.delete_components()
            if self.plan is not None:
                _ = jp.P(
                    a=self.plan_div,
                    text=f"Found a sequence of moves that connects {self.start} to {self.destination}!",
                    classes=PLAN_PART_P_CLASS,
                    style=PLAN_PART_P_STYLE,
                )
                for action_instance in self.plan.actions:
                    text = write_action_instance(action_instance)
                    _ = jp.P(
                        a=self.plan_div,
                        text=text,
                        classes=PLAN_PART_P_CLASS,
                        style=PLAN_PART_P_STYLE,
                    )
                _ = jp.P(
                    a=self.plan_div,
                    text=f"After this sequence you arrived at: {self.destination}!",
                    classes=PLAN_PART_P_CLASS,
                    style=PLAN_PART_P_STYLE,
                )
            elif self.plan_expected:
                if self.mode == Mode.GENERATING_PROBLEM:
                    single_p = jp.P(
                        a=self.plan_div,
                        text="No plan found; The start is not connected to the destination!",
                        classes=PLAN_PART_P_CLASS,
                        style=PLAN_PART_P_STYLE,
                    )
                else:
                    single_p = jp.P(
                        a=self.plan_div,
                        text="Wait for planning to finish!",
                        classes=PLAN_PART_P_CLASS,
                        style=PLAN_PART_P_STYLE,
                    )
            else:
                single_p = jp.P(
                    a=self.plan_div,
                    text="Modify graph and press SOLVE!",
                    classes=PLAN_PART_P_CLASS,
                    style=PLAN_PART_P_STYLE,
                )
            try:
                asyncio.run(self.plan_div.update())
            except RuntimeError:
                self.plan_div.update()

    def clear_activities_click(self, msg):

        self.logger.info("Clearing")
        if self.mode == Mode.GENERATING_PROBLEM:
            self.graph = Graph()
            assert N_STARTING_LOCATIONS > 1
            self.add_locations_to_graph(N_STARTING_LOCATIONS)

            self.start = "L_1"
            self.destination = f"L_{N_STARTING_LOCATIONS}"

            self.plan = None
            self.plan_expected = False
            self.display_graph()
            self.update_planning_execution()

    def show_gui_thread(self):
        from main_page import main_page
        @jp.SetRoute("/")
        def get_main_page():
            return main_page(self)
        jp.justpy(get_main_page)

    def generate_problem_click(self, msg):
        self.logger.info("Generating")
        if self.mode == Mode.GENERATING_PROBLEM:
            self.mode = Mode.OPERATING
            self.plan = None
            self.plan_expected = True
            self.update_planning_execution()
            # unlock the planing method with the problem correctly generated
            self.start_queue.put(None)


def write_action_instance(action_instance: up.plans.ActionInstance) -> str:
    return str(action_instance)

async def reload_page():
    for page in jp.WebPage.instances.values():
        if page.page_type == 'main':
            await page.reload()

import os
import requests
import asyncio
import logging
import xml.etree.ElementTree as ET
from typing import Tuple
from up_graphene_engine.engine import  GrapheneEngine
from gui import Gui

from unified_planning.shortcuts import *
import unified_planning as up
import unified_planning.engines
import unified_planning.model
import unified_planning.model.metrics

get_environment().credits_stream = None



def planning(engine: GrapheneEngine, gui: Gui, reload_page):
    logging.info("Generating planning problem...")

    # First, we declare a "Location" type
    Location = UserType('Location')

    # We create a new problem
    problem = Problem('robot')

    # Declare the fluents:
    # - `robot_at` is a predicate modeling the robot position,
    # - `connected` is a static fluent for modeling the graph connectivity relation
    robot_at = Fluent('robot_at', BoolType(), position=Location)
    connected = Fluent('connected', BoolType(), l_from=Location, l_to=Location)

    # Add the fluents to the problem, a Fluent can be resused in many problems
    # The default values are optional and can be any value (not forcing closed-world assumption)
    problem.add_fluent(robot_at, default_initial_value=False)
    problem.add_fluent(connected, default_initial_value=False)

    # Create a simple `move` action
    move = InstantaneousAction('move', l_from=Location, l_to=Location)
    l_from = move.parameter('l_from')
    l_to = move.parameter('l_to')
    move.add_precondition(robot_at(l_from))
    move.add_precondition(connected(l_from, l_to))
    move.add_effect(robot_at(l_from), False)
    move.add_effect(robot_at(l_to), True)
    problem.add_action(move)

    # Programmatically create a map from location name to a new `Object` of type `Location`
    locations = {str(l) : Object(str(l), Location) for l in gui.graph.nodes}

    # Add all the objects to the problem
    problem.add_objects(locations.values())

    # Setting the initial location
    problem.set_initial_value(robot_at(locations[gui.start]), True)

    # Initializing the connectivity relations by iterating over the graph edges
    for (f, t) in gui.graph.edges:
        problem.set_initial_value(connected(locations[str(f)], locations[str(t)]), True)
        problem.set_initial_value(connected(locations[str(t)], locations[str(f)]), True)

    # Setting the goal
    problem.add_goal(robot_at(locations[gui.destination]))

    # Printing the problem data structure in human-readable form
    # (We can also print in PDDL and ANML)
    #print(problem)


    logging.info("Planning...")

    res = engine.solve(problem)
    plan = res.plan

    return plan

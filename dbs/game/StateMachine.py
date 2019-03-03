from GameState import FINAL_GAME_STATE


class Node:
    """
    Class defining a graph node. It is used by the StateMachine class to represent
    the state graph.
    """

    def __init__(self, game_state):
        self._game_state = game_state
        self._successor_list = list()

    def add_successor(self, node, condition_func):
        """
        Add successor node.
        :param node: _Node succeding the current node in the graph.
        :param condition_func: Function returning true if the state machine should move
        to the next state. It should use the state_values from the GameState class.
        """
        self._successor_list.append((condition_func, node))

    def get_successor_list(self):
        """
        Returns a list of sets. The set is made up of a condition func in first position
        and a _Node in second position.
        """

        return self._successor_list

    def run(self):
        self._game_state.run()


FINAL_NODE = Node(FINAL_GAME_STATE)


class StateMachine:
    def __init__(self):
        self._active_node = None

    # Runs the active node. This function returns True if the state machine should keep on running (all its states haven't finished).
    # :return: True if the state machine should keep on running (all its states haven't finished). It returns False if all nodes have completed their execution.
    def run(self):
        # Check state transition
        for node_and_cond in self._active_node.get_successor_list():
            if node_and_cond[0]() is True:
                self._active_node = node_and_cond[1]
                break

        # Run game state
        self._active_node.run()

        # Returns True if the active node is not the FINAL_NODE (doesn't have the same name), False otherwise
        return False if self._active_node._game_state == FINAL_NODE._game_state else True

    def set_active_node(self, node: Node):
        self._active_node = node

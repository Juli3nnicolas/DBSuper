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


class StateMachine:
    def __init__(self):
        self._active_node = None

    def run(self):
        # Check state transition
        for node_and_cond in self._active_node.get_successor_list():
            if node_and_cond[0]() is True:
                self._active_node = node_and_cond[1]
                break

        # Run game state
        self._active_node.run()

    def set_active_node(self, node: Node):
        self._active_node = node

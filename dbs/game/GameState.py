class GameState:
    def __init__(self, name: str, state_values: dict, run_function):
        """
        Object's constructor.
        :name: game state's name. Names cannot start by two leading '_' and ending by two '_'. This syntax is for
        reserved system game states.
        :state_values: values exposed by the game state and used by the state machine to determine whether
        it should proceed to the next state
        :run_function: function called by run(). It is the state's main function and must change the state_values so
        that a transition to another state can be done. This function can be a closure but mustn't take any parameters.
        Ultimately, it must be idempotent as it will be called every frame.
        """
        self._name = name
        self._state_values = state_values
        self._run = run_function

    def __str__(self):
        return self._name

    def get_state_values(self):
        return self._state_values

    def run(self):
        """
        State's main function. It is executed every frame.
        """
        self._run()


FINAL_GAME_STATE = GameState(name="__FINAL_GAME_STATE__", state_values={}, run_function=lambda: True)

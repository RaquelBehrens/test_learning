### Run tests

To run coverage unit tests

`python3 -m unittest tests.data_flow_tests`

##

To check coverage of unit tests

`python3 -m pip install coverage`

`coverage run -m unittest tests.data_flow_tests`

`coverage report -m`

For a nicer presentation

`coverage html`

Report will be in `htmlcov/index`

##

To run mutmut (execute Mutation Tests)

`mutmut run --paths-to-mutate src/puzzle_game.py`

For a nicer presentation

`mutmut html`

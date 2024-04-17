### Run tests

To run coverage unit tests

`python3 -m unittest tests.command_and_branch_coverage_tests`

##

To check coverage of unit tests

`python3 -m pip install coverage`

`coverage run -m unittest tests.command_and_branch_coverage_tests`

`coverage report -m`

For a nicer presentation

`coverage html`

Report will be in `htmlcov/index`

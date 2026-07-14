printf "Running node related tests"
python3 -m unittest discover -s src/nodes/tests

printf "Running markdown_processor related tests"
python3 -m unittest discover -s src/markdown_processor/tests
# My Python Kata Scaffold

There are Kata Scaffolds for many programming languages out there.
I prefer to create my own Scaffold to my taste:

- run python directly via PyCharm / venv
- have program and script in a subdir named "kata"
- use a "testloop.sh" script to re-run all tests automatically
  after a file change (rather than using this functionality in the ide)

## Usage

### Shell:

installation:

    pip install pytest
    
run
    ./testloop.sh

in a separate window.

To activate the venv environment, source .venv/bin/activate:

   . .venv/bin/activate


(This sets the path to use the python libraries/links in .venv )


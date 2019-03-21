1. Install dependencies

- `pip install -r requirements.txt`

2. Ways to use program:
- insert data manually:
`python main.py`

- use file path argument:
`python main.py sample0.input`

- use pipeline:
`cat sample0.input | python main.py`

- use file descriptor:
`python main.py < sample0.input`

3. Run tests

- `python tests.py`
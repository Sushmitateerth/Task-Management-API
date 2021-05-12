boards = [
    {
        "title": "one",
        "description": "one description"
    },
    {
        "title": "two",
        "description": "two description"
    },
    {
        "title": "three",
        "description": "three description"
    },
    {
        "title": "four",
        "description": "four description"
    },
    {
        "title": "five",
        "description": "five description"
    },
    {
        "title": "six",
        "description": "six description"
    },
    {
        "title": "seven",
        "description": "seven description"
    },
    {
        "title": "eight",
        "description": "eight description"
    },
    {
        "title": "nine",
        "description": "nine description"
    },
    {
        "title": "ten",
        "description": "ten description"
    }
]

# sort boards by description
sort_by_description = sorted(boards, key=lambda board: board['description'])

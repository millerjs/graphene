import re


def to_camel_case(snake_str):
    # To maintain consistency with existing snake case
    return snake_str


# From this response in Stackoverflow
# http://stackoverflow.com/a/1176023/1072990
def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

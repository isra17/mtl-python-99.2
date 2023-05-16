#!/Users/israelhalle/.pyenv/versions/3.10.6/bin/python

def dot_product_coord_vec(a, b):
  return dot_product(parse_vec(a["vec"]), parse_vec(b["vec"]))

def parse_vec(data):
  return (data[1]["x"] - data[0]["x"], data[1]["y"] - data[0]["y"])

def dot_product(a, b):
  return sum([i * j for (i, j) in zip(a, b)])

print(dot_product_coord_vec(
    {"vec": [{"x": 0, "y": 0}, {"x": 1, "y": 2}]},
    {"vec": [{"x": 5, "y": 1}, {"x": 1}]},
))

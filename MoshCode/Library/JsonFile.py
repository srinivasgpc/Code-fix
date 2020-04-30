import json
from pathlib import Path
#
# movies = [
#     {"id":1, "title": "RObo", "year": 1989},
#     {"id":1, "title1": "RObo1", "year": 1990},
#     {"id":1, "title2": "RObo2", "year": 1989}
#
# ]
#
#
# data = json.dumps(movies)
#
# Path("movies.json").write_text(data)


data =Path("movies").read_text()
movies = json.loads(data)
print(movies[0]["title"])
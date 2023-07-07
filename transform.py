import sys

input_file = sys.argv[1]


from standalone import Lark_StandAlone
parser = Lark_StandAlone()

fyle = open(input_file)
data = fyle.read()
tree = parser.parse(data)
print(tree.pretty())

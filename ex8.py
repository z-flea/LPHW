formatter = "{} {} {} {}"

# I don't extactly understand why formatter.fomat(,,,,)
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True)) # why True not ""
print(formatter.format(formatter, formatter, formatter, formatter))
# print (
   why exits comma , because formatter had four {}, each {} one unit
)
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
import Chap03.header_area as mod
from Chap03.header_area import write

mod.say()
area, msg = mod.calc_area(type=1, a=5, b=5)
write(area, msg)
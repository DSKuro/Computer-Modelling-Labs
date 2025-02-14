import math

from Lab3.classes.Extremum import IntervalSearch
from Lab3.classes.Function import Function
from Lab3.classes.GoldenSection import GoldenSection
from Lab3.classes.Extremum import Interval
from Lab3.classes.Chord import Chord
from Lab3.classes.Graphic import Graphic

def golden_section_method():
    fn = Function(lambda x: math.sqrt(x) * math.atan(math.sqrt(x)))
    interval = Interval(1, 5)
    gs = GoldenSection()
    try:
        gs.find_extremum(fn, interval, True)
    except:
        print("Invalid value set")
        return

    graph = Graphic(fn, interval, 1)
    graph.create()

def chord_method():
    #fn = Function(lambda x: math.sqrt(x) * math.atan(math.sqrt(x)))
    fn = Function(lambda x: (x+2) ** 2)
    interval = Interval(-1, 0)
    ch = Chord()
    ch.find_extremum(fn, interval, True)
    c = IntervalSearch(fn, 1, interval)
    print(c.find_extremum_intervals()[0].get_end)

if __name__ == "__main__":
    fn = Function(lambda x: x ** 3 * math.e ** (3 * x))
    interval = Interval(-2, 2)
    find_int = IntervalSearch(fn, 1, interval)
    print(find_int.find_extremum_intervals()[0].get_end)
    graphic = Graphic(fn, interval, 1)
    graphic.create()

    epsilons = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14, 1e-15]

    gs = GoldenSection()
    ch = Chord()
    for epsilon in epsilons:
        try:
           gs.find_extremum(fn, interval, True)
           print(f"Iteration of GS: {gs.get_iterations}")
        except Exception as e:
            pass

        try:
            ch.find_extremum(fn, interval, True)
            print(f"Iteration of CH: {ch.get_iterations}")
        except Exception as e:
            print("yes")
            pass

    #golden_section_method()
    #chord_method()
import argparse
from parsing import getData
from argparse import RawTextHelpFormatter
from astar import aStarOptimized
from heuristics import heuristics
from is_solvable import isSolvable
from states import generateGoalState
from viz import Visualizer

parser = argparse.ArgumentParser(description="A n-puzzle solver", formatter_class=RawTextHelpFormatter)
parser.add_argument("-p", "--path", help="The path to the n-puzzle")
parser.add_argument("-he", "--heuristic", type=int, default=0, choices = [0,1,2], help="Your choice of heuristic for the search algorithm\n0 for manhattan distance(by default)\n1 for euclidean distance\n2 for out of place tiles")
parser.add_argument("-v", "--graphicalView", action="store_true", default=False, help="Displays movements in a graphical interface.")
args = parser.parse_args()

if not args.path:
    parser.error("You must provide a path")

if __name__ == '__main__':
    try:
        puzzle, size, matrix = getData(args)
        solved_state = generateGoalState()
        if isSolvable(puzzle, size, solved_state) != 0:
            heuristic = heuristics(args.heuristic)
            success, path, complexity = aStarOptimized(puzzle, solved_state, size, heuristic)
            if args.graphicalView:
                Visualizer(path, 3)
            if success:
                for s in path:
                    print(s)
                print(f"Open list: {complexity['space']}")
                print(f"Closed list: {complexity['time']}")
            else:
                print("Unsolvable")
        else:
            print("Unsolvable")
    except:
        print("ERROR")
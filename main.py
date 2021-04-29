import imp
import sys
from argparse import ArgumentParser
from pattern_search import pattern_search
from nelder_mead import nelder_mead_method
from gradient_descent import gradient_descent


def main(problem, method=0):
    if method == 0:
        pattern_search(problem.f, problem.x0, h=1e-01, eps=problem.eps, verbose=True)
    elif method == 1:
        nelder_mead_method(problem.f, problem.x0, eps=problem.eps)
    else:
        gradient_descent(problem.f, problem.x0)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--problem', type=str, help='path to file with problem to solve')
    parser.add_argument('--method', choices=['pattern_search', 'nelder_mead', 'gd'])
    args = parser.parse_args()
    problem = imp.load_source("problem", args.problem)
    if args.method == 'pattern_search':
        main(problem, 0)
    elif args.method == 'nelder_mead':
        main(problem, 1)
    else:
        main(problem, 2)

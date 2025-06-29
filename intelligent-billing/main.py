from parser import parser
from evaluator import evaluate, variables
from visualizer import print_tree as print_ast

def run_test_cases(filename):
    with open(filename, 'r') as f:
        for line in f:
            expr = line.strip()
            if not expr or expr.startswith("#"):
                continue
            print(f"\n➤ expr > {expr}")
            try:
                ast = parser.parse(expr)
                print(" AST:")
                print_ast(ast)  # comment out if visualizer not used
                result = evaluate(ast)
                print(f" Result: {result}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    run_test_cases("test_cases.txt")

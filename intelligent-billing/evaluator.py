variables = {}  # Runtime variable store

def evaluate(node):
    if isinstance(node, (int, float, bool)):
        return node

    if isinstance(node, str):
        return variables.get(node, 0)

    if isinstance(node, tuple):
        op = node[0]

        # Assignment
        if op == 'assign':
            var_name = node[1]
            value = evaluate(node[2])
            variables[var_name] = value
            return value

        # Add-assign
        if op == 'add_assign':
            var_name = node[1]
            value = evaluate(node[2])
            old = variables.get(var_name, 0)
            variables[var_name] = old + value
            return variables[var_name]

        # Binary operations
        if op in ('+', '-', '*', '/'):
            left = evaluate(node[1])
            right = evaluate(node[2])
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/':
                if right == 0:
                    raise ValueError("Division by zero")
                return left / right

        # Comparisons
        if op in ('>', '<', '>=', '<=', '==', '!='):
            left = evaluate(node[1])
            right = evaluate(node[2])
            if op == '>': return left > right
            if op == '<': return left < right
            if op == '>=': return left >= right
            if op == '<=': return left <= right
            if op == '==': return left == right
            if op == '!=': return left != right

        # Logical operations
        if op == '&&':
            return evaluate(node[1]) and evaluate(node[2])
        if op == '||':
            return evaluate(node[1]) or evaluate(node[2])
        if op == 'not':
            return not evaluate(node[1])

        # Ternary: (cond ? if_true : if_false)
        if op == 'if':
            cond = evaluate(node[1])
            return evaluate(node[2]) if cond else evaluate(node[3])

        # Function call: forecast(units)
        if op == 'func':
            func_name = node[1]
            arg = evaluate(node[2])
            if func_name == 'forecast':
                print(f"📈 Forecast used: ({arg} * 1.1 + 200)")
                return arg * 1.1 + 200
            else:
                raise Exception(f"Unknown function: {func_name}")

    raise ValueError(f"Invalid node: {node}")

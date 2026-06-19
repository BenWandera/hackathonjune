import sys
import os
import re
import json


def analyze_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return None

    # Regex patterns
    # Matches standard variable assignments like: my_var = 10 or x = "hello"
    # Excludes lines starting with 'if', comparisons '==', or inside comments
    var_pattern = re.compile(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=(?!=)')
    # Strict snake_case pattern (lowercase letters, numbers, and underscores)
    snake_case_pattern = re.compile(r'^[a-z0-9_]+$')

    # Metrics counters
    total_lines = 0
    blank_lines = 0
    comment_lines = 0
    code_lines = 0
    
    complexity_counts = {
        "if": 0,
        "elif": 0,
        "else": 0,
        "for": 0,
        "while": 0
    }
    
    warnings = []

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            total_lines += 1
            stripped = line.strip()

            # 1. Handle Blank Lines
            if not stripped:
                blank_lines += 1
                continue

            # 2. Handle Comments (Assuming standard # comments for Python)
            if stripped.startswith('#'):
                comment_lines += 1
                continue

            # If it's not blank and not a pure comment, it's a line of code
            code_lines += 1

            # 3. Complexity Check (Tokenizing to match whole words only)
            words = re.findall(r'\b\w+\b', stripped)
            for word in words:
                if word in complexity_counts:
                    complexity_counts[word] += 1

            # 4. Variable Check & snake_case Validation
            var_match = var_pattern.match(stripped)
            if var_match:
                var_name = var_match.group(1)
                if not snake_case_pattern.match(var_name):
                    warnings.append(f"Variable '{var_name}' at line {total_lines} is not snake_case")

    # 5. Calculate Comment Ratio
    comment_ratio = round((comment_lines / total_lines) * 100, 2) if total_lines > 0 else 0

    # 6. Calculate a Dynamic Health Score (Starting at 100, deducting for issues)
    # Deduct 5 points per non-snake_case variable, and cap it between 0 and 100
    health_score = max(0, 100 - (len(warnings) * 5))

    # Construct the JSON-like dictionary output
    output = {
        "health_score": f"{health_score}/100",
        "line_metrics": {
            "total_lines": total_lines,
            "blank_lines": blank_lines,
            "lines_of_code": code_lines,
            "comment_lines": comment_lines,
            "comment_ratio_pct": comment_ratio
        },
        "complexity_metrics": complexity_counts,
        "warnings": warnings
    }

    return output


if __name__ == "__main__":
    # Ensure a file path was passed via the CLI
    if len(sys.argv) < 2:
        print("Usage: python code_analyser.py <path_to_python_file>")
        sys.exit(1)

    target_file = sys.argv[1]
    results = analyze_file(target_file)

    if results:
        # Pretty print the JSON-like dictionary to the terminal
        print(json.dumps(results, indent=4))
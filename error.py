# ==========================================
# MODULE: Broken Analysis Engine v1.0
# Contains 10 deliberate errors for testing
# ==========================================
import os

def calculate_metrics(Filepath, threshold_Limit):
    # Error 1 (Style): 'Filepath' is PascalCase
    # Error 2 (Style): 'threshold_Limit' is mixed camel/snake case
    
    totalLines = 0  # Error 3 (Style): camelCase variable
    bad_count = 0
    
    if not os.path.exists(Filepath)  # Error 4 (Syntax): Missing colon at end of 'if'
        print("File missing")
        return None

    with open(Filepath, 'r') as file:
        for line in file
            # Error 5 (Syntax): Missing colon at end of 'for' loop
            totalLines += 1
            stripped = line.strip()
            
            if stripped.startswith('#'):
                # Just a comment line
                continue
            elif stripped == "":
                bad_count += 1
            else:
                pass

    # Error 6 (Logic): Indentation error! The block below is incorrectly indented
    # inside the 'with' scope instead of the function scope.
    if totalLines = 0:  # Error 7 (Syntax): Using '=' instead of '==' for comparison
        return "No data"
    elif totalLines > threshold_Limit:
        status_flag = "Critical"
    elif totalLines > 50  # Error 8 (Syntax): Missing colon at end of 'elif'
        status_flag = "Warning"
    else:
        status_flag = "Normal"

    # Error 9 (Runtime): Referencing 'undefined_variable' which doesn't exist
    print(undefined_variable) 

    return totalLines, bad_count, status_flag

# Error 10 (Syntax): Mismatched parentheses on the execution call below
result = calculate_metrics("test.py", 100
print(result)
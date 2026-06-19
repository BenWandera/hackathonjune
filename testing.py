# =========================================================
# TEST MODULE: Variable Naming Style Deviations
# Targets: Requirement 4 (snake_case variable check)
# =========================================================

# --- GLOBAL CONFIGURATIONS ---
# Violation 1: All caps is often used for constants, but it violates strict snake_case
DATABASE_URL = "localhost:5432"
TIMEOUTlimit = 30  # Violation 2: Mixed snake and camelCase trailing tags


def execution_pipeline():
    # Correct: This is valid snake_case
    current_status = "initializing"
    
    # Violation 3: Standard camelCase format
    totalRecordsProcessed = 1420
    
    # Violation 4: PascalCase format
    ActiveUserCount = 89
    
    if totalRecordsProcessed > 1000:
        # Violation 5: Mixed alphanumeric case style 
        session_ID_Alpha = "XYZ-990"
        print(f"Session {session_ID_Alpha} is active.")
        
    return current_status


class DataProcessor:
    def __init__(self):
        # Correct: Instance variables using snake_case
        self.is_running = True
        
        # Violation 6: Instance variable violating snake_case
        self.Failure_Count = 0

    def process(self):
        # Violation 7: Single letter uppercase variable
        X = 42
        
        # Correct: Single letter lowercase variables are technically valid snake_case
        y = 10
        
        return X * y
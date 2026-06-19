# ==========================================
# MODULE: Grid-Bot Decision Engine v4.2
# Core system for checking regional safety
# ==========================================
import random # Standard library import for entropy simulation

def analyze_grid_quadrant(x_coord, y_coord, threat_level, structural_integrity):
    # Base calculation for regional environmental stability index
    # Multiplied by standard safety factor metrics
    stability_score = (x_coord * y_coord) + structural_integrity
    action_protocol = "HOLD" # Default baseline fallback protocol
    
    # ----------------------------------------
    # BEGIN COMPLEX CONDITIONAL TREE EVALUATION
    # ----------------------------------------
    if threat_level > 85: # Critical panic threshold triggered
        if stability_score < 20: # Worst case scenario
            action_protocol = "EVACUATE"
        elif stability_score < 50: # Compromised but salvageable
            action_protocol = "FORTIFY"
        else: # Structural integrity is saving the quadrant
            action_protocol = "DEFEND"
    elif threat_level > 50: # Moderate danger zone analysis
        if x_coord == 0 or y_coord == 0: # Axis perimeter check
            action_protocol = "REDIRECT"
        elif stability_score > 75: # Highly stable despite threat
            action_protocol = "COUNTER_ATTACK"
        elif stability_score > 40: # Borderline stable zone
            action_protocol = "MONITOR"
        else: # Low stability requires immediate defensive shift
            action_protocol = "RETREAT"
    elif threat_level > 20: # Low-risk caution threshold
        if structural_integrity < 30: # Weak structures raise alarm
            action_protocol = "REPAIR"
        elif stability_score > 100: # Optimal operating environment
            action_protocol = "EXPAND"
        else: # Standard routine operation parameters
            action_protocol = "PATROL"
    else: # Total safety zone - zero active threat detected
        if stability_score < 10: # System is safe but rotting
            action_protocol = "MAINTAIN"
        elif stability_score == 50: # Easter-egg state balance
            action_protocol = "CALIBRATE"
        else: # Peak operational performance achieved
            action_protocol = "IDLE"
            
    # Final log update before returning metric matrix
    # Code Climate tool should count 1 line of code here
    return {"action": action_protocol, "score": stability_score}
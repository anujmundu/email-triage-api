def apply_rules(ai_output):
    """
    Apply smarter deterministic rules based on AI classification.
    """
    intent = ai_output.get("intent", "other")
    urgency = ai_output.get("urgency", "low")

    # --- Support cases ---
    if intent == "support":
        if urgency == "high":
            return "escalate"          # Critical issues → escalate immediately
        elif urgency == "medium":
            return "manual-review"     # Needs human judgment
        else:
            return "acknowledge"       # Low urgency support → acknowledge but not escalate

    # --- Sales cases ---
    elif intent == "sales":
        if urgency == "high":
            return "priority-reply"    # Hot leads → reply quickly
        elif urgency == "medium":
            return "auto-reply"        # Standard sales inquiries → auto-reply template
        else:
            return "defer"             # Low urgency sales → respond later

    # --- Spam cases ---
    elif intent == "spam":
        if urgency == "high":
            return "block"             # Aggressive spam → block sender
        else:
            return "ignore"            # Normal spam → ignore silently

    # --- Other / Unknown cases ---
    else:
        if urgency == "high":
            return "manual-review"     # Unknown but urgent → human check
        elif urgency == "medium":
            return "manual-review"     # Still needs human judgment
        else:
            return "archive"           # Low urgency + unknown intent → archive safely

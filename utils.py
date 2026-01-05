def validate_ai_output(ai_output):
    allowed_intents = ["support", "sales", "spam", "other"]
    allowed_urgency = ["low", "medium", "high"]

    if not isinstance(ai_output, dict):
        return False
    if ai_output.get("intent") not in allowed_intents:
        return False
    if ai_output.get("urgency") not in allowed_urgency:
        return False
    if not (0 <= ai_output.get("confidence", 0) <= 1):
        return False
    return True

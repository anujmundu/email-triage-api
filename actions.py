def take_action(email, decision):
    if decision == "auto-reply":
        print(f"Auto-reply sent to {email['sender']}")
    elif decision == "escalate":
        print(f"Escalation logged for {email['sender']}")
    elif decision == "ignore":
        print("Email ignored")
    else:
        print("Manual review required")

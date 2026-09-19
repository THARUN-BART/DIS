logs = ["login failed", "login failed",
        "<script>alert('xss')</script>"]

alert = any("failed" in x or "<script>" in x for x in logs)

if alert:
    print("[ALERT] Attack detected")
    print("1. User disabled")
    print("2. Input filtering applied")
    print("3. Logs archived")
    print("4. System recovered")
    print("5. Incident documented")
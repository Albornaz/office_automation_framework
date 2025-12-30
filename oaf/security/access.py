def check_access(user_role):
    if user_role not in ("admin", "finance"):
        raise PermissionError("Access denied")

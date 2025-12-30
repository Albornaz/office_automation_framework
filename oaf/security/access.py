ROLE_PERMISSIONS = {
    "admin": {"run_report", "email_report"},
    "finance": {"run_report"},
}

def check_permission(role: str, action: str):
    permissions = ROLE_PERMISSIONS.get(role, set())
    if action not in permissions:
        raise PermissionError(
            f"Role '{role}' is not allowed to perform '{action}'"
        )

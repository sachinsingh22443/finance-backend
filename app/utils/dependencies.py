from fastapi import Depends, HTTPException, Header
from typing import Literal

# 🔐 Step 1: Get role from request header
def get_current_role(x_role: Literal["admin", "analyst", "viewer"] = Header()):
    return x_role


# 🎯 Step 2: Role-based access control
def allow_roles(allowed_roles: list):
    """
    Restrict API access based on allowed roles

    Usage:
        Depends(allow_roles(["admin", "analyst"]))
    """

    def checker(role: str = Depends(get_current_role)):
        if role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail=f"Access denied. Allowed roles: {allowed_roles}"
            )
        return role

    return checker
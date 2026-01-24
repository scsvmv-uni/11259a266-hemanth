import functools

def requires_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract 'is_admin', defaulting to False if not provided
        is_admin = kwargs.pop("is_admin", False)
        
        if not is_admin:
            raise PermissionError("Admin privileges required")
        
        # Now call the original function with the remaining arguments
        return func(*args, **kwargs)
    return wrapper

@requires_admin
def reset_user_password(username: str) -> str:
    return f"Password reset for {username}"

# --- Testing the logic ---
try:
    # 1. Successful call
    print(reset_user_password("alice", is_admin=True))
    
    # 2. This will trigger the PermissionError
    print(reset_user_password("bob", is_admin=False))
except PermissionError as e:
    print(f"Caught: {e}")
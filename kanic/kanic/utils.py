def jwt_response_payload_handler(token, user=None, request=None):
    return {
        "token": token,
        "username": str(user.email),
        "active" : user.is_active,
        "is_mechanic": user.is_mechanic
    }

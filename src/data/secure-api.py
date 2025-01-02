import hashlib

class SecureAPIAccess:
    def __init__(self):
        self.tokens = {}

    def generate_api_token(self, user_id):
        """Generate a secure API token for a user."""
        token = hashlib.sha256(user_id.encode()).hexdigest()
        self.tokens[user_id] = token
        print(f"Generated API token for user {user_id}: {token}")
        return token

    def validate_api_token(self, user_id, token):
        """Validate an API token."""
        if user_id in self.tokens and self.tokens[user_id] == token:
            print("Token validation successful.")
            return True
        print("Token validation failed.")
        return False

# Example usage
if __name__ == "__main__":
    api_access = SecureAPIAccess()

    # Generate a token
    user_token = api_access.generate_api_token("user123")

    # Validate the token
    api_access.validate_api_token("user123", user_token)

    # Attempt validation with an invalid token
    api_access.validate_api_token("user123", "invalid_token")
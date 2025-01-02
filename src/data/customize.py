class CustomizableAgent:
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose
        self.configurations = {}
        print(f"Customizable agent {self.name} created for {self.purpose}.")

    def configure(self, setting, value):
        """Configure the agent with a specific setting."""
        self.configurations[setting] = value
        print(f"Agent {self.name} configured: {setting} set to {value}.")

    def perform_action(self, action):
        """Perform an action based on configuration."""
        if action in self.configurations:
            return f"Agent {self.name} performed {action} with setting: {self.configurations[action]}"
        else:
            return f"Action {action} not configured for agent {self.name}."

# Example usage
if __name__ == "__main__":
    # Create a customizable agent
    customer_service_agent = CustomizableAgent("CustomerSupportBot", "customer service")

    # Configure the agent
    customer_service_agent.configure("language", "English")
    customer_service_agent.configure("response_time", "fast")

    # Perform an action
    print(customer_service_agent.perform_action("language"))
    print(customer_service_agent.perform_action("response_time"))
    print(customer_service_agent.perform_action("unsupported_action"))
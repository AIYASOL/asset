class AIYATrainingSandbox:
    def __init__(self):
        self.models = {}

    def add_model(self, model_name, model_data):
        """Add a new model to the training sandbox."""
        self.models[model_name] = model_data
        print(f"Model {model_name} has been added to the training sandbox.")

    def train_model(self, model_name, data):
        """Simulate training a model."""
        if model_name in self.models:
            print(f"Training model {model_name} with provided data...")
            self.models[model_name]['training_data'] = data
            print(f"Model {model_name} has been successfully trained.")
        else:
            print(f"Model {model_name} not found in the training sandbox.")

    def deploy_model(self, model_name):
        """Simulate deploying a trained model."""
        if model_name in self.models and 'training_data' in self.models[model_name]:
            print(f"Deploying model {model_name}...")
            print(f"Model {model_name} is now live and ready to use.")
        else:
            print(f"Model {model_name} is not ready for deployment. Ensure it is trained.")

# Example usage
if __name__ == "__main__":
    sandbox = AIYATrainingSandbox()

    # Add a new model
    sandbox.add_model("SentimentAnalyzer", {"type": "NLP"})

    # Train the model
    sandbox.train_model("SentimentAnalyzer", ["positive", "negative", "neutral"])

    # Deploy the model
    sandbox.deploy_model("SentimentAnalyzer")
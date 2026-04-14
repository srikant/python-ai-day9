def normalize_vector(values):
    total = sum(values)
    normalized = [v/total for v in values]
    return normalized

def load_model(model_path):
    # Simulate loading a model (in reality, you'd use something like pickle or joblib)
    print(f"Loading model from {model_path}...")
    return {"status": "loaded", "path": model_path}

def predict(model, input_data):
    # Simulate a prediction (in reality, you'd use the model to make a prediction)
    return {"prediction": "class_a", "confidence": 0.95}

if __name__ == "__main__":
    print("=== Example 1: Basic Normalization ===")
    data = [1, 1, 2]
    result = normalize_vector(data)
    print(f"Input:  {data}")
    print(f"Output: {result}")
    print(f"Sum:    {sum(result)}  ← Should be 1.0!")
    print()

    print("=== Example 2: RGB Pixel Normalization ===")
    pixel = [255, 128, 64]
    result = normalize_vector(pixel)
    print(f"RGB values: {pixel}")
    print(f"Normalized: {result}")
    print()
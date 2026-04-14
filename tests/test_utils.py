from app.model_utils import normalize_vector

def test_normalize_standard():
    assert normalize_vector([1,1,2]) == [0.25, 0.25, 0.5]

def test_normalize_float_values():
    result = normalize_vector([0.5, 1.5, 2.0])
    assert abs(sum(result) - 1.0) < 0.0001

def test_normalize_single_element():
    assert normalize_vector([5]) == [1.0]

def test_normalize_all_zeros():
    pass

def test_integration_normalize_and_load():
    from app.model_utils import load_model, predict
    model = load_model("test_model.pkl")
    assert model["status"] == "loaded"

    result = predict(model, [1, 2, 3])
    assert "prediction" in result
    assert "confidence" in result
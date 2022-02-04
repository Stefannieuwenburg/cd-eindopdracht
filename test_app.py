import app

def test_index():
    assert app.index() == "Dit was de laatste opdracht"

def test_Stefan():
    assert app.Stefan() == "Goed Bezig Stefan!"
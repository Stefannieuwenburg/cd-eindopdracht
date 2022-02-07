import app

def test_index():
    assert app.index() == f"<h1>Dit was de laatste opdracht<h1>"

def test_Stefan():
    assert app.Stefan() == f"<h1>Goed Bezig Stefan!<h1>"
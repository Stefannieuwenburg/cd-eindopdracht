import main

def test_index():
    assert main.index() == f"<h1>Dit was de laatste opdracht<h1>"

def test_Stefan():
    assert main.Stefan() == f"<h1>Goed Bezig Stefan!<h1>"
def test_views_return():
    import views
    assert views.index() == 'Hello world'

def test_goodbye():
    import views()
    assert views.goodbye() == 'Goodbye world'

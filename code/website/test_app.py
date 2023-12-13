import os
import tempfile
import pytest
from app import app, db, perform_search


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_home_page(client):
    response = client.get('/')
    assert b'Welcome to Cooking Copilot!' in response.data


# def test_publish_page(client):
#     response = client.get('/publish')
#     assert b'Add Recipe' in response.data


# def test_recipe_creation(client):
#     response = client.post('/publish', data={
#         'authorname': 'John Doe',
#         'email': 'john@example.com',
#         'recipename': 'Test Recipe',
#         'recipedesc': 'This is a test recipe',
#         'serves': '2',
#         'image': 'test.jpg',
#         'time': '30 minutes',
#         'ingredients': '["Ingredient 1", "Ingredient 2"]',
#         'steps': '["Step 1", "Step 2"]',
#         'cuisine': 'Test Cuisine'
#     })
#     assert b'Recipe inserted successfully' in response.data

def test_scrambled_eggs_recipe(client):
    response = client.get('/scrambled-eggs')
    assert b'Scrambled Eggs' in response.data
    assert b'British' in response.data
    assert b'20 minutes' in response.data
    assert b'2' in response.data

def test_chatbot_interaction(client):
    response = client.post('/chatbot', data={'prompt': 'Hello, chatbot!'})
    assert response.status_code == 200

def test_chatbot_joke(client):
    response = client.post('/chatbot', data={'prompt': 'Tell me a joke'})
    assert response.data.strip()



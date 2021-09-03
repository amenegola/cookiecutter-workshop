import pytest

def fast_health_endpoint(fast_test_client):
    response = fast_test_client.get('/health')

    assert response.status_code == 200



def test_prediction_endpoint(fast_test_client,
                    model_payload_post,
                    wrong_payload_post):
    response = fast_test_client.post('/api/v1/recommendations',
                                      json=model_payload_post)
    assert response.status_code == 200

    response = fast_test_client.post('/api/v1/recommendations',
                                      json=wrong_payload_post)
    assert response.status_code == 422

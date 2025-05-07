import pytest
from src.weather import get_weather
from unittest.mock import patch

@patch('requests.get')
def test_get_weather_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"main": {"temp": 15.5}}
    
    result = get_weather()
    assert result["main"]["temp"] == 15.5

@patch('requests.get')
def test_get_weather_missing_key(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 401
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("401 Unauthorized")
    
    with pytest.raises(requests.exceptions.HTTPError):
        get_weather()
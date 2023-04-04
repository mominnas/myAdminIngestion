"""This module contains the main function for the Thibert API."""
import json
import requests
from typing import Dict, List, Union, Tuple, Optional
from tapi_client import Client, AuthenticatedClient
import tapi_client.models
import tapi_client.api
from tapi_client.types import Response
import cred




TAPI_KEY: str = cred.TAPI_KEY
JSON_URL: str = cred.JSON_URL
BASE_URL: str = cred.THIBERT_BASE_URL

def get_json() -> Dict[str, Union[str, Dict]]:
    """Get the JSON response from the API.
    
    Args:
        None
    Returns:
        str: The JSON response from the API.
    """
    response = requests.get(JSON_URL, timeout=500).text
    response_info = json.loads(response)
    print(f"Connected to OpenAPI ver {response_info.get('openapi')}")
    return response_info



def get_api_paths(response_info: Dict[str, Union[str, Dict]]) -> None:
    """Return the paths to the API method endpoints.

    Args:
        response_info (Dict[str, Union[str, Dict]]): Dictionary of the 
            OpenAPI json from the endpoint.
    """
    if response_info.get('paths') is None:
        print("No paths found.")
        return None
    for key in response_info['paths']:
        print(key)
        break


    return None



def generate_client(key: str=TAPI_KEY) -> Client:
    """Generate a client for the API.

    Returns:
        Client: _description_
    """
    client: Client = AuthenticatedClient(base_url=BASE_URL, token=key,
                                         timeout=50, verify_ssl=False,
                                         raise_on_unexpected_status=True)
    return client


if __name__ == "__main__":
    r_info: Dict[str, Union[str, Dict]] = get_json()
    get_api_paths(r_info)
    api_client = generate_client()
    print(api_client.get_headers())

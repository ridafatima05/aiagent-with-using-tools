import requests
from agents import function_tool


#FUNCTION TOOL: 

@function_tool
def fetch_user_data()-> list:
    """Fetch Function for user data and return list."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


@function_tool
def fetch_user_data_by_id(user_id: int) -> str:
    """
    Fetch user data from JSONPlaceholder by user ID.

    Args:
        user_id (int): The ID of the user to fetch.

    Returns:
        str: A nicely formatted string with user details.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, dict) and "id" in data:
        return (
            f"User ID: {data['id']}\n"
            f"Name: {data['name']}\n"
            f"Username: {data['username']}\n"
            f"Email: {data['email']}\n"
            f"Phone: {data['phone']}\n"
            f"Website: {data['website']}\n"
            f"Company: {data['company']['name']}\n"
            f"City: {data['address']['city']}"
        )
    return "No user found with that ID."

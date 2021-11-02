from openapi_server.config import config


def info_from_ApiKeyAuth(api_key, required_scopes):
    """
    Check and retrieve authentication information from api_key. Returned value
    will be passed in 'token_info' parameter of your operation function, if
    there is one. 'sub' or 'uid' will be set in 'user' parameter of your
    operation function, if there is one.

    :param api_key API key provided by Authorization header :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None :return: Information attached to provided
    api_key or None if api_key is invalid or does not allow access to called API
    :rtype: dict | None
    """
    try:
        # disable authentication if secret key is empty
        # TODO the time required to evaluate the key value must be independent
        # of the content of the api key defined by the server.
        if not config.secret_key or api_key == config.secret_key:
            return {'uid': 'user_id'}
    except Exception as error:
        print("Invalid API key", error)

    return None

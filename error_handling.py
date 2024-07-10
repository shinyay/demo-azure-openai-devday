from flask import jsonify

class AuthenticationError(Exception):
    pass

class InvalidSessionError(Exception):
    pass

def handle_authentication_error(e):
    response = jsonify({'error': 'Authentication failed', 'message': str(e)})
    response.status_code = 401
    return response

def handle_invalid_session_error(e):
    response = jsonify({'error': 'Invalid session', 'message': str(e)})
    response.status_code = 403
    return response

def register_error_handlers(app):
    app.register_error_handler(AuthenticationError, handle_authentication_error)
    app.register_error_handler(InvalidSessionError, handle_invalid_session_error)

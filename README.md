# Title

## Description
This project is a smart chatbot designed to provide quick and accurate responses to user queries. It leverages advanced Natural Language Processing (NLP) and machine learning models to understand and respond to user inputs contextually. The chatbot is integrated with Azure Open AI services to enhance its capabilities and ensure secure and scalable deployment.

## Smart Chatbot Requirements

### User Stories
- As a user, I want to interact with the chatbot to get quick responses to my queries.
- As an admin, I want to monitor the chatbot's performance and improve its responses.

### Features
- Natural Language Processing (NLP) for understanding user queries.
- Contextual responses based on user history.
- Integration with external APIs for fetching real-time data.
- Chat interface designed using Flask, responsive and user-friendly.
- Mock chat functionality using generative AI.

### Integration with Azure Open AI Services
- Utilize Azure Open AI for advanced NLP capabilities.
- Leverage Azure's machine learning models to improve chatbot accuracy.
- Ensure secure and scalable deployment using Azure services.

## Demo
A live demo of the smart chatbot can be accessed at [Demo Link]. The demo showcases the chatbot's ability to understand and respond to various user queries, demonstrating its NLP and contextual response capabilities.

## Features

- feature:1
- feature:2

## Chat Interface
The chat interface is designed using Flask and is responsive and user-friendly. It includes a form for user input and a display area for chat messages. The chat functionality is currently mocked using generative AI.

### Accessing the Chat Interface
1. Run the application: `python app.py`
2. Access the chat interface via the URL: `http://localhost:5000/chat`
3. Type your message in the input field and click "Send" to interact with the mock chat functionality.

## Requirement
- Azure Open AI subscription
- Python 3.8 or higher
- Flask framework
- Authlib for OAuth2 integration
- Flask-SQLAlchemy for database interactions

## Usage
1. Clone the repository: `git clone https://github.com/shinyay/demo-azure-openai-devday.git`
2. Navigate to the project directory: `cd demo-azure-openai-devday`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`
5. Access the chatbot via the provided URL.

## Installation
1. Ensure you have Python 3.8 or higher installed.
2. Clone the repository: `git clone https://github.com/shinyay/demo-azure-openai-devday.git`
3. Navigate to the project directory: `cd demo-azure-openai-devday`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`

## Authentication Setup

### OAuth2 Integration
1. **Choose OAuth2 Provider**: This project uses GitHub as the OAuth2 provider.
2. **Set Up OAuth2 Provider**:
   - Register the application with GitHub.
   - Obtain client ID and client secret.
3. **Create Login Page**:
   - The login page is located at `templates/login.html`.
4. **Create Registration Page**:
   - The registration page is located at `templates/register.html`.
5. **Implement OAuth2 Flow**:
   - The OAuth2 flow is integrated in the backend using Flask.
   - Relevant file paths: `app.py`.
6. **Define User Model**:
   - The user model is defined in `models.py`.
   - Database schema and migrations are included.
7. **Session Management**:
   - Session management is implemented in `session_management.py`.
8. **Error Handling**:
   - Error handling for authentication failures and invalid sessions is added in `error_handling.py`.
9. **Unit Tests**:
   - Unit tests for authentication endpoints and user model validations are written in `tests/test_authentication.py`.

### Running Unit Tests
To run the unit tests for authentication:
1. Ensure you have all dependencies installed.
2. Run the tests using the following command:
   ```
   python -m unittest discover -s tests
   ```

## References

## Licence

Released under the [MIT license](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

## Author

- github: <https://github.com/shinyay>
- twitter: <https://twitter.com/yanashin18618>
- mastodon: <https://mastodon.social/@yanashin>

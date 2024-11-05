import pytest
import allure
import json
from assertpy import assert_that
from builders.post_builder import PostBuilder
from utilities.request_utility import RequestUtility


@allure.epic("JSONPlaceholder API")
@allure.feature("Posts Management")
class TestPosts:

    @allure.title("Create new post with valid data")
    @allure.description("""
    Test steps:
    1. Prepare post data using builder pattern
    2. Send POST request to create new post
    3. Verify response status code and content
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_create_post(self):
        """Test creating a new post with complete data set"""
        # Arrange
        with allure.step("Prepare test data"):
            post_data = (PostBuilder()
                         .with_title("foo")
                         .with_body("bar")
                         .with_user_id(1)
                         .build())
            allure.attach(json.dumps(post_data, indent=2),
                          "Request Payload",
                          allure.attachment_type.JSON)

        # Act
        with allure.step("Send POST request to create new post"):
            response = RequestUtility.make_request("POST", "/posts", post_data)
            allure.attach(json.dumps(response.json(), indent=2),
                          "Response Data",
                          allure.attachment_type.JSON)

        # Assert
        with allure.step("Verify response"):
            assert_that(response.status_code).is_equal_to(201)
            response_json = response.json()
            assert_that(response_json).contains_key('id')
            assert_that(response_json['title']).is_equal_to('foo')
            assert_that(response_json['body']).is_equal_to('bar')
            assert_that(response_json['userId']).is_equal_to(1)

    @allure.title("Update existing post")
    @allure.description("""
    Test steps:
    1. Prepare update data
    2. Send PATCH request to update post
    3. Verify response status code and content
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_update_post(self):
        """Test updating an existing post's title"""
        # Arrange
        with allure.step("Prepare update data"):
            post_data = (PostBuilder()
                         .with_title("foo")
                         .build())
            allure.attach(json.dumps(post_data, indent=2),
                          "Update Payload",
                          allure.attachment_type.JSON)

        # Act
        with allure.step("Send PATCH request to update post"):
            response = RequestUtility.make_request("PATCH", "/posts/1", post_data)
            allure.attach(json.dumps(response.json(), indent=2),
                          "Response API",
                          allure.attachment_type.JSON)

        # Assert
        with allure.step("Verify response"):
            assert_that(response.status_code).is_equal_to(200)
            response_json = response.json()
            assert_that(response_json['title']).is_equal_to('foo')

    @allure.title("Get specific post")
    @allure.description("""
    Test steps:
    1. Send GET request for specific post
    2. Verify response structure and content
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_get_post(self):
        """Test retrieving a specific post"""
        # Act
        with allure.step("Send GET request for post ID 1"):
            response = RequestUtility.make_request("GET", "/posts/1")
            allure.attach(json.dumps(response.json(), indent=2),
                          "Response Data",
                          allure.attachment_type.JSON)

        # Assert
        with allure.step("Verify response structure"):
            assert_that(response.status_code).is_equal_to(200)
            response_json = response.json()
            assert_that(response_json).contains_key('id')
            assert_that(response_json).contains_key('title')
            assert_that(response_json).contains_key('body')
            assert_that(response_json).contains_key('userId')


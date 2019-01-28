Feature: This feature tests the functionalty of the REST API that I have just created

	@wip
	Scenario: Get my name from the REST API
			Given The flask server is running
			When I send a post request to the server url
			Then I should get back my name back in the response


from typing import Any

from pyconnectwise.endpoints.automate.ContactsIdEndpoint import ContactsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateContact
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Contacts", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ContactsIdEndpoint: The initialized ContactsIdEndpoint object.
        """
        child = ContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AutomateContact]:
        """
        Performs a GET request against the /Contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateContact]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateContact,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AutomateContact]:
        """
        Performs a GET request against the /Contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateContact]: The parsed response data.
        """
        return self._parse_many(AutomateContact, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateContact:
        """
        Performs a POST request against the /Contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateContact: The parsed response data.
        """
        return self._parse_one(AutomateContact, super()._make_request("POST", data=data, params=params).json())

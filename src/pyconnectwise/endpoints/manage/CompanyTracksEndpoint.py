from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksCountEndpoint import CompanyTracksCountEndpoint
from pyconnectwise.endpoints.manage.CompanyTracksIdEndpoint import CompanyTracksIdEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import Track
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyTracksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tracks", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyTracksCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyTracksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyTracksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyTracksIdEndpoint: The initialized CompanyTracksIdEndpoint object.
        """
        child = CompanyTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Track]:
        """
        Performs a GET request against the /company/tracks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Track]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Track,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Track]:
        """
        Performs a GET request against the /company/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Track]: The parsed response data.
        """
        return self._parse_many(Track, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Track:
        """
        Performs a POST request against the /company/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Track: The parsed response data.
        """
        return self._parse_one(Track, super()._make_request("POST", data=data, params=params).json())
from typing import Any

from pyconnectwise.endpoints.automate.NetworkdevicesIdEndpoint import (
    NetworkdevicesIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Models import NetworkDevice
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class NetworkdevicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Networkdevices", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> NetworkdevicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized NetworkdevicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            NetworkdevicesIdEndpoint: The initialized NetworkdevicesIdEndpoint object.
        """
        child = NetworkdevicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[NetworkDevice]:
        """
        Performs a GET request against the /Networkdevices endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[NetworkDevice]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            NetworkDevice,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[NetworkDevice]:
        """
        Performs a GET request against the /Networkdevices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[NetworkDevice]: The parsed response data.
        """
        return self._parse_many(
            NetworkDevice, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> NetworkDevice:
        """
        Performs a POST request against the /Networkdevices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            NetworkDevice: The parsed response data.
        """
        return self._parse_one(
            NetworkDevice,
            super()._make_request("POST", data=data, params=params).json(),
        )

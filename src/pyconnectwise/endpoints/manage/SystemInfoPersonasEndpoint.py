from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoPersonasCountEndpoint import SystemInfoPersonasCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoPersonasIdEndpoint import SystemInfoPersonasIdEndpoint
from pyconnectwise.models.manage import PersonasInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemInfoPersonasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "personas", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemInfoPersonasCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoPersonasIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoPersonasIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoPersonasIdEndpoint: The initialized SystemInfoPersonasIdEndpoint object.
        """
        child = SystemInfoPersonasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PersonasInfo]:
        """
        Performs a GET request against the /system/info/personas endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PersonasInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PersonasInfo,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PersonasInfo]:
        """
        Performs a GET request against the /system/info/personas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PersonasInfo]: The parsed response data.
        """
        return self._parse_many(PersonasInfo, super()._make_request("GET", data=data, params=params).json())

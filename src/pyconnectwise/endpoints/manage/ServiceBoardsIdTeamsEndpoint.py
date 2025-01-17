from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsCountEndpoint import ServiceBoardsIdTeamsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsIdEndpoint import ServiceBoardsIdTeamsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsInfoEndpoint import ServiceBoardsIdTeamsInfoEndpoint
from pyconnectwise.models.manage import BoardTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceBoardsIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ServiceBoardsIdTeamsInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(ServiceBoardsIdTeamsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceBoardsIdTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdTeamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdTeamsIdEndpoint: The initialized ServiceBoardsIdTeamsIdEndpoint object.
        """
        child = ServiceBoardsIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardTeam]:
        """
        Performs a GET request against the /service/boards/{id}/teams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardTeam]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardTeam,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardTeam]:
        """
        Performs a GET request against the /service/boards/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardTeam]: The parsed response data.
        """
        return self._parse_many(BoardTeam, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardTeam:
        """
        Performs a POST request against the /service/boards/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardTeam: The parsed response data.
        """
        return self._parse_one(BoardTeam, super()._make_request("POST", data=data, params=params).json())

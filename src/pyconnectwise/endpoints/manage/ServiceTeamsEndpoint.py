from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTeamsCountEndpoint import ServiceTeamsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceTeamsIdEndpoint import ServiceTeamsIdEndpoint
from pyconnectwise.models.manage import ServiceTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceTeamsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTeamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTeamsIdEndpoint: The initialized ServiceTeamsIdEndpoint object.
        """
        child = ServiceTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceTeam]:
        """
        Performs a GET request against the /service/teams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTeam]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ServiceTeam,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceTeam]:
        """
        Performs a GET request against the /service/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceTeam]: The parsed response data.
        """
        return self._parse_many(ServiceTeam, super()._make_request("GET", data=data, params=params).json())

from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import ProjectTicket
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectTicketsSearchEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "search", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectTicket]:
        """
        Performs a POST request against the /project/tickets/search endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTicket]: The parsed response data.
        """
        return self._parse_many(ProjectTicket, super()._make_request("POST", data=data, params=params).json())

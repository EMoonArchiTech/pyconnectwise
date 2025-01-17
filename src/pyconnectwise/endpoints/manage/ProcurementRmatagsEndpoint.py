from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmatagsCountEndpoint import ProcurementRmatagsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmatagsDefaultEndpoint import ProcurementRmatagsDefaultEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmatagsIdEndpoint import ProcurementRmatagsIdEndpoint
from pyconnectwise.models.manage import RmaTag
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementRmatagsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaTags", parent_endpoint=parent_endpoint)

        self.default = self._register_child_endpoint(ProcurementRmatagsDefaultEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(ProcurementRmatagsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementRmatagsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmatagsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmatagsIdEndpoint: The initialized ProcurementRmatagsIdEndpoint object.
        """
        child = ProcurementRmatagsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaTag]:
        """
        Performs a GET request against the /procurement/rmaTags endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaTag]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            RmaTag,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaTag]:
        """
        Performs a GET request against the /procurement/rmaTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaTag]: The parsed response data.
        """
        return self._parse_many(RmaTag, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaTag:
        """
        Performs a POST request against the /procurement/rmaTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaTag: The parsed response data.
        """
        return self._parse_one(RmaTag, super()._make_request("POST", data=data, params=params).json())

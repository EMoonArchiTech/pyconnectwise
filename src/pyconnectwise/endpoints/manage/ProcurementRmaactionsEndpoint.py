from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaactionsCountEndpoint import ProcurementRmaactionsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaactionsIdEndpoint import ProcurementRmaactionsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaactionsInfoEndpoint import ProcurementRmaactionsInfoEndpoint
from pyconnectwise.models.manage import RmaAction
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementRmaactionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaActions", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ProcurementRmaactionsInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(ProcurementRmaactionsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementRmaactionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmaactionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmaactionsIdEndpoint: The initialized ProcurementRmaactionsIdEndpoint object.
        """
        child = ProcurementRmaactionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaAction]:
        """
        Performs a GET request against the /procurement/rmaActions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaAction]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            RmaAction,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaAction]:
        """
        Performs a GET request against the /procurement/rmaActions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaAction]: The parsed response data.
        """
        return self._parse_many(RmaAction, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaAction:
        """
        Performs a POST request against the /procurement/rmaActions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaAction: The parsed response data.
        """
        return self._parse_one(RmaAction, super()._make_request("POST", data=data, params=params).json())

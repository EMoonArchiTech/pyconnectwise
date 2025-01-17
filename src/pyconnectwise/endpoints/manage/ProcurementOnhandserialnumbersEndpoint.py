from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementOnhandserialnumbersCountEndpoint import \
    ProcurementOnhandserialnumbersCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementOnhandserialnumbersIdEndpoint import \
    ProcurementOnhandserialnumbersIdEndpoint
from pyconnectwise.models.manage import OnHandSerialNumber
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementOnhandserialnumbersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "onhandserialnumbers", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementOnhandserialnumbersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementOnhandserialnumbersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementOnhandserialnumbersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementOnhandserialnumbersIdEndpoint: The initialized ProcurementOnhandserialnumbersIdEndpoint object.
        """
        child = ProcurementOnhandserialnumbersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OnHandSerialNumber]:
        """
        Performs a GET request against the /procurement/onhandserialnumbers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OnHandSerialNumber]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OnHandSerialNumber,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OnHandSerialNumber]:
        """
        Performs a GET request against the /procurement/onhandserialnumbers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OnHandSerialNumber]: The parsed response data.
        """
        return self._parse_many(OnHandSerialNumber, super()._make_request("GET", data=data, params=params).json())

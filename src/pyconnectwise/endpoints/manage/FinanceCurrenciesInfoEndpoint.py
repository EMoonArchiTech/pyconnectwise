from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceCurrenciesInfoCountEndpoint import FinanceCurrenciesInfoCountEndpoint
from pyconnectwise.models.manage import CurrencyInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceCurrenciesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceCurrenciesInfoCountEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CurrencyInfo]:
        """
        Performs a GET request against the /finance/currencies/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CurrencyInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CurrencyInfo,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CurrencyInfo]:
        """
        Performs a GET request against the /finance/currencies/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CurrencyInfo]: The parsed response data.
        """
        return self._parse_many(CurrencyInfo, super()._make_request("GET", data=data, params=params).json())

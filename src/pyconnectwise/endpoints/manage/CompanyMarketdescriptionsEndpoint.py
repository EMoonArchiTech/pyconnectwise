from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyMarketdescriptionsCountEndpoint import CompanyMarketdescriptionsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyMarketdescriptionsIdEndpoint import CompanyMarketdescriptionsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyMarketdescriptionsInfoEndpoint import CompanyMarketdescriptionsInfoEndpoint
from pyconnectwise.models.manage import MarketDescription
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyMarketdescriptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "marketDescriptions", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyMarketdescriptionsInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(CompanyMarketdescriptionsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyMarketdescriptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyMarketdescriptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyMarketdescriptionsIdEndpoint: The initialized CompanyMarketdescriptionsIdEndpoint object.
        """
        child = CompanyMarketdescriptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MarketDescription]:
        """
        Performs a GET request against the /company/marketDescriptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MarketDescription]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            MarketDescription,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MarketDescription]:
        """
        Performs a GET request against the /company/marketDescriptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MarketDescription]: The parsed response data.
        """
        return self._parse_many(MarketDescription, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MarketDescription:
        """
        Performs a POST request against the /company/marketDescriptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketDescription: The parsed response data.
        """
        return self._parse_one(MarketDescription, super()._make_request("POST", data=data, params=params).json())

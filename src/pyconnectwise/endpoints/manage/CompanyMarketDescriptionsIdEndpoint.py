from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyMarketdescriptionsIdInfoEndpoint import (
    CompanyMarketdescriptionsIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyMarketdescriptionsIdUsagesEndpoint import (
    CompanyMarketdescriptionsIdUsagesEndpoint,
)
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import MarketDescription
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyMarketdescriptionsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.usages = self._register_child_endpoint(
            CompanyMarketdescriptionsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyMarketdescriptionsIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MarketDescription]:
        """
        Performs a GET request against the /company/marketDescriptions/{id} endpoint and returns an initialized PaginatedResponse object.

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

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> MarketDescription:
        """
        Performs a GET request against the /company/marketDescriptions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketDescription: The parsed response data.
        """
        return self._parse_one(
            MarketDescription,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> GenericMessageModel:
        """
        Performs a DELETE request against the /company/marketDescriptions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(
            GenericMessageModel,
            super()._make_request("DELETE", data=data, params=params).json(),
        )

    def put(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> MarketDescription:
        """
        Performs a PUT request against the /company/marketDescriptions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketDescription: The parsed response data.
        """
        return self._parse_one(
            MarketDescription,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> MarketDescription:
        """
        Performs a PATCH request against the /company/marketDescriptions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketDescription: The parsed response data.
        """
        return self._parse_one(
            MarketDescription,
            super()._make_request("PATCH", data=data, params=params).json(),
        )

from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsCountEndpoint import FinanceBillingsetupsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsIdEndpoint import FinanceBillingsetupsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsInfoEndpoint import FinanceBillingsetupsInfoEndpoint
from pyconnectwise.models.manage import BillingSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceBillingsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingSetups", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(FinanceBillingsetupsInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(FinanceBillingsetupsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceBillingsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingsetupsIdEndpoint: The initialized FinanceBillingsetupsIdEndpoint object.
        """
        child = FinanceBillingsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[BillingSetup]:
        """
        Performs a GET request against the /finance/billingSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BillingSetup,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingSetup]:
        """
        Performs a GET request against the /finance/billingSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingSetup]: The parsed response data.
        """
        return self._parse_many(BillingSetup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingSetup:
        """
        Performs a POST request against the /finance/billingSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingSetup: The parsed response data.
        """
        return self._parse_one(BillingSetup, super()._make_request("POST", data=data, params=params).json())

from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesCountEndpoint import FinanceAccountingpackagesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesIdEndpoint import FinanceAccountingpackagesIdEndpoint
from pyconnectwise.models.manage import AccountingPackage
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAccountingpackagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accountingPackages", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceAccountingpackagesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceAccountingpackagesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingpackagesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingpackagesIdEndpoint: The initialized FinanceAccountingpackagesIdEndpoint object.
        """
        child = FinanceAccountingpackagesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AccountingPackage]:
        """
        Performs a GET request against the /finance/accountingPackages endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingPackage]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AccountingPackage,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AccountingPackage]:
        """
        Performs a GET request against the /finance/accountingPackages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AccountingPackage]: The parsed response data.
        """
        return self._parse_many(AccountingPackage, super()._make_request("GET", data=data, params=params).json())

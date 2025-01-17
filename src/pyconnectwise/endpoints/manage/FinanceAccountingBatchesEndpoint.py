from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesCountEndpoint import FinanceAccountingBatchesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEndpoint import FinanceAccountingBatchesIdEndpoint
from pyconnectwise.models.manage import AccountingBatch, GLExport
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAccountingBatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "batches", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceAccountingBatchesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceAccountingBatchesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingBatchesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingBatchesIdEndpoint: The initialized FinanceAccountingBatchesIdEndpoint object.
        """
        child = FinanceAccountingBatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AccountingBatch]:
        """
        Performs a GET request against the /finance/accounting/batches endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingBatch]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AccountingBatch,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AccountingBatch]:
        """
        Performs a GET request against the /finance/accounting/batches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AccountingBatch]: The parsed response data.
        """
        return self._parse_many(AccountingBatch, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GLExport:
        """
        Performs a POST request against the /finance/accounting/batches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLExport: The parsed response data.
        """
        return self._parse_one(GLExport, super()._make_request("POST", data=data, params=params).json())

from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementIdTaxablelevelsCountEndpoint import \
    FinanceAccountingUnpostedprocurementIdTaxablelevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementIdTaxablelevelsIdEndpoint import \
    FinanceAccountingUnpostedprocurementIdTaxablelevelsIdEndpoint
from pyconnectwise.models.manage import UnpostedProcurementTaxableLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAccountingUnpostedprocurementIdTaxablelevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableLevels", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAccountingUnpostedprocurementIdTaxablelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAccountingUnpostedprocurementIdTaxablelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedprocurementIdTaxablelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedprocurementIdTaxablelevelsIdEndpoint: The initialized FinanceAccountingUnpostedprocurementIdTaxablelevelsIdEndpoint object.
        """
        child = FinanceAccountingUnpostedprocurementIdTaxablelevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[UnpostedProcurementTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement/{id}/taxableLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedProcurementTaxableLevel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            UnpostedProcurementTaxableLevel,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[UnpostedProcurementTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement/{id}/taxableLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedProcurementTaxableLevel]: The parsed response data.
        """
        return self._parse_many(
            UnpostedProcurementTaxableLevel, super()._make_request("GET", data=data, params=params).json()
        )

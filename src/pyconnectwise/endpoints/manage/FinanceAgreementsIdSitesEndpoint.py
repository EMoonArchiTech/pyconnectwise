from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdSitesCountEndpoint import FinanceAgreementsIdSitesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdSitesIdEndpoint import FinanceAgreementsIdSitesIdEndpoint
from pyconnectwise.models.manage import AgreementSite
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementsIdSitesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sites", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceAgreementsIdSitesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceAgreementsIdSitesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdSitesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdSitesIdEndpoint: The initialized FinanceAgreementsIdSitesIdEndpoint object.
        """
        child = FinanceAgreementsIdSitesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AgreementSite]:
        """
        Performs a GET request against the /finance/agreements/{id}/sites endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementSite]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AgreementSite,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementSite]:
        """
        Performs a GET request against the /finance/agreements/{id}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementSite]: The parsed response data.
        """
        return self._parse_many(AgreementSite, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementSite:
        """
        Performs a POST request against the /finance/agreements/{id}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementSite: The parsed response data.
        """
        return self._parse_one(AgreementSite, super()._make_request("POST", data=data, params=params).json())

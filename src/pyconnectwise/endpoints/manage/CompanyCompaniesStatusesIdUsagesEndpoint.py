from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesStatusesIdUsagesListEndpoint import \
    CompanyCompaniesStatusesIdUsagesListEndpoint
from pyconnectwise.models.manage import Usage
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesStatusesIdUsagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "usages", parent_endpoint=parent_endpoint)

        self.list = self._register_child_endpoint(
            CompanyCompaniesStatusesIdUsagesListEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Usage]:
        """
        Performs a GET request against the /company/companies/statuses/{id}/usages endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Usage]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Usage,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Usage]:
        """
        Performs a GET request against the /company/companies/statuses/{id}/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Usage]: The parsed response data.
        """
        return self._parse_many(Usage, super()._make_request("GET", data=data, params=params).json())

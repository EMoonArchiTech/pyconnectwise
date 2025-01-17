from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsCountEndpoint import \
    CompanyManageddevicesintegrationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdEndpoint import \
    CompanyManageddevicesintegrationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsInfoEndpoint import \
    CompanyManageddevicesintegrationsInfoEndpoint
from pyconnectwise.models.manage import ManagedDevicesIntegration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManageddevicesintegrationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managedDevicesIntegrations", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            CompanyManageddevicesintegrationsInfoEndpoint(client, parent_endpoint=self)
        )
        self.count = self._register_child_endpoint(
            CompanyManageddevicesintegrationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyManageddevicesintegrationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManageddevicesintegrationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManageddevicesintegrationsIdEndpoint: The initialized CompanyManageddevicesintegrationsIdEndpoint object.
        """
        child = CompanyManageddevicesintegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ManagedDevicesIntegration]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegration]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagedDevicesIntegration,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagedDevicesIntegration]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegration]: The parsed response data.
        """
        return self._parse_many(
            ManagedDevicesIntegration, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegration:
        """
        Performs a POST request against the /company/managedDevicesIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegration: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegration, super()._make_request("POST", data=data, params=params).json()
        )

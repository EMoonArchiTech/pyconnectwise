from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesCountEndpoint import SalesOpportunitiesTypesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesIdEndpoint import SalesOpportunitiesTypesIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesInfoEndpoint import SalesOpportunitiesTypesInfoEndpoint
from pyconnectwise.models.manage import OpportunityType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SalesOpportunitiesTypesInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(SalesOpportunitiesTypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOpportunitiesTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesTypesIdEndpoint: The initialized SalesOpportunitiesTypesIdEndpoint object.
        """
        child = SalesOpportunitiesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OpportunityType]:
        """
        Performs a GET request against the /sales/opportunities/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OpportunityType,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityType]:
        """
        Performs a GET request against the /sales/opportunities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityType]: The parsed response data.
        """
        return self._parse_many(OpportunityType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityType:
        """
        Performs a POST request against the /sales/opportunities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityType: The parsed response data.
        """
        return self._parse_one(OpportunityType, super()._make_request("POST", data=data, params=params).json())

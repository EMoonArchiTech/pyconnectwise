from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesCountEndpoint import ExpenseTypesCountEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesIdEndpoint import ExpenseTypesIdEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesInfoEndpoint import ExpenseTypesInfoEndpoint
from pyconnectwise.models.manage import ExpenseType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ExpenseTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ExpenseTypesInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(ExpenseTypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ExpenseTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseTypesIdEndpoint: The initialized ExpenseTypesIdEndpoint object.
        """
        child = ExpenseTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExpenseType]:
        """
        Performs a GET request against the /expense/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ExpenseType,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExpenseType]:
        """
        Performs a GET request against the /expense/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseType]: The parsed response data.
        """
        return self._parse_many(ExpenseType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ExpenseType:
        """
        Performs a POST request against the /expense/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ExpenseType: The parsed response data.
        """
        return self._parse_one(ExpenseType, super()._make_request("POST", data=data, params=params).json())

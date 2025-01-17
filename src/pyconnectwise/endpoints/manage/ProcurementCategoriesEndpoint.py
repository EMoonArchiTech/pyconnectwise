from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesCountEndpoint import ProcurementCategoriesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesIdEndpoint import ProcurementCategoriesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesInfoEndpoint import ProcurementCategoriesInfoEndpoint
from pyconnectwise.models.manage import Category
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "categories", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ProcurementCategoriesInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(ProcurementCategoriesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementCategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCategoriesIdEndpoint: The initialized ProcurementCategoriesIdEndpoint object.
        """
        child = ProcurementCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Category]:
        """
        Performs a GET request against the /procurement/categories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Category]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Category,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Category]:
        """
        Performs a GET request against the /procurement/categories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Category]: The parsed response data.
        """
        return self._parse_many(Category, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Category:
        """
        Performs a POST request against the /procurement/categories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Category: The parsed response data.
        """
        return self._parse_one(Category, super()._make_request("POST", data=data, params=params).json())

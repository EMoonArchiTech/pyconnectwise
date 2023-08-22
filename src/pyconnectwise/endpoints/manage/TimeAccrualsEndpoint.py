from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeAccrualsCountEndpoint import TimeAccrualsCountEndpoint
from pyconnectwise.endpoints.manage.TimeAccrualsIdEndpoint import TimeAccrualsIdEndpoint
from pyconnectwise.models.manage import TimeAccrual
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeAccrualsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accruals", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(TimeAccrualsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeAccrualsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeAccrualsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeAccrualsIdEndpoint: The initialized TimeAccrualsIdEndpoint object.
        """
        child = TimeAccrualsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeAccrual]:
        """
        Performs a GET request against the /time/accruals endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeAccrual]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TimeAccrual,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimeAccrual]:
        """
        Performs a GET request against the /time/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeAccrual]: The parsed response data.
        """
        return self._parse_many(TimeAccrual, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeAccrual:
        """
        Performs a POST request against the /time/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeAccrual: The parsed response data.
        """
        return self._parse_one(TimeAccrual, super()._make_request("POST", data=data, params=params).json())

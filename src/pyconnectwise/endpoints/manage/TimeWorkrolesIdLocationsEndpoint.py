from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesIdLocationsCountEndpoint import TimeWorkrolesIdLocationsCountEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesIdLocationsIdEndpoint import TimeWorkrolesIdLocationsIdEndpoint
from pyconnectwise.models.manage import WorkRoleLocation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeWorkrolesIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(TimeWorkrolesIdLocationsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeWorkrolesIdLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeWorkrolesIdLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeWorkrolesIdLocationsIdEndpoint: The initialized TimeWorkrolesIdLocationsIdEndpoint object.
        """
        child = TimeWorkrolesIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[WorkRoleLocation]:
        """
        Performs a GET request against the /time/workRoles/{id}/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRoleLocation]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            WorkRoleLocation,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkRoleLocation]:
        """
        Performs a GET request against the /time/workRoles/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkRoleLocation]: The parsed response data.
        """
        return self._parse_many(WorkRoleLocation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleLocation:
        """
        Performs a POST request against the /time/workRoles/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleLocation: The parsed response data.
        """
        return self._parse_one(WorkRoleLocation, super()._make_request("POST", data=data, params=params).json())

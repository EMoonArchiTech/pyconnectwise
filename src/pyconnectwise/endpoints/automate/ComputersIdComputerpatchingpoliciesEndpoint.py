from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechComputerPatchingPolicy
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdComputerpatchingpoliciesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Computerpatchingpolicies", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechComputerPatchingPolicy]:
        """
        Performs a GET request against the /Computers/{id}/Computerpatchingpolicies endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerPatchingPolicy]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechComputerPatchingPolicy,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechComputerPatchingPolicy]:
        """
        Performs a GET request against the /Computers/{id}/Computerpatchingpolicies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechComputerPatchingPolicy]: The parsed response data.
        """
        return self._parse_many(
            LabTechComputerPatchingPolicy, super()._make_request("GET", data=data, params=params).json()
        )

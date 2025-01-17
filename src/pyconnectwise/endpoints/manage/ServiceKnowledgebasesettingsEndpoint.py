from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesettingsIdEndpoint import ServiceKnowledgebasesettingsIdEndpoint
from pyconnectwise.models.manage import KnowledgeBaseSettings
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceKnowledgebasesettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgebasesettings", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ServiceKnowledgebasesettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgebasesettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceKnowledgebasesettingsIdEndpoint: The initialized ServiceKnowledgebasesettingsIdEndpoint object.
        """
        child = ServiceKnowledgebasesettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[KnowledgeBaseSettings]:
        """
        Performs a GET request against the /service/knowledgebasesettings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseSettings]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            KnowledgeBaseSettings,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseSettings:
        """
        Performs a GET request against the /service/knowledgebasesettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSettings: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseSettings, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseSettings:
        """
        Performs a POST request against the /service/knowledgebasesettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSettings: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseSettings, super()._make_request("POST", data=data, params=params).json())

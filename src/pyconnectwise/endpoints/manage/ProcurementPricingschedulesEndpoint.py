from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesCountEndpoint import (
    ProcurementPricingschedulesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesIdEndpoint import (
    ProcurementPricingschedulesIdEndpoint,
)
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import PricingSchedule
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPricingschedulesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "pricingschedules", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementPricingschedulesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPricingschedulesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPricingschedulesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPricingschedulesIdEndpoint: The initialized ProcurementPricingschedulesIdEndpoint object.
        """
        child = ProcurementPricingschedulesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PricingSchedule]:
        """
        Performs a GET request against the /procurement/pricingschedules endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PricingSchedule]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PricingSchedule,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[PricingSchedule]:
        """
        Performs a GET request against the /procurement/pricingschedules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PricingSchedule]: The parsed response data.
        """
        return self._parse_many(
            PricingSchedule,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> PricingSchedule:
        """
        Performs a POST request against the /procurement/pricingschedules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PricingSchedule: The parsed response data.
        """
        return self._parse_one(
            PricingSchedule,
            super()._make_request("POST", data=data, params=params).json(),
        )

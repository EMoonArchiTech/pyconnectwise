from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanytypeassociationsCountEndpoint import \
    CompanyCompanytypeassociationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanytypeassociationsIdEndpoint import \
    CompanyCompanytypeassociationsIdEndpoint
from pyconnectwise.models.manage import CompanyCompanyTypeAssociation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompanytypeassociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companyTypeAssociations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyCompanytypeassociationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyCompanytypeassociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompanytypeassociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompanytypeassociationsIdEndpoint: The initialized CompanyCompanytypeassociationsIdEndpoint object.
        """
        child = CompanyCompanytypeassociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CompanyCompanyTypeAssociation]:
        """
        Performs a GET request against the /company/companyTypeAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyCompanyTypeAssociation]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CompanyCompanyTypeAssociation,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyCompanyTypeAssociation]:
        """
        Performs a GET request against the /company/companyTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyCompanyTypeAssociation]: The parsed response data.
        """
        return self._parse_many(
            CompanyCompanyTypeAssociation, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyCompanyTypeAssociation:
        """
        Performs a POST request against the /company/companyTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyCompanyTypeAssociation: The parsed response data.
        """
        return self._parse_one(
            CompanyCompanyTypeAssociation, super()._make_request("POST", data=data, params=params).json()
        )

from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesEndpoint import (
    ConfigurationsTypesEndpoint,
)
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "configurations", parent_endpoint=parent_endpoint)

        self.types = self._register_child_endpoint(
            ConfigurationsTypesEndpoint(client, parent_endpoint=self)
        )

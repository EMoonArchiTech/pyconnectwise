from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketnoteIdMarkasEndpoint import ProjectTicketnoteIdMarkasEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectTicketnoteIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.mark_as = self._register_child_endpoint(ProjectTicketnoteIdMarkasEndpoint(client, parent_endpoint=self))

from ._add_species_service import AddSpeciesService
from ._add_user_service import AddUserService
from ._fetch_critter_service import FetchCritterService
from ._fetch_species_service import FetchSpeciesService
from ._fetch_user_service import FetchUserService
from ._get_critters_service import GetCrittersService
from ._get_events_service import GetEventsService
from ._get_species_service import GetSpeciesService
from ._get_status_service import GetStatusService
from ._get_users_service import GetUsersService
from ._init_service import InitService
from ._ping_service import PingService
from ._post_event_service import PostEventService
from ._spawn_critter_service import SpawnCritterService

ALL_SERVICES = (
    AddSpeciesService,
    AddUserService,
    FetchCritterService,
    FetchSpeciesService,
    FetchUserService,
    GetCrittersService,
    GetEventsService,
    GetSpeciesService,
    GetStatusService,
    GetUsersService,
    InitService,
    PingService,
    PostEventService,
    SpawnCritterService,
)

__all__ = (
    AddSpeciesService.__name__,
    AddUserService.__name__,
    FetchCritterService.__name__,
    FetchSpeciesService.__name__,
    FetchUserService.__name__,
    GetCrittersService.__name__,
    GetEventsService.__name__,
    GetSpeciesService.__name__,
    GetStatusService.__name__,
    GetUsersService.__name__,
    InitService.__name__,
    PingService.__name__,
    PostEventService.__name__,
    SpawnCritterService.__name__,
)

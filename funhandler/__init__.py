import sys

from .base import (
    set_host,
    set_store_name,
    initialize_database,
    get_db_params,
)
from .data import add_bars, load_data
from .file_manager import (
    set_storage_model,
    set_local_storage_info,
    set_cloud_storage_info,
    store_local_storage,
    store_cloud_storage,
)

this = sys.modules[__name__]

this.store_name = 'datahandler'
this.host = None
this.db = None
this.current_storage_type = ''
this.storage_information = {}

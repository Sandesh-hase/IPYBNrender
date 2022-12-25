from IPython import display
from ensure import ensure_annotations
from IPYNBrenderer.custom_exception import InvalidURLException
from IPYNBrenderer.logger import logger
from py_youtube import Data

@ensure_annotations
def get_time_info(URL: str) -> int:
    def _verify_vid_id_len(vid_id, __expected_len=11):
        len_of_vid_id = len(vid_id)
        if len_of_vid_id != __expected_len:
            raise InvalidURLException(
                f"Invalid video id with length: {len_of_vid_id}, expected: {__expected_len}"
            )
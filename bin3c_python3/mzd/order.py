"""Small ordering interface used by the METAHI-T bin3C clustering adapter."""

import numpy as np


class SeqOrder:
    """Create the typed sequence-index records expected by bin3C clustering."""

    FORWARD = 1
    INDEX_TYPE = np.dtype([("index", np.int32), ("ori", np.int8)])

    @staticmethod
    def asindex(indices):
        indices = np.asarray(indices, dtype=np.int32)
        return np.array(
            list(zip(indices, np.full(len(indices), SeqOrder.FORWARD, dtype=np.int8))),
            dtype=SeqOrder.INDEX_TYPE,
        )

from unittest import mock as mock

import time_machine

# Ensure no real clock is used in tests.
m_time = time_machine.travel("202003010000Z", tick=True).start()

# Conftest

# Create Token
# Create Booking Id
# Update the Booking(Put) - BookingID, Token
# Delete the Booking

# Verify that created booking id when we update we are able to update it and delete it also

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class TestCRUDBooking(object):
    def test_update_booking_id_token(self):
        pass

    def test_delete_booking_id(self):
        pass













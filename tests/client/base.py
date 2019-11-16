import unittest
from unittest.mock import MagicMock

from requests import HTTPError
from spotipy.client.base import SpotifyBase
from spotipy.model.error import PlayerErrorReason


class TestSpotifyBase(unittest.TestCase):
    def setUp(self):
        self.client = SpotifyBase('token')

    def test_token_equals_given_token(self):
        self.assertEqual(self.client.token, 'token')

    def test_token_assignable(self):
        self.client.token = 'new'
        self.assertEqual(self.client.token, 'new')

    def test_token_equals_str_of_given_value(self):
        self.client.token = 1
        self.assertEqual(self.client.token, '1')

    def test_new_token_used_in_context(self):
        with self.client.token_as('new'):
            self.assertEqual(self.client.token, 'new')

    def test_old_token_restored_after_context(self):
        with self.client.token_as('new'):
            pass
        self.assertEqual(self.client.token, 'token')

    def test_next_with_no_next_set_returns_none(self):
        paging = MagicMock()
        paging.next = None

        next_ = self.client.next(paging)
        self.assertIsNone(next_)

    def test_previous_with_no_previous_set_returns_none(self):
        paging = MagicMock()
        paging.previous = None

        previous = self.client.previous(paging)
        self.assertIsNone(previous)

    def test_bad_request_is_parsed_for_error_reason(self):
        error = list(PlayerErrorReason)[0]

        class BadResponse:
            status_code = 400
            url = 'example.com'

            @staticmethod
            def json():
                return {
                    'message': 'Error message',
                    'reason': error.name
                }

        sender = MagicMock()
        sender.send.return_value = BadResponse()
        self.client.sender = sender

        try:
            self.client._get('example.com')
        except HTTPError as e:
            self.assertIn(error.value, str(e))
# -*- coding: utf-8 -*-
from mock import MagicMock, patch, Mock
from openprocurement.bridge.competitivedialogue.databridge import TendersClientSync
from restkit.errors import ResourceError
import unittest


class TenderClientTestCase(unittest.TestCase):

    def test_exception_access_http_code(self):
        with patch("openprocurement_client.client.TendersClientSync.create_tender") as create_tender:
            create_tender.side_effect = ResourceError(msg="Hi", http_code=422)

            client = TendersClientSync("", host_url="https://lb-api-sandbox.prozorro.gov.ua", api_version="2.4")

            with self.assertRaises(ResourceError) as exc:
                client.create_tender({})

            self.assertEqual(exc.exception.status_int, 422)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TenderClientTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

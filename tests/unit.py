import unittest
import responses
from bipolar import BipolarClient


class BipolarClientTest(unittest.TestCase):
    def setUp(self):
        self.client = BipolarClient(
                #base_url="http://bipolar.tdispatch.com",
                base_url="http://bipolar.test",
                api_key="XyLHPw78WfoHlHacDfvbtKiPKvQxNbmt",
                )

    def tearDown(self):
        responses.reset()

    @responses.activate
    def test_add_feature_error(self):
        responses.add(
            method="POST",
            url="http://bipolar.test/api/v1/feature/",
            body='AAA'
            )

        try:
            resp = self.client.add_feature(
                name="test",
                )
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_add_feature(self):
        responses.add(
            method="POST",
            url="http://bipolar.test/api/v1/feature/",
            body='{"boolean_permission": true, "creation": "2014-05-23T08:54:42.077131", "id": 10, "limit_permission": null, "name": "data.business", "permission_level": "qualifier", "permission_type": "boolean", "resource_uri": "/api/v1/feature/10/"}'
            )

        resp = self.client.add_feature(
                name="data.business",
                permission_type='boolean',
                boolean_permission=True,
                limit_permission=None,
                permission_level='qualifier',
                )
        expected = {
                'name': 'data.business',
                'permission_type': 'boolean',
                'boolean_permission': True,
                'limit_permission': None,
                'permission_level': 'qualifier',
                }
        self.assertTrue("id" in resp.keys())
        self.assertTrue("resource_uri" in resp.keys())
        self.assertTrue("creation" in resp.keys())
        for k, v in expected.items():
            self.assertEqual((k, resp[k]), (k, v))

    @responses.activate
    def test_update_feature_error(self):
        responses.add(
            method="PUT",
            url="http://bipolar.test/api/v1/feature/data.business/",
            body='AAA'
            )

        try:
            resp = self.client.update_feature(
                name="data.business",
                boolean_permission=False
                )
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_update_feature(self):
        responses.add(
            method="PUT",
            url="http://bipolar.test/api/v1/feature/data.business/",
            body='{"boolean_permission": false, "creation": "2014-05-23T08:43:13.340877", "id": 4, "limit_permission": null, "name": "data.business", "permission_level": "qualifier", "permission_type": "boolean", "resource_uri": "/api/v1/feature/4/"}'
            )

        resp = self.client.update_feature(
                name="data.business",
                boolean_permission=False
                )
        expected = {
                'name': 'data.business',
                'permission_type': 'boolean',
                'boolean_permission': False,
                'limit_permission': None,
                'permission_level': 'qualifier',
                }
        self.assertTrue("id" in resp.keys())
        self.assertTrue("resource_uri" in resp.keys())
        self.assertTrue("creation" in resp.keys())
        for k, v in expected.items():
            self.assertEqual((k, resp[k]), (k, v))

    @responses.activate
    def test_get_feature_error(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/feature/data.business",
            body='AAA'
            )

        try:
            resp = self.client.get_feature(
                name="data.business",
                )
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_get_feature(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/feature/data.business",
            body='{"boolean_permission": true, "creation": "2014-05-23T08:43:13.340877", "id": 4, "limit_permission": null, "name": "data.business", "permission_level": "qualifier", "permission_type": "boolean", "resource_uri": "/api/v1/feature/4/"}'
            )

        resp = self.client.get_feature(
                name="data.business",
                )
        expected = {
                'name': 'data.business',
                'permission_type': 'boolean',
                'boolean_permission': True,
                'limit_permission': None,
                'permission_level': 'qualifier',
                }
        self.assertTrue("id" in resp.keys())
        self.assertTrue("resource_uri" in resp.keys())
        self.assertTrue("creation" in resp.keys())
        for k, v in expected.items():
            self.assertEqual((k, resp[k]), (k, v))

    @responses.activate
    def test_list_features_error(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/feature/",
            body='AAA'
            )

        try:
            resp = self.client.list_features()
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_list_features(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/feature/",
            body='{"meta": {"previous": null, "total_count": 1, "offset": 0, "limit": 10, "next": null}, "objects": [{"name": "data.business", "creation": "2014-05-23T08:43:13.340877", "permission_type": "boolean", "boolean_permission": false, "limit_permission": null, "permission_level": "qualifier", "id": 4, "resource_uri": "/api/v1/feature/4/"}]}'
            )

        resp = self.client.list_features()
        self.assertEqual(len(resp["objects"]), 1)
        self.assertEqual(set(resp["objects"][0].keys()), set([
            'name',
            'creation',
            'permission_type',
            'boolean_permission',
            'limit_permission',
            'permission_level',
            'id',
            'resource_uri',
            ]))

    @responses.activate
    def test_delete_feature(self):
        responses.add(
            method="DELETE",
            url="http://bipolar.test/api/v1/feature/data.business",
            body='',
            status=204
            )

        resp = self.client.delete_feature("data.business")
        self.assertTrue(resp)

    @responses.activate
    def test_add_qualifier_error(self):
        responses.add(
            method="POST",
            url="http://bipolar.test/api/v1/qualifier/",
            body='AAA'
            )

        try:
            resp = self.client.add_qualifier(
                name="test-free",
                )
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_add_qualifier(self):
        responses.add(
            method="POST",
            url="http://bipolar.test/api/v1/qualifier/",
            body='{"creation": "2014-05-23T09:30:32.232231", "id": 2, "name": "test-free", "permissions": {"crm.business": false, "crm.locations_limit": 0, "crm.person": false}, "resource_uri": "/api/v1/qualifier/2/"}'
            )

        resp = self.client.add_qualifier(
                name="test-free",
                )
        expected = {
                'name': 'test-free',
                }
        self.assertTrue("id" in resp.keys())
        self.assertTrue("resource_uri" in resp.keys())
        self.assertTrue("creation" in resp.keys())
        for k, v in expected.items():
            self.assertEqual((k, resp[k]), (k, v))

    @responses.activate
    def test_get_qualifier_error(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/qualifier/test-free",
            body='AAA'
            )

        try:
            resp = self.client.get_qualifier(
                name="test-free",
                )
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_get_qualifier(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/qualifier/test-free",
            body='{"creation": "2014-05-23T09:30:32.232231", "id": 2, "name": "test-free", "permissions": {"crm.business": false, "crm.locations_limit": 0, "crm.person": false}, "resource_uri": "/api/v1/qualifier/2/"}'
            )

        resp = self.client.get_qualifier(
                name="test-free",
                )
        expected = {
                'name': 'test-free',
                }
        self.assertTrue("id" in resp.keys())
        self.assertTrue("resource_uri" in resp.keys())
        self.assertTrue("creation" in resp.keys())
        for k, v in expected.items():
            self.assertEqual((k, resp[k]), (k, v))

    @responses.activate
    def test_list_qualifiers_error(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/qualifier/",
            body='AAA'
            )

        try:
            resp = self.client.list_qualifiers()
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_list_qualifiers(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/qualifier/",
            body='{"meta": {"limit": 10, "next": null, "offset": 0, "previous": null, "total_count": 1}, "objects": [{"creation": "2014-05-23T09:30:32.232231", "id": 2, "name": "test-free", "permissions": {"crm.business": false, "crm.locations_limit": 0, "crm.person": false}, "resource_uri": "/api/v1/qualifier/2/"}]}'
            )

        resp = self.client.list_qualifiers()
        self.assertEqual(len(resp["objects"]), 1)
        self.assertEqual(set(resp["objects"][0].keys()), set([
            'name',
            'creation',
            'id',
            'resource_uri',
            "permissions",
            ]))

    @responses.activate
    def test_delete_qualifier(self):
        responses.add(
            method="DELETE",
            url="http://bipolar.test/api/v1/qualifier/test-free",
            body='',
            status=204
            )

        resp = self.client.delete_qualifier("test-free")
        self.assertTrue(resp)

    @responses.activate
    def test_set_permissions_error(self):
        responses.add(
            method="POST",
            url="http://bipolar.test/api/v1/permissions/",
            body='AAA',
            status=201
            )

        try:
            resp = self.client.set_permissions({
                "test-free": {
                    "data.business": True,
                    }
                })
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 201 / content: AAA')

    @responses.activate
    def test_set_permissions(self):
        responses.add(
            method="POST",
            url="http://bipolar.test/api/v1/permissions/",
            body='{"permissions": {"test-free": {"data.business": true}}, "resource_uri": ""}',
            status=201
            )

        resp = self.client.set_permissions({
            "test-free": {
                "data.business": True,
                }
            })
        self.assertEqual(resp, {"test-free": {"data.business": True}})

    @responses.activate
    def test_get_permissions_error(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/permissions/",
            body='AAA',
            )

        try:
            resp = self.client.get_permissions()
        except ValueError as e:
            self.assertEqual(str(e), 'No JSON object could be decoded. status: 200 / content: AAA')

    @responses.activate
    def test_get_permissions(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/permissions/",
            body='{"permissions": {"test-free": {"data.business": true}}, "resource_uri": ""}',
            )

        resp = self.client.get_permissions()
        self.assertEqual(resp, {"test-free": {"data.business": True}})

    @responses.activate
    def test_get_permissions_for_qualifier(self):
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/permissions/?qualifier=test-free",
            body='{"permissions": {"test-free": {"data.business": true}}}',
            match_querystring=True,
            )
        responses.add(
            method="GET",
            url="http://bipolar.test/api/v1/permissions/?qualifier=test-not-found",
            body='{"permissions": {"test-free": {"data.business": true}}}',
            match_querystring=True,
            )

        resp = self.client.get_permissions(qualifier="test-not-found")
        self.assertEqual(resp, {"test-free": {"data.business": True}})

        resp = self.client.get_permissions(qualifier="test-free")
        self.assertEqual(resp, {"test-free": {"data.business": True}})


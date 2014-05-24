#!/usr/bin/env python
# coding: utf-8

import requests
import urllib
import json


class UnexpectedStatusCode(Exception):
    pass


class BipolarClient(object):
    base_url = None
    api_key = None
    version = "v1"

    def __init__(self, base_url="http://localhost:5006", api_key=None, version="v1"):
        self.base_url = base_url
        self.api_key = api_key
        self.version = version

    def make_url(self, path):
        return "%s/api/%s/%s" % (self.base_url.rstrip("/"), self.version, path.lstrip("/"))

    def _get(self, url):
        full_url = self.make_url(url)
        headers = self.get_headers()
        return requests.get(full_url, headers=headers)

    def _post(self, url, data, content_type="application/json"):
        full_url = self.make_url(url)
        headers = self.get_headers()
        if content_type:
            headers["Content-Type"] = content_type
        return requests.post(full_url, data=data, headers=headers)

    def _put(self, url, data, content_type="application/json"):
        full_url = self.make_url(url)
        headers = self.get_headers()
        if content_type:
            headers["Content-Type"] = content_type
        return requests.put(full_url, data=data, headers=headers)

    def _delete(self, url):
        full_url = self.make_url(url)
        headers = self.get_headers()
        return requests.delete(full_url, headers=headers)

    def get_headers(self):
        headers = {}
        headers["Authorization"] = "ApiKey %s" % self.api_key
        return headers

    def add_feature(self, name, **kwargs):
        params = {"name": name}
        if "permission_type" in kwargs:
            params["permission_type"] = kwargs["permission_type"]
        if "boolean_permission" in kwargs:
            params["boolean_permission"] = kwargs["boolean_permission"]
        if "limit_permission" in kwargs:
            params["limit_permission"] = kwargs["limit_permission"]
        if "permission_level" in kwargs:
            params["permission_level"] = kwargs["permission_level"]

        resp = self._post("/feature/", json.dumps(params))

        if resp.status_code not in (200, 201):
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def update_feature(self, name, **kwargs):
        params = {}
        if "permission_type" in kwargs:
            params["permission_type"] = kwargs["permission_type"]
        if "boolean_permission" in kwargs:
            params["boolean_permission"] = kwargs["boolean_permission"]
        if "limit_permission" in kwargs:
            params["limit_permission"] = kwargs["limit_permission"]
        if "permission_level" in kwargs:
            params["permission_level"] = kwargs["permission_level"]

        resp = self._put("/feature/%s/" % name, json.dumps(params))

        if resp.status_code not in (200, 201):
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def get_feature(self, name):
        resp = self._get("/feature/%s" % name)

        if resp.status_code != 200:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def list_features(self):
        resp = self._get("/feature/")

        if resp.status_code != 200:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def delete_feature(self, name):
        resp = self._delete("/feature/%s" % name)

        if resp.status_code != 204:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        return True

    def add_qualifier(self, name):
        params = {"name": name}

        resp = self._post("/qualifier/", json.dumps(params))

        if resp.status_code not in (200, 201):
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def get_qualifier(self, name):
        resp = self._get("/qualifier/%s" % name)

        if resp.status_code != 200:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def list_qualifiers(self):
        resp = self._get("/qualifier/")

        if resp.status_code != 200:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def delete_qualifier(self, name):
        resp = self._delete("/qualifier/%s" % name)

        if resp.status_code != 204:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        return True

    def set_permissions(self, permissions):
        params = {"permissions": permissions}
        resp = self._post("/permissions/", json.dumps(params))

        if resp.status_code != 201:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)["permissions"]
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))

    def get_permissions(self, qualifier=None):
        params = {}
        if qualifier:
            params["qualifier"] = qualifier
        resp = self._get("/permissions/?" + urllib.urlencode(params))

        if resp.status_code != 200:
            raise UnexpectedStatusCode("Unexpected status code %s" % resp.status_code)

        try:
            return json.loads(resp.content)["permissions"]
        except ValueError as e:
            raise ValueError("%s. status: %s / content: %s" % (e, resp.status_code, resp.content))


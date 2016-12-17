#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

def get(url, params=None, **kwargs):
    return requests.request('get', url, params=params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    """Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return requests.request('post', url, data=data, json=json, **kwargs)

__all__ = ["get","post"]

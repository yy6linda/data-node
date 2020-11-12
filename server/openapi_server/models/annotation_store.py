# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AnnotationStore(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None):  # noqa: E501
        """AnnotationStore - a model defined in OpenAPI

        :param name: The name of this AnnotationStore.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'AnnotationStore':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnnotationStore of this AnnotationStore.  # noqa: E501
        :rtype: AnnotationStore
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this AnnotationStore.

        Resource name of the annotation store, of the form datasets/{datasetId}/annotationStore/{annotationStoreId}  # noqa: E501

        :return: The name of this AnnotationStore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnnotationStore.

        Resource name of the annotation store, of the form datasets/{datasetId}/annotationStore/{annotationStoreId}  # noqa: E501

        :param name: The name of this AnnotationStore.
        :type name: str
        """

        self._name = name

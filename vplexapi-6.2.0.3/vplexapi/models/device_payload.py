# coding: utf-8

"""
    VPlex REST API

    A defnition for the next-gen VPlex API  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DevicePayload(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'secondary_legs': 'list[str]',
        'geometry': 'str',
        'primary_leg': 'str',
        'stripe_depth': 'str'
    }

    attribute_map = {
        'name': 'name',
        'secondary_legs': 'secondary_legs',
        'geometry': 'geometry',
        'primary_leg': 'primary_leg',
        'stripe_depth': 'stripe_depth'
    }

    def __init__(self, name=None, secondary_legs=None, geometry=None, primary_leg=None, stripe_depth=None):  # noqa: E501
        """DevicePayload - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._secondary_legs = None
        self._geometry = None
        self._primary_leg = None
        self._stripe_depth = None
        self.discriminator = None

        self.name = name
        if secondary_legs is not None:
            self.secondary_legs = secondary_legs
        self.geometry = geometry
        self.primary_leg = primary_leg
        if stripe_depth is not None:
            self.stripe_depth = stripe_depth

    @property
    def name(self):
        """Gets the name of this DevicePayload.  # noqa: E501


        :return: The name of this DevicePayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DevicePayload.


        :param name: The name of this DevicePayload.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def secondary_legs(self):
        """Gets the secondary_legs of this DevicePayload.  # noqa: E501


        :return: The secondary_legs of this DevicePayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._secondary_legs

    @secondary_legs.setter
    def secondary_legs(self, secondary_legs):
        """Sets the secondary_legs of this DevicePayload.


        :param secondary_legs: The secondary_legs of this DevicePayload.  # noqa: E501
        :type: list[str]
        """

        self._secondary_legs = secondary_legs

    @property
    def geometry(self):
        """Gets the geometry of this DevicePayload.  # noqa: E501

        Geometry for the new device. Valid values are raid-0, raid-1, or raid-c.  # noqa: E501

        :return: The geometry of this DevicePayload.  # noqa: E501
        :rtype: str
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this DevicePayload.

        Geometry for the new device. Valid values are raid-0, raid-1, or raid-c.  # noqa: E501

        :param geometry: The geometry of this DevicePayload.  # noqa: E501
        :type: str
        """
        if geometry is None:
            raise ValueError("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

    @property
    def primary_leg(self):
        """Gets the primary_leg of this DevicePayload.  # noqa: E501


        :return: The primary_leg of this DevicePayload.  # noqa: E501
        :rtype: str
        """
        return self._primary_leg

    @primary_leg.setter
    def primary_leg(self, primary_leg):
        """Sets the primary_leg of this DevicePayload.


        :param primary_leg: The primary_leg of this DevicePayload.  # noqa: E501
        :type: str
        """
        if primary_leg is None:
            raise ValueError("Invalid value for `primary_leg`, must not be `None`")  # noqa: E501

        self._primary_leg = primary_leg

    @property
    def stripe_depth(self):
        """Gets the stripe_depth of this DevicePayload.  # noqa: E501

        Required only if geometry is raid-0.  # noqa: E501

        :return: The stripe_depth of this DevicePayload.  # noqa: E501
        :rtype: str
        """
        return self._stripe_depth

    @stripe_depth.setter
    def stripe_depth(self, stripe_depth):
        """Sets the stripe_depth of this DevicePayload.

        Required only if geometry is raid-0.  # noqa: E501

        :param stripe_depth: The stripe_depth of this DevicePayload.  # noqa: E501
        :type: str
        """

        self._stripe_depth = stripe_depth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DevicePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class SystemAlert(object):
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
        'additional_data': 'str',
        'component': 'str',
        'condition_id': 'str',
        'corrective_action': 'str',
        'created': 'datetime',
        'description': 'str',
        'enabled': 'bool',
        'event_source': 'str',
        'event_source_id': 'str',
        'external_rca': 'str',
        'id': 'int',
        'last_modified': 'datetime',
        'message': 'str',
        'name': 'str',
        'resource': 'str',
        'scope': 'str',
        'severity': 'str',
        'state': 'str'
    }

    attribute_map = {
        'additional_data': 'additionalData',
        'component': 'component',
        'condition_id': 'conditionId',
        'corrective_action': 'correctiveAction',
        'created': 'created',
        'description': 'description',
        'enabled': 'enabled',
        'event_source': 'eventSource',
        'event_source_id': 'eventSourceId',
        'external_rca': 'externalRCA',
        'id': 'id',
        'last_modified': 'lastModified',
        'message': 'message',
        'name': 'name',
        'resource': 'resource',
        'scope': 'scope',
        'severity': 'severity',
        'state': 'state'
    }

    def __init__(self, additional_data=None, component=None, condition_id=None, corrective_action=None, created=None, description=None, enabled=None, event_source=None, event_source_id=None, external_rca=None, id=None, last_modified=None, message=None, name=None, resource=None, scope=None, severity=None, state=None):  # noqa: E501
        """SystemAlert - a model defined in Swagger"""  # noqa: E501

        self._additional_data = None
        self._component = None
        self._condition_id = None
        self._corrective_action = None
        self._created = None
        self._description = None
        self._enabled = None
        self._event_source = None
        self._event_source_id = None
        self._external_rca = None
        self._id = None
        self._last_modified = None
        self._message = None
        self._name = None
        self._resource = None
        self._scope = None
        self._severity = None
        self._state = None
        self.discriminator = None

        if additional_data is not None:
            self.additional_data = additional_data
        if component is not None:
            self.component = component
        if condition_id is not None:
            self.condition_id = condition_id
        if corrective_action is not None:
            self.corrective_action = corrective_action
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if event_source is not None:
            self.event_source = event_source
        if event_source_id is not None:
            self.event_source_id = event_source_id
        if external_rca is not None:
            self.external_rca = external_rca
        if id is not None:
            self.id = id
        if last_modified is not None:
            self.last_modified = last_modified
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if resource is not None:
            self.resource = resource
        if scope is not None:
            self.scope = scope
        if severity is not None:
            self.severity = severity
        if state is not None:
            self.state = state

    @property
    def additional_data(self):
        """Gets the additional_data of this SystemAlert.  # noqa: E501


        :return: The additional_data of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this SystemAlert.


        :param additional_data: The additional_data of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._additional_data = additional_data

    @property
    def component(self):
        """Gets the component of this SystemAlert.  # noqa: E501


        :return: The component of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this SystemAlert.


        :param component: The component of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def condition_id(self):
        """Gets the condition_id of this SystemAlert.  # noqa: E501


        :return: The condition_id of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        """Sets the condition_id of this SystemAlert.


        :param condition_id: The condition_id of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._condition_id = condition_id

    @property
    def corrective_action(self):
        """Gets the corrective_action of this SystemAlert.  # noqa: E501


        :return: The corrective_action of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._corrective_action

    @corrective_action.setter
    def corrective_action(self, corrective_action):
        """Sets the corrective_action of this SystemAlert.


        :param corrective_action: The corrective_action of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._corrective_action = corrective_action

    @property
    def created(self):
        """Gets the created of this SystemAlert.  # noqa: E501

        Creation date of Sytem Alert  # noqa: E501

        :return: The created of this SystemAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SystemAlert.

        Creation date of Sytem Alert  # noqa: E501

        :param created: The created of this SystemAlert.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this SystemAlert.  # noqa: E501

        Description of Sytem Alert  # noqa: E501

        :return: The description of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemAlert.

        Description of Sytem Alert  # noqa: E501

        :param description: The description of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this SystemAlert.  # noqa: E501


        :return: The enabled of this SystemAlert.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SystemAlert.


        :param enabled: The enabled of this SystemAlert.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def event_source(self):
        """Gets the event_source of this SystemAlert.  # noqa: E501


        :return: The event_source of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this SystemAlert.


        :param event_source: The event_source of this SystemAlert.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEM", "DEVICE", "VIRTUALVOLUME", "EXTENT", "CLUSTER", "STORAGEVOLUME", "STORAGEARRAY", "LOGICALUNIT", "DIRECTOR", "SYSTEMVOLUME", "CONSISTENCYGROUP", "STORAGEVIEW", "LOGGINGVOLUME", "UNKNOWN"]  # noqa: E501
        if event_source not in allowed_values:
            raise ValueError(
                "Invalid value for `event_source` ({0}), must be one of {1}"  # noqa: E501
                .format(event_source, allowed_values)
            )

        self._event_source = event_source

    @property
    def event_source_id(self):
        """Gets the event_source_id of this SystemAlert.  # noqa: E501


        :return: The event_source_id of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        """Sets the event_source_id of this SystemAlert.


        :param event_source_id: The event_source_id of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._event_source_id = event_source_id

    @property
    def external_rca(self):
        """Gets the external_rca of this SystemAlert.  # noqa: E501


        :return: The external_rca of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._external_rca

    @external_rca.setter
    def external_rca(self, external_rca):
        """Sets the external_rca of this SystemAlert.


        :param external_rca: The external_rca of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._external_rca = external_rca

    @property
    def id(self):
        """Gets the id of this SystemAlert.  # noqa: E501

        The unique ID of the system alert  # noqa: E501

        :return: The id of this SystemAlert.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SystemAlert.

        The unique ID of the system alert  # noqa: E501

        :param id: The id of this SystemAlert.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_modified(self):
        """Gets the last_modified of this SystemAlert.  # noqa: E501


        :return: The last_modified of this SystemAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this SystemAlert.


        :param last_modified: The last_modified of this SystemAlert.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def message(self):
        """Gets the message of this SystemAlert.  # noqa: E501


        :return: The message of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SystemAlert.


        :param message: The message of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this SystemAlert.  # noqa: E501


        :return: The name of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemAlert.


        :param name: The name of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource(self):
        """Gets the resource of this SystemAlert.  # noqa: E501

        Resource that generated the alert  # noqa: E501

        :return: The resource of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this SystemAlert.

        Resource that generated the alert  # noqa: E501

        :param resource: The resource of this SystemAlert.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def scope(self):
        """Gets the scope of this SystemAlert.  # noqa: E501


        :return: The scope of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SystemAlert.


        :param scope: The scope of this SystemAlert.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER", "DIRECTOR", "MANAGEMENTSERVER", "UNKNOWN"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def severity(self):
        """Gets the severity of this SystemAlert.  # noqa: E501


        :return: The severity of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this SystemAlert.


        :param severity: The severity of this SystemAlert.  # noqa: E501
        :type: str
        """
        allowed_values = ["CRITICAL", "ERROR", "WARNING", "INFO", "CLEAR", "UNKNOWN"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def state(self):
        """Gets the state of this SystemAlert.  # noqa: E501


        :return: The state of this SystemAlert.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SystemAlert.


        :param state: The state of this SystemAlert.  # noqa: E501
        :type: str
        """
        allowed_values = ["OPEN", "CLOSE", "ACK", "UNKNOWN"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, SystemAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

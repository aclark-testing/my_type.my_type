from zope.interface import Interface
from zope.schema import TextLine
from zope.configuration.fields import GlobalInterface, GlobalObject

# -*- extra stuff goes here -*-

class IMydirectiveDirective(Interface):
    """
    Defines a schema for mydirective directive
    (The attributes are given as example)
    """

    name = TextLine(
        title=u"Name",
        description=u"The name of the mydirective directive.",
        required=True
        )

    for_ = GlobalInterface(
        title=u"interface",
        description=u"""Specifies the interface for which the directive is
        registered.""",
        required=True
        )

    factory = GlobalObject(
        title=u"hander",
        description=u"The factory",
        required=True
        )

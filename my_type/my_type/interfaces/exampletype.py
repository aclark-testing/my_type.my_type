from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from my_type.my_type import my_typeMessageFactory as _



class IExampleType(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    newfield = schema.TextLine(
        title=_(u"New Field"),
        required=False,
        description=_(u"Field description"),
    )
#

"""Definition of the Example Type content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from my_type.my_type import my_typeMessageFactory as _

from my_type.my_type.interfaces import IExampleType
from my_type.my_type.config import PROJECTNAME

ExampleTypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        'newfield',
        storage=atapi.AnnotationStorage(),
        widget=atapi.LinesWidget(
            label=_(u"New Field"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'newfield',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"New Field"),
            description=_(u"Field description"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ExampleTypeSchema['title'].storage = atapi.AnnotationStorage()
ExampleTypeSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ExampleTypeSchema, moveDiscussion=False)


class ExampleType(base.ATCTContent):
    """Description of the Example Type"""
    implements(IExampleType)

    meta_type = "ExampleType"
    schema = ExampleTypeSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    newlinesfield = atapi.ATFieldProperty('newlinesfield')

    newfield = atapi.ATFieldProperty('newfield')


atapi.registerType(ExampleType, PROJECTNAME)

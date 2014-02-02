from zope import interface, schema
from zope.formlib import form
from Products.Five.formlib import formbase
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from my_type.my_type import my_typeMessageFactory as _

class IExampleFormSchema(interface.Interface):
    # -*- extra stuff goes here -*-

    examplefield = schema.TextLine(
        title=u'A short summary or label',
        description=u'',
        required=False,
        readonly=False,
        default=None,
        )


class ExampleForm(formbase.PageForm):
    form_fields = form.FormFields(IExampleFormSchema)
    label = _(u'Example Form')
    description = _(u'')

    @form.action('Submit')
    def actionSubmit(self, action, data):
        pass
        # Put the action handler code here 




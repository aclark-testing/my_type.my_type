from zope.app.component.metaconfigure import handler
from zope.app.component.interface import provideInterface
from zope.configuration.exceptions import ConfigurationError

# -*- extra stuff goes here -*-

def MydirectiveDirective(_context, name=None, for_=None, factory=None):
    """
    register the mydirective directive
    """
    if name is None or for_ is None or factory is None:
        raise ConfigurationError(
         "You must specify the 'name', the 'for' and the 'factory' attributes.")

    # # the following is just an example
    # _context.action(
    #                  discriminator = ('Mydirective', name),
    #                  callable = handler,
    #                  args = ('provideAdapter', (for_,),
    #                          IExampleInterface, name, factory, _context.info)
    #                )
    # for_ = tuple(for_)
    # for iface in for_:
    #     if iface is not None:
    #         _context.action( discriminator = None,
    #                          callable = provideInterface,
    #                          args = ('', iface)
    #                        )

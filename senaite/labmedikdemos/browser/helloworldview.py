from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from senaite.labmedikdemos import labmedikdemosMessageFactory as _


class IHelloWorldView(Interface):
    """
    HelloWorld view interface
    """

    def test():
        """ test method"""


class HelloWorldView(BrowserView):
    """
    HelloWorld browser view
    """
    implements(IHelloWorldView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        message = _(u'Hello world,')
        company = _(u'Plone Foundation!!!')

        return {'message': message, 'company': company,}

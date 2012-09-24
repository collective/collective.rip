from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate
try:
    # >= Plone 4.3
    from zope.component.hooks import getSite
except:
    # < Plone 4.3
    from zope.app.component.hooks import getSite


default_css = """
#portal-globalnav {
  padding: 0 0 0 2em;
  border-radius: 5px;
}
#portal-globalnav li a {
  margin: 0;
  padding: 5px;
  height: 50px;
}
"""

default_js = """
jq(function(){
  $("h1").animate({
    width: "70%",
    opacity: 0.4,
    marginLeft: "0.6in",
    fontSize: "3em",
    borderWidth: "10px"
  }, 1500 );
});
"""


class ResourcesInPlone(BrowserView):

    template = ViewPageTemplateFile('rip.pt')

    def __init__(self, context, request):

        self.context = context
        self.request = request

        self.default_css = default_css
        self.default_js = default_js
        self.custom_css = 'rip.css'
        self.custom_js = 'rip.js'

        self.plonesite = getSite()
        self.portal_skins = self.plonesite.portal_skins
        self.portal_css = self.plonesite.portal_css
        self.portal_js = self.plonesite.portal_javascripts

    def __call__(self):
        """
        Manage "static" resources in Plone
        """
        form = self.request.form

        # Enable/disable CSS debug
        if 'submitted_css' in form:
            if 'css_debug' in form:
                self.portal_css.setDebugMode(True)
            if not 'css_debug' in form:
                self.portal_css.setDebugMode(False)

        # Enable/disable JS debug
        if 'submitted_js' in form:
            if 'js_debug' in form:
                self.portal_js.setDebugMode(True)
            if not 'js_debug' in form:
                self.portal_js.setDebugMode(False)

        # Edit CSS/JS
        if 'edit_css' in form and 'submitted_css' in form:
            text = form['edit_css']
            self.setPloneCustom(self.portal_css, text)
        if 'edit_js' in form and 'submitted_js' in form:
            text = form['edit_js']
            self.setPloneCustom(self.portal_js, text)

        return self.template()

    def getDebugMode(self, value):
        """
        Called from rip.pt
        """
        tool = getToolByName(self.plonesite, value)
        status = tool.getDebugMode()
        return status

    def getCustomObjectAndMethods(self, tool):
        """
        Based on the tool, return custom object and methods to update resources
        """
        if tool.getId() == 'portal_css':
            custom_id = self.custom_css
            default_text = self.default_css
            try:
                obj = self.portal_skins.custom[custom_id]
            except:
                self.create_custom(custom_id, default_text)
                obj = self.portal_skins.custom[custom_id]
            register = self.portal_css.registerStylesheet
            update = self.portal_css.updateStylesheet
            default_text = self.default_css
        elif tool.getId() == 'portal_javascripts':
            custom_id = self.custom_js
            default_text = self.default_js
            try:
                obj = self.portal_skins.custom[custom_id]
            except:
                self.create_custom(custom_id, default_text)
                obj = self.portal_skins.custom[custom_id]
            register = self.portal_js.registerScript
            update = self.portal_js.updateScript
            default_text = self.default_js
        else:
            raise Exception("Unable to traverse to custom object in skins!")

        return custom_id, obj, register, update, default_text

    def setPloneCustom(self, tool, text):
        """
        Look for a ZPT obj to update
        """
        custom_id, obj, register, update, default_text = (
            self.getCustomObjectAndMethods(tool))
        if hasattr(obj, 'pt_edit'):
            # ZopePageTemplate
            obj.pt_edit(text, 'text/html')
        else:
            raise Exception("Unable to update object: %s." % repr(obj))
        self.updatePloneCustom(tool, custom_id, obj, register, update)

    def updatePloneCustom(self, tool, custom_id, obj, register, update):
        resource_ids = tool.getResourceIds()
        if custom_id not in resource_ids:
            register(id=custom_id, enabled=True)
        else:
            update(id=custom_id, enabled=True)
        tool.cookResources()

    def create_custom(self, custom_id, default_text):
        text = default_text
        content_type = 'text/html'
        obj = ZopePageTemplate(custom_id, text, content_type)
        self.portal_skins.custom._setObject(custom_id, obj)

    def getPloneCustom(self, tool):
        custom_id, obj, register, update, default_text = (
            self.getCustomObjectAndMethods(tool))
        if custom_id in self.portal_skins.custom.objectIds():
            try:
                document_src = self.portal_skins.custom[custom_id].document_src()
            except:
                raise Exception("Unable to get source of: %s" % repr(obj))
        else:
            self.create_custom(custom_id, default_text)
            document_src = self.portal_skins.custom[custom_id].document_src()
        return document_src

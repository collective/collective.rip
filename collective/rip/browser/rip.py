from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate

default_css = """
/* DELETE THIS LINE AND PUT YOUR CUSTOM STUFF HERE. E.g.
body{background:black;}
*/
"""

default_js = """
/* DELETE THIS LINE AND PUT YOUR CUSTOM STUFF HERE. E.g.
jq(function () { jq("h1").hide("slow"); } );
*/
"""

class EditCSS(BrowserView):

    template = ViewPageTemplateFile('edit_css.pt')
    default_css = default_css
    default_js = default_js
    custom_css = 'ploneCustom.css'
    custom_js = 'ploneCustom.js'

    def __call__(self, *args, **kw):
        request = self.context.request
        form = request.form

        # XXX Replace this with Zope 2 form processing
        # http://docs.zope.org/zope2/zope2book/ScriptingZope.html#passing-parameters-to-scripts

        contains = form.__contains__

        if contains('edit_css') and contains('submit'):
            if form['submit'] == 'Save':
                self.setPloneCustomCSS(form['edit_css'])

        if contains('edit_js') and contains('submit'):
            if form['submit'] == 'Save':
                self.setPloneCustomJS(form['edit_js'])

        if contains('toggle_css_debug') and contains('submit'):
            if form['toggle_css_debug'] == 'on' and form['submit'] == 'Save':
                self.setDebugModeCSS(True)

        if not contains('toggle_css_debug') and contains('submit'):
            if form['submit'] == 'Save':
                self.setDebugModeCSS(False)

        if contains('toggle_js_debug') and contains('submit'):
            if form['toggle_js_debug'] == 'on' and form['submit'] == 'Save':
                self.setDebugModeJS(True)

        if not contains('toggle_js_debug') and contains('submit'):
            if form['submit'] == 'Save':
                self.setDebugModeJS(False)

        return self.template()

    def getPloneCustomCSS(self):
        site = getSite()
        skins = site.portal_skins
        if self.custom_css in skins.custom.objectIds():
            try:
                return skins.custom[self.custom_css].document_src()
            except:
                raise Exception("It's not possible to manage the object %s. "
                    "Use '%s' instead." % (repr(skins.custom[self.custom_css]),
                    "ZopePageTemplate"))
        else:
            id = self.custom_css
            text = self.default_css
            content_type = 'text/html'
            obj = ZopePageTemplate(id, text, content_type)
            skins.custom._setObject(id, obj)
            return skins.custom[self.custom_css].document_src()

    def getPloneCustomJS(self):
        site = getSite()
        skins = site.portal_skins
        if self.custom_js in skins.custom.objectIds():
            try:
                return skins.custom[self.custom_js].document_src()
            except:
                raise Exception("It's not possible to manage the object %s. "
                    "Use '%s' instead." % (repr(skins.custom[self.custom_js]),
                    "ZopePageTemplate"))
        else:
            id = self.custom_js
            text = self.default_js
            content_type = 'text/html'
            obj = ZopePageTemplate(id, text, content_type)
            skins.custom._setObject(id, obj)
            return skins.custom[self.custom_js].document_src()

    def setPloneCustomCSS(self, text):
        site = getSite()
        skins = site.portal_skins
        obj = skins.custom[self.custom_css]
        try:
            if hasattr(obj, 'manage_edit'):
                # DTMLMethod
                obj.manage_edit(text, 'text/html')
            else:
                # ZopePageTemplate
                obj.pt_edit(text, 'text/html')
        except:
            raise Exception("It's not possible to update object %s. "
                "Use '%s' instead." % (repr(obj), "ZopePageTemplate"))
        self.updatePloneCustomCSS()

    def setPloneCustomJS(self, text):
        site = getSite()
        skins = site.portal_skins
        obj = skins.custom[self.custom_js]
        try:
            if hasattr(obj, 'manage_edit'):
                # DTMLMethod
                obj.manage_edit(text, 'text/html')
            else:
                # ZopePageTemplate
                obj.pt_edit(text, 'text/html')
        except:
            raise Exception("It's not possible to update object %s. "
                "Use '%s' instead." % (repr(obj), "ZopePageTemplate"))
        self.updatePloneCustomJS()

    def updatePloneCustomCSS(self):
        site = getSite()
        cssreg = getToolByName(site, 'portal_css', None)
        if cssreg is not None:
            stylesheet_ids = cssreg.getResourceIds()
            if self.custom_css not in stylesheet_ids:
#y               cssreg.registerStylesheet(id=sheetId, enabled=True)
                cssreg.registerStylesheet(id=self.custom_css, enabled=True)
                cssreg.cookResources()
            else:
                cssreg.updateStylesheet(self.custom_css, enabled=True)
                cssreg.cookResources()

    def updatePloneCustomJS(self):
        site = getSite()
        jsreg = getToolByName(site, 'portal_javascripts', None)
        if jsreg is not None:
            script_ids = jsreg.getResourceIds()
            if self.custom_js not in script_ids:
                jsreg.registerScript(id=self.custom_js, enabled=True)
                jsreg.cookResources()
            else:
                jsreg.updateScript(self.custom_js, enabled=True)
                jsreg.cookResources()

    def getDebugModeCSS(self):
        site = getSite() 
        css_tool = getToolByName(site, 'portal_css') 
        return css_tool.getDebugMode()

    def getDebugModeJS(self):
        site = getSite()
        js_tool = getToolByName(site, 'portal_javascripts')
        return js_tool.getDebugMode()

    def setDebugModeCSS(self, value):
        site = getSite() 
        css_tool = getToolByName(site, 'portal_css') 
        css_tool.setDebugMode(value)

    def setDebugModeJS(self, value):
        site = getSite()
        js_tool = getToolByName(site, 'portal_javascripts')
        js_tool.setDebugMode(value)

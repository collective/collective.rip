*Formerly collective.controlpanel.edit_css*

Introduction
============

collective.rip: (**r**)esources (**i**)n (**p**)lone is for quick and dirty UI prototyping. Install this add-on to edit CSS and JavaScript from within the Plone control panel. You may also toggle CSS and JavaScript debug modes.

Installation
------------

To install:

- Add ``collective.rip`` to your buildout ``plone.recipe.zope2instance``
  section's eggs parameter::

    [plone]
    recipe = plone.recipe.zope2instance
    ...
    eggs =
        ...
        collective.rip

- Run ``Buildout`` and restart ``Plone``.
- Browse to ``Site Setup -> Add-ons -> Available add-ons``.
- Check ``Resources in Plone`` and click ``Activate``.

Have fun!

Questions/comments/concerns? E-mail: aclark@aclark.net


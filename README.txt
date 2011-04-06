
Introduction
============

This is ``collective.rip`` AKA "Resources In Plone".

For quick and dirty UI prototyping: install this add-on to edit CSS and 
Javascript from within Plone (in the Plone control panel). You can also 
toggle CSS/JS debug modes.

Installation
------------

To install: 

- Add ``collective.rip`` to your buildout ``plone.recipe.zope2instance``
  section's eggs parameter, e.g.::

    [plone]
    recipe = plone.recipe.zope2instance
    ...
    eggs = 
        ...
        collective.rip

- Run buildout and restart Plone.

- Browse to Site Setup -> Add-ons -> Available add-ons -> [] Resources in Plone

- Check the box next to ``Resources in Plone`` and click the Activate button.

Have fun!

Questions/comments/concerns? E-mail: aclark@aclark.net


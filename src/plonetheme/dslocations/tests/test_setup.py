# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plonetheme.dslocations.testing import PLONETHEME_DSLOCATIONS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.dslocations is properly installed."""

    layer = PLONETHEME_DSLOCATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.dslocations is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.dslocations'))

    def test_browserlayer(self):
        """Test that IPlonethemeDslocationsLayer is registered."""
        from plonetheme.dslocations.interfaces import (
            IPlonethemeDslocationsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPlonethemeDslocationsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_DSLOCATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plonetheme.dslocations'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonetheme.dslocations is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.dslocations'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeDslocationsLayer is removed."""
        from plonetheme.dslocations.interfaces import \
            IPlonethemeDslocationsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPlonethemeDslocationsLayer,
            utils.registered_layers())

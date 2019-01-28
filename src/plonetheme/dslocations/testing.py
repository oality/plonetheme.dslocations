# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.dslocations


class PlonethemeDslocationsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.dslocations)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.dslocations:default')


PLONETHEME_DSLOCATIONS_FIXTURE = PlonethemeDslocationsLayer()


PLONETHEME_DSLOCATIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_DSLOCATIONS_FIXTURE,),
    name='PlonethemeDslocationsLayer:IntegrationTesting',
)


PLONETHEME_DSLOCATIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_DSLOCATIONS_FIXTURE,),
    name='PlonethemeDslocationsLayer:FunctionalTesting',
)


PLONETHEME_DSLOCATIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_DSLOCATIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeDslocationsLayer:AcceptanceTesting',
)

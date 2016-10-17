import os, fnmatch, logging
from charmhelpers.core import templating, hookenv, host
from charms.reactive import hook, when, when_all, when_any, when_not, when_none, set_state, remove_state


@when('apache.available')
def setup_ifest_ui():
	set_state('apache.start')
	hookenv.status_set('maintenance', 'Starting Apache')

@when('apache.started')
def started():
	hookenv.status_set('active', 'Ready')

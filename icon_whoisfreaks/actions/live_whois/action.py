import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import LiveWhoisInput, LiveWhoisOutput, Input, Output, Component

# Custom imports below


class LiveWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="live_whois", description=Component.DESCRIPTION, input=LiveWhoisInput(), output=LiveWhoisOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domainname = params.get(Input.DOMAINNAME)
        format = params.get(Input.FORMAT)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

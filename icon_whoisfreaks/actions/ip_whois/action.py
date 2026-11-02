import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpWhoisInput, IpWhoisOutput, Input, Output, Component

# Custom imports below


class IpWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_whois", description=Component.DESCRIPTION, input=IpWhoisInput(), output=IpWhoisOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        format = params.get(Input.FORMAT)
        ip = params.get(Input.IP)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

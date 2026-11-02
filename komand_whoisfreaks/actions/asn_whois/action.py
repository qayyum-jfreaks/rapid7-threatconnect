import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import AsnWhoisInput, AsnWhoisOutput, Input, Output, Component

# Custom imports below


class AsnWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="asn_whois", description=Component.DESCRIPTION, input=AsnWhoisInput(), output=AsnWhoisOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        asn = params.get(Input.ASN)
        format = params.get(Input.FORMAT)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DnsLookupInput, DnsLookupOutput, Input, Output, Component

# Custom imports below


class DnsLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="dns_lookup", description=Component.DESCRIPTION, input=DnsLookupInput(), output=DnsLookupOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domainname = params.get(Input.DOMAINNAME)
        format = params.get(Input.FORMAT)
        ipaddress = params.get(Input.IPADDRESS)
        type = params.get(Input.TYPE)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

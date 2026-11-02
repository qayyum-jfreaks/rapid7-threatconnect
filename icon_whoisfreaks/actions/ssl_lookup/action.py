import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SslLookupInput, SslLookupOutput, Input, Output, Component

# Custom imports below


class SslLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ssl_lookup", description=Component.DESCRIPTION, input=SslLookupInput(), output=SslLookupOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        chain = params.get(Input.CHAIN)
        domainname = params.get(Input.DOMAINNAME)
        format = params.get(Input.FORMAT)
        sslraw = params.get(Input.SSLRAW)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

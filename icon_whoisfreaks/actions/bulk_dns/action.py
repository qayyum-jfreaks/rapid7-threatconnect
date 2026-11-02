import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkDnsInput, BulkDnsOutput, Input, Output, Component

# Custom imports below


class BulkDns(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_dns", description=Component.DESCRIPTION, input=BulkDnsInput(), output=BulkDnsOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        format = params.get(Input.FORMAT)
        type = params.get(Input.TYPE)
        values = params.get(Input.VALUES)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

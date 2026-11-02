import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ReverseDnsInput, ReverseDnsOutput, Input, Output, Component

# Custom imports below


class ReverseDns(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_dns", description=Component.DESCRIPTION, input=ReverseDnsInput(), output=ReverseDnsOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        exact = params.get(Input.EXACT)
        format = params.get(Input.FORMAT)
        page = params.get(Input.PAGE)
        type = params.get(Input.TYPE)
        value = params.get(Input.VALUE)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

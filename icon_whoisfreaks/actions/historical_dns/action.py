import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import HistoricalDnsInput, HistoricalDnsOutput, Input, Output, Component

# Custom imports below


class HistoricalDns(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="historical_dns",
            description=Component.DESCRIPTION,
            input=HistoricalDnsInput(),
            output=HistoricalDnsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domainname = params.get(Input.DOMAINNAME)
        format = params.get(Input.FORMAT)
        page = params.get(Input.PAGE)
        type = params.get(Input.TYPE)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

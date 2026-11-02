import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import HistoricalWhoisInput, HistoricalWhoisOutput, Input, Output, Component

# Custom imports below


class HistoricalWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="historical_whois",
            description=Component.DESCRIPTION,
            input=HistoricalWhoisInput(),
            output=HistoricalWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domainname = params.get(Input.DOMAINNAME)
        format = params.get(Input.FORMAT)
        page = params.get(Input.PAGE)
        whois = params.get(Input.WHOIS)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

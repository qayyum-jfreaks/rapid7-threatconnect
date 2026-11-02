import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ReverseWhoisInput, ReverseWhoisOutput, Input, Output, Component

# Custom imports below


class ReverseWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_whois",
            description=Component.DESCRIPTION,
            input=ReverseWhoisInput(),
            output=ReverseWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        company = params.get(Input.COMPANY)
        email = params.get(Input.EMAIL)
        exact = params.get(Input.EXACT)
        format = params.get(Input.FORMAT)
        keyword = params.get(Input.KEYWORD)
        mode = params.get(Input.MODE)
        owner = params.get(Input.OWNER)
        page = params.get(Input.PAGE)
        whois = params.get(Input.WHOIS)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

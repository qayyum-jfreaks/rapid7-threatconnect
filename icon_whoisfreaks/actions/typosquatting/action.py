import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import TyposquattingInput, TyposquattingOutput, Input, Output, Component

# Custom imports below


class Typosquatting(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="typosquatting",
            description=Component.DESCRIPTION,
            input=TyposquattingInput(),
            output=TyposquattingOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        format = params.get(Input.FORMAT)
        keyword = params.get(Input.KEYWORD)
        page = params.get(Input.PAGE)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

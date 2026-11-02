import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SubdomainsInput, SubdomainsOutput, Input, Output, Component

# Custom imports below


class Subdomains(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="subdomains", description=Component.DESCRIPTION, input=SubdomainsInput(), output=SubdomainsOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        after = params.get(Input.AFTER)
        before = params.get(Input.BEFORE)
        domainname = params.get(Input.DOMAINNAME)
        format = params.get(Input.FORMAT)
        page = params.get(Input.PAGE)
        status = params.get(Input.STATUS)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DomainReputationInput, DomainReputationOutput, Input, Output, Component

# Custom imports below


class DomainReputation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_reputation",
            description=Component.DESCRIPTION,
            input=DomainReputationInput(),
            output=DomainReputationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domainname = params.get(Input.DOMAINNAME)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

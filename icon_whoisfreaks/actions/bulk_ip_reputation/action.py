import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkIpReputationInput, BulkIpReputationOutput, Input, Output, Component

# Custom imports below


class BulkIpReputation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_ip_reputation",
            description=Component.DESCRIPTION,
            input=BulkIpReputationInput(),
            output=BulkIpReputationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ips = params.get(Input.IPS)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

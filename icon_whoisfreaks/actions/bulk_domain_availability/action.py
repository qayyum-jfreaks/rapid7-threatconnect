import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkDomainAvailabilityInput, BulkDomainAvailabilityOutput, Input, Output, Component

# Custom imports below


class BulkDomainAvailability(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_domain_availability",
            description=Component.DESCRIPTION,
            input=BulkDomainAvailabilityInput(),
            output=BulkDomainAvailabilityOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domains = params.get(Input.DOMAINS)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

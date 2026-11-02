import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkIpSecurityInput, BulkIpSecurityOutput, Input, Output, Component

# Custom imports below


class BulkIpSecurity(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_ip_security",
            description=Component.DESCRIPTION,
            input=BulkIpSecurityInput(),
            output=BulkIpSecurityOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ips = params.get(Input.IPS)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RESPONSE: None,
        }

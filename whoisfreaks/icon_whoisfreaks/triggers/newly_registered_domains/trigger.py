import insightconnect_plugin_runtime
import time
from .schema import NewlyRegisteredDomainsInput, NewlyRegisteredDomainsOutput, Input, Output, Component

# Custom imports below


class NewlyRegisteredDomains(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="newly_registered_domains",
            description=Component.DESCRIPTION,
            input=NewlyRegisteredDomainsInput(),
            output=NewlyRegisteredDomainsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        batch_size = params.get(Input.BATCH_SIZE)
        date = params.get(Input.DATE)
        dedupe_window_days = params.get(Input.DEDUPE_WINDOW_DAYS)
        max_rows_per_run = params.get(Input.MAX_ROWS_PER_RUN)
        tld_family = params.get(Input.TLD_FAMILY)
        whois = params.get(Input.WHOIS)
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            # TODO: Implement trigger functionality
            self.send(
                {
                    Output.EVENTS: None,
                    Output.NEXT_OFFSET: None,
                }
            )
            time.sleep(5)

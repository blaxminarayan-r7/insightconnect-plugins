import komand
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException
from ipaddress import ip_network
from icon_fortinet_fortigate.util.util import Helpers


class DeleteAddressObject(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_address_object",
            description=Component.DESCRIPTION,
            input=DeleteAddressObjectInput(),
            output=DeleteAddressObjectOutput(),
        )

    def run(self, params={}):
        host = params[Input.ADDRESS_OBJECT]
        original_host = params[Input.ADDRESS_OBJECT]
        helper = Helpers(self.logger)

        # This will check if the host is an IP
        # If not it will check if the host ends with 2 chars. If this is true it is assumed to be a valid FQDN
        # Else it is assumed to be an invalid IP
        try:
            host = ip_network(host)
        except ValueError:
            if host[-1].isdigit() or host[-2].isdigit():
                raise PluginException(
                    cause="The host input appears to be an invalid IP or domain name.",
                    assistance="Ensure that the host input is valid IP address or domain.",
                    data=host,
                )
            pass

        is_ipv6 = self.connection.get_address_object(original_host)["name"] == "address6"

        if is_ipv6:
            params_payload = {"mkey": original_host}
            response = self.connection.call_api(method="DELETE", path=f"firewall/address6", params=params_payload)
        else:
            params_payload = {"mkey": str(host)}
            response = self.connection.call_api(method="DELETE", path=f"firewall/address", params=params_payload)

        try:
            json_response = response.json()
        except ValueError:
            raise PluginException(
                cause="Data sent by FortiGate was not in JSON format.\n",
                assistance="Contact support for help.",
                data=response.text,
            )
        helper.http_errors(json_response, response.status_code)

        return {Output.SUCCESS: True, Output.RESPONSE_OBJECT: json_response}

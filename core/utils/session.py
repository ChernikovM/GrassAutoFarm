

class BaseClient:
    devices_id_base = "22707469397757736452392d7763764422"
    server_constants = ["5b", "2c", "5d"]

    def __init__(self, user_agent: str, proxy: str = None, device_id_multiplier: int = 4):
        self.session = None
        self.ip = None
        self.username = None
        self.proxy = None

        self.device_id_multiplier = device_id_multiplier

        #self.device_id = BaseClient.server_constants[0]+(BaseClient.devices_id_base+BaseClient.server_constants[1])*self.device_id_multiplier+BaseClient.devices_id_base+BaseClient.server_constants[2]
        self.user_agent = user_agent
        self.proxy = proxy

        self.website_headers = {
            'authority': 'api.getgrass.io',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://app.getgrass.io',
            'referer': 'https://app.getgrass.io/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': self.user_agent,
        }
    
    def get_device_id(self, id: int):
        return BaseClient.server_constants[0]+(BaseClient.devices_id_base+BaseClient.server_constants[1])*id+BaseClient.devices_id_base+BaseClient.server_constants[2]
        
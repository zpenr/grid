class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            parts = ipaddress.split('.')
        elif isinstance(ipaddress, (list, tuple)):
            parts = ipaddress
        
        self.parts = []
        for part in parts:
            self.parts.append(str(part))
        self.ip_string = ".".join(self.parts)

    def __str__(self):
        return self.ip_string

    def __repr__(self):
        return f"IPAddress('{self.ip_string}')"
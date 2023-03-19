class PowerCable:
    def pling_in_power_cable(self):
        pass


class RCACable:
    def pling_in_rca_cable(self, device):
        pass


class HDMICable:
    def pling_in_hdmi_cable(self, device):
        pass


class EthernetCable:
    def pling_in_ethernet_cable(self, device):
        pass


class Television(HDMICable, RCACable, PowerCable):
    def connect_to_dvd(self, dvd_player):
        self.pling_in_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.pling_in_hdmi_cable(game_console)


class DVDPlayer(HDMICable, PowerCable):
    def connect_to_tv(self, television):
        self.pling_in_hdmi_cable(television)


class GameConsole(HDMICable, EthernetCable, PowerCable):
    def connect_to_tv(self, television):
        self.pling_in_hdmi_cable(television)

    def connect_to_router(self, router):
        self.pling_in_ethernet_cable(router)


class Router(EthernetCable, PowerCable):
    def connect_to_tv(self, television):
        self.pling_in_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.pling_in_ethernet_cable(game_console)

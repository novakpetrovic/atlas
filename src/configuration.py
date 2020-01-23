import configparser


class Configuration:
    def __init__(self, configuration_ini_file):
        self.config = configparser.ConfigParser(
                interpolation=configparser.ExtendedInterpolation())
        self.config.read(configuration_ini_file)
        self.cfg = self.config['USER']
        self.cfg_space = self.cfg['space'][1]
        self.cfg_active_task_prefixes = (
                self.cfg['active_task_prefixes'].split('\n'))
        self.cfg_portfolio_files = self.cfg['portfolio_files'].split('\n')
        self.cfg_tab_order = self.cfg['tab_order'].split('\n')
        if self.cfg['newline'] == 'linux':
            self.cfg_newline = '\n'
        else:
            self.cfg_newline = '\r\n'

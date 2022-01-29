from src.helpers.config.validate import ConfigValidation
from src.helpers.config.config_instance import ConfigInstance


class ConfigTimeIntervals(ConfigInstance):
    def __init__(self, values) -> None:
        validate = ConfigValidation(values['time_intervals'], 'time_intervals')

        self.send_heroes_for_work = validate.compose(
            'send_heroes_for_work').required().positive().value
        """ 
            [en_US] Time interval for check if there are available heroes to work
            Default value (in minutes): 10
            
            [pt_BR] Intervalo de tempo para verificar se há heróis disponíveis para trabalhar
            Valor padrão (em minutos): 10
        """

        self.refresh_heroes_positions = validate.compose(
            'refresh_heroes_positions').required().positive().value
        """ 
            [en_US] Time interval to update heroes position in the map,
            Default value (in minutes): 3
            
            [pt_BR] Intervalo de tempo para atualizar a posição dos heróis no mapa
            Valor padrão (em minutos): 3
        """

        self.check_for_new_map_button = validate.compose(
            'check_for_new_map_button').required().positive().value
        """ 
            [en_US] Time interval to check for new maps
            Default value (in minutes): 5 
            
            [pt_BR] Intervalo de tempo para verificar por novos mapas
            Valor padrão (em segundos): 5
        """

        self.check_for_captcha = validate.compose(
            'check_for_captcha').required().positive().value
        """ 
            [en_US] Time interval to check for captcha.
            Default value (in minutes): 1
            
            [pt_BR] Intervalo de tempo para verificar se precisa resolver o captcha.
            Valor padrão (em minutos): 1
        """

        self.check_for_login = validate.compose(
            'check_for_login').required().positive().value
        """ 
            [en_US] Time interval to check for login request
            Default value (in minutes): 3
            
            [pt_BR] Intervalo de tempo para verificar se existe solicitação de login
            Valor padrão (em minutos): 5
        """

        self.interval_between_moviments = validate.compose(
            'interval_between_moviments').required().positive().value
        """ 
            [en_US] Time interval between moviments
            Default value (in seconds): 1 
            
            [pt_BR] Intervalo de tempo entre movimentos
            Valor padrão (em segundos): 1
        """

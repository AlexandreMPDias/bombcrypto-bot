from src.helpers.config.validate import ConfigValidation
from src.helpers.config.config_instance import ConfigInstance


class ConfigThresholds(ConfigInstance):
    """ 
    [en_US] How confident the bot needs to be to click the buttons (values from 0 to 1. 0 is the minimum value, 1 is the maximum value)
    [pt_BR] O quão confiante o bot precisa estar para clicar nos botões (valores entre 0 e 1. 0 é o valor mínimo, 1 é o valor máximo)
    """

    def __init__(self, values: dict) -> None:
        validate = ConfigValidation(values['threshold'], 'threshold')

        self.default = validate.compose(
            'default').required().number().percent().value
        """ 
		[en_US]
		Default value: 0.7
		
		[pt_BR]
		Valor padrão: 0.7
        """

        self.commom = validate.compose(
            'commom').required().number().percent().value
        """ 
		[en_US]
		Default value: 0.8
		
		[pt_BR]
		Valor padrão: 0.8
        """

        self.select_wallet_buttons = validate.compose(
            'select_wallet_buttons').required().number().percent().value
        """ 
		[en_US]
		Default value: 0.8
		
		[pt_BR]
		Valor padrão: 0.8
        """

        self.go_to_work_btn = validate.compose(
            'go_to_work_btn').required().number().percent().value
        """ 
		[en_US]
		Default value: 0.9
		
		[pt_BR]
		Valor padrão: 0.9
        """

        self.green_bar = validate.compose(
            'green_bar').required().number().percent().value
        """ 
		[en_US]
		Default value: 0.9
		
		[pt_BR]
		Valor padrão: 0.9
        """

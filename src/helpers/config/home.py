from src.helpers.config.validate import ConfigValidation


class ConfigHome:
    """ 
    [en_US] How confident the bot needs to be to click the buttons (values from 0 to 1. 0 is the minimum value, 1 is the maximum value)
    [pt_BR] O quão confiante o bot precisa estar para clicar nos botões (valores entre 0 e 1. 0 é o valor mínimo, 1 é o valor máximo)
    """

    def __init__(self, values: dict) -> None:
        self.values = values['home']

        validate = ConfigValidation(values, 'home')

        self.enable = validate.compose(
            'enable').required().boolean().value

        self.hero_threshold = validate.compose(
            'hero_threshold').required().number().percent().value
        """ 
        If bot is sending the wrong hero home, make this number bigger.
        if bot is not sending any hero home make this number smaller.
        """

        self.home_button_threshold = validate.compose(
            'home_button_threshold').required().number().percent().value

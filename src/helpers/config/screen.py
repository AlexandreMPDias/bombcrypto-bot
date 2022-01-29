from src.helpers.config.validate import ConfigValidation
from src.helpers.config.config_instance import ConfigInstance


class ConfigScreen(ConfigInstance):

    def __init__(self, values: dict) -> None:
        validate = ConfigValidation(values['screen'], 'screen')

        self.offset_x = validate.compose(
            'offset_x').required().number().value
        self.offset_y = validate.compose(
            'offset_y').required().number().value

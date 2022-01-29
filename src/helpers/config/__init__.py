from src.helpers.config.screen import ConfigScreen
from src.helpers.config.validate import ConfigValidation
from src.helpers.config.thresholds import ConfigThresholds
from src.helpers.config.time_intervals import ConfigTimeIntervals


class Config:
    def __init__(self, config):

        self.thresholds = ConfigThresholds(config)
        self.time_intervals = ConfigTimeIntervals(config)
        self.screen = ConfigScreen(config)

        validate = ConfigValidation(config, '')

        self.scroll_size = validate.compose('scroll_size').required().value
        """
        [en_US]
        Default value: 60

        [pt_BR]
        Valor padrão: 60
        """

        self.scroll_attemps = validate.compose(
            'scroll_attemps').required().value
        """
        [en_US]
        Default value: 3

        [pt_BR]
        Valor padrão: 3
        """

        self.use_click_and_drag_instead_of_scroll = validate.compose(
            'use_click_and_drag_instead_of_scroll').required().value
        """
        [en_US]
        Default value: true

        [pt_BR]
        Valor padrão: true
        """

        self.click_and_drag_amount = validate.compose(
            'click_and_drag_amount').required().value
        """
        [en_US]
        Default value: 200

        [pt_BR]
        Valor padrão: 200
        """

        self.select_heroes_mode = validate.compose(
            'select_heroes_mode').required().enum(['all', 'green', 'full']).value
        """

        [en_US]
        Default value: green
        Available options:
        all   = select all heroes (regardless of the stamina bar)
        green = select the heroes with green stamina bar (half or full)
        full  = select only the heroes with full stamina bar

        [pt_BR]
        Valor padrão: green
        Opções disponíveis:
        all   = seleciona todos os heróis (independente da barra de stamina)
        green = seleciona os heróis com a barra de stamina verde (metade ou cheia)
        full  = seleciona somente os heróis com a barra de stamina cheia
        """

        self.save_log_to_file = validate.compose(
            'save_log_to_file').required().value
        """
        [en_US] Option for save logs to a file (logs.txt)
        Default value: False
        Available options: False or True

        [pt_BR] Opção para salvar os logs em arquivo (logs.txt)
        Valor padrão : False
        Opções disponíveis: False ou True
        """

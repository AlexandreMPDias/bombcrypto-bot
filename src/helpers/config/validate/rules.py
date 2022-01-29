from src.helpers.config.validate.rules_contructor import ConfigValidationRuleConstructor
from src.helpers.debug import Paint


class ConfigValidationRule(ConfigValidationRuleConstructor):

    def percent(self):
        """
            [en_US] Check if the value is a number ranging from 0 to 1
        """
        if not (self.value <= 1.0 and self.value >= 0.0):
            self.raiseInvalid("Value must be between 0.0 and 1.0")
        return self

    def enum(self, options: list):
        if not (self.value in options):
            self.raiseInvalid(f"Value must be one of {options}")
        return self

    def boolean(self):
        if not (self.value in [True, False]):
            self.raiseInvalid(f"Value must be one of type boolean")
        return self

    def defaultTo(self, value):
        if self.value is None:
            self.__source[value] = value
            self.value = value
        return self

    def required(self):
        """
            [en_US] Check if the value is set
        """
        if(self.value is None):
            self.raiseInvalid("Value is required, but it was not found.")
        return self

    def positive(self):
        """
            [en_US] Check if the value is a positive number
        """
        self.castValue(float(self.value))
        if self.value < 0:
            self.raiseInvalid("Value must be a positive number.")
        return self

    def number(self):
        """
            [en_US] Check if the value is a number
        """
        try:
            self.castValue(float(self.value))
        except ValueError:
            self.raiseInvalid("Value must be a number.")
        return self

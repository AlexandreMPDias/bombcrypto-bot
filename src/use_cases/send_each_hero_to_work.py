from src.helpers.logger import Logger

from src.use_cases.utils import UseCase


class SendEachHeroToWork(UseCase):

    def handle(self):
        buttons = self.cv.positions('go-work', threshold='go_to_work_btn')

        # print('buttons: {}'.format(len(buttons)))
        for (x, y, w, h) in buttons:
            self.mouse.click(x+(w/2), y+(h/2), 1)
            self.globals.hero_clicks += 1
            if self.globals.hero_clicks > 20:
                Logger.log(
                    'too many hero clicks, try to increase the go_to_work_btn threshold')
                return
        return len(buttons)

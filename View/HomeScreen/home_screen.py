from View.base_screen import BaseScreenView


class HomeScreenView(BaseScreenView):
    def __init__(self, *args, **kwargs):
        super(HomeScreenView, self).__init__(*args, **kwargs)

    def set_timeout(self, timeout: any, *args) -> None:
        try:
            timeout = float(timeout)
            self.app.switch_screen_timeout = float(timeout)
            self.ids.timeout_field.text = ""
        except:
            self.ids.timeout_field.error = True

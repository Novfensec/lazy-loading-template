from View.HomeScreen.home_screen import HomeScreenView
from View.SettingsScreen.settings_screen import SettingsScreenView

screens = {
    'home screen': {
        'object': HomeScreenView,
        'module': 'View.HomeScreen'
    },
    'settings screen': {
        'object': SettingsScreenView,
        'module': 'View.SettingsScreen'
    },
}

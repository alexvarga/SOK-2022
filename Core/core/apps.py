from django.apps import AppConfig
import pkg_resources


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    source_plugins=[]
    visualization_plugins=[]

    def ready(self):
        self.source_plugins = load_plugins('code.source')
        self.visualization_plugins = load_plugins('code.visualization')


def load_plugins(group):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group):
        p = ep.load()
        print("{} {}".format(ep.name, p), "test")
        plugin = p()
        plugins.append(plugin)
    return plugins

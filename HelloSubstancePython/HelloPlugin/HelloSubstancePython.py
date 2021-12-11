import importlib
import substance_painter_plugins

all_plugins_names = substance_painter_plugins.plugin_module_names()
for name in all_plugins_names:
    print(name)

plugin = importlib.import_module("HelloPlugin")

# 指定したプラグインが開始されていない場合
if not substance_painter_plugins.is_plugin_started(plugin):
    # 指定したプラグインを起動
    substance_painter_plugins.start_plugin(plugin)


def start_plugin():
    print("start")

    for n in substance_painter_plugins.plugin_module_names():
        print(n)

def close_plugin():
    print("close")
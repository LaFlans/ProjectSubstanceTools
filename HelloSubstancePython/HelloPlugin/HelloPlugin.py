from PySide2 import QtWidgets
import substance_painter.ui

plugin_widgets = []

def start_plugin():
    # プラグインが開始した時に呼ばれる
    hello_widget = QtWidgets.QTextEdit()
    hello_widget.setText("Hello from python scripting!")
    hello_widget.setReadOnly(True)
    hello_widget.setWindowTitle("Widget1")

    substance_painter.ui.add_dock_widget(hello_widget)
    plugin_widgets.append(hello_widget)

def close_plugin():
    for widget in plugin_widgets:
        substance_painter.ui.plugin_widgets
    plugin_widgets.clear()

if __name__ == "__main__":
    start_plugin()
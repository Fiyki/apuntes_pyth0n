from tokenize import group
from DI_U04_A02_01 import CronometroUI
import DI_U04_A04_06
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection


TOOLTIP = "Cronómetro"
DOM_XML = """
<ui language='c++'>
    <widget class='CronometroUI' name='cronometroUI'>
        <property name='geometry'>
            <rect>
                <x>0</x>
                <y>0</y>
                <width>400</width>
                <height>200</height>
            </rect>
        </property>
    </widget>
</ui>
"""

QPyDesignerCustomWidgetCollection.registerCustomWidget(CronometroUI, module="C:/Users/danmo/OneDrive/Escritorio/Dam 2/Desarrollo de interfaces/DesarrolloInterfaces_python1/Tema 3/Widgets00 creados con plugin_181/DI_U04_A02_01",
                                                       tool_tip=TOOLTIP, xml=DOM_XML, group="Display Widgets", icon=":/icons/cronometro.png")

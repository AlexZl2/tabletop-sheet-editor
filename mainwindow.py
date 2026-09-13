# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.character_stats = {}

        #Set buttons functionality onClick
        self.ui.export_sheet_button.clicked.connect(self.save_stats_to_file)
        self.ui.import_sheet_button.clicked.connect(self.load_stats_from_file)
        self.ui.calculate_stats_button.clicked.connect(self.calculate_character_stats)

    #Block of functions to determine player stats without
    #needing manual calculation, for convenience
    def determine_intrigue_defense(self):
        #Awareness + Cunning + Status
        awareness_value = int(self.ui.awareness_rating_text.toPlainText());
        cunning_value = int(self.ui.cunning_rating_text.toPlainText());
        status_value = int(self.ui.status_rating_text.toPlainText());
        intrigue_defense = awareness_value + cunning_value + status_value;
        self.ui.intrigue_defense_value_text.setText(str(intrigue_defense));

    def determine_maximum_health(self):
        #Endurance * 3
        endurance_value = int(self.ui.endurance_rating_text.toPlainText());
        max_health_value = endurance_value * 3;
        self.ui.max_health_value_text.setText(str(max_health_value));

    def determine_combat_defense(self):
        #Agility + Athletics + Awareness + Defense Bonus - Armor Penalty
        agility_value = int(self.ui.agility_rating_text.toPlainText());
        athletics_value = int(self.ui.athletics_rating_text.toPlainText());
        awareness_value = int(self.ui.awareness_rating_text.toPlainText());
        defense_value = int(self.ui.armor_rating_final_value.text());
        armor_penalty_value = int(self.ui.armor_penalty_final_value.text());

        combat_defense = agility_value + athletics_value + awareness_value + defense_value - armor_penalty_value;
        self.ui.combat_defense_value_text.setText(str(combat_defense));

    def determine_composure(self):
        #Will * 3
        will_value = int(self.ui.will_rating_text.toPlainText());
        composure_value = will_value * 3;
        self.ui.composure_value_text.setText(str(composure_value));

    def calculate_character_stats(self):
        self.determine_maximum_health()
        self.determine_intrigue_defense()
        self.determine_combat_defense()
        self.determine_composure()

    def update_stats_from_ui(self):
        self.character_stats["agility"] = int(self.ui.agility_rating_text.toPlainText());
        self.character_stats["animal_handling"]= int(self.ui.animal_rating_text.toPlainText());
        self.character_stats["athletics"] = int(self.ui.athletics_rating_text.toPlainText());
        self.character_stats["awareness"] = int(self.ui.awareness_rating_text.toPlainText());
        self.character_stats["cunning"] = int(self.ui.cunning_rating_text.toPlainText());
        self.character_stats["endurance"] = int(self.ui.endurance_rating_text.toPlainText());
        self.character_stats["fighting"] = int(self.ui.fighting_rating_text.toPlainText());
        self.character_stats["healing"] = int(self.ui.healing_rating_text.toPlainText());
        self.character_stats["language"] = int(self.ui.language_rating_text.toPlainText());
        self.character_stats["knowledge"] = int(self.ui.knowledge_rating_text.toPlainText());
        self.character_stats["marksmanship"] = int(self.ui.marksmanship_rating_text.toPlainText());
        self.character_stats["persuasion"] = int(self.ui.persuasion_rating_text.toPlainText());
        self.character_stats["status"] = int(self.ui.status_rating_text.toPlainText());
        self.character_stats["stealth"] = int(self.ui.stealth_rating_text.toPlainText());
        self.character_stats["survival"] = int(self.ui.survival_rating_text.toPlainText());
        self.character_stats["thievery"] = int(self.ui.thievery_rating_text.toPlainText());
        self.character_stats["warfare"] = int(self.ui.warfare_rating_text.toPlainText());
        self.character_stats["will"] = int(self.ui.will_rating_text.toPlainText());

    def update_ui_from_stats(self):
        self.ui.agility_rating_text.setPlainText(str(self.character_stats["agility"]))
        self.ui.animal_rating_text.setPlainText(str(self.character_stats["animal_handling"]))
        self.ui.athletics_rating_text.setPlainText(str(self.character_stats["athletics"]))
        self.ui.awareness_rating_text.setPlainText(str(self.character_stats["awareness"]))
        self.ui.cunning_rating_text.setPlainText(str(self.character_stats["cunning"]))
        self.ui.endurance_rating_text.setPlainText(str(self.character_stats["endurance"]))
        self.ui.fighting_rating_text.setPlainText(str(self.character_stats["fighting"]))
        self.ui.healing_rating_text.setPlainText(str(self.character_stats["healing"]))
        self.ui.language_rating_text.setPlainText(str(self.character_stats["language"]))
        self.ui.knowledge_rating_text.setPlainText(str(self.character_stats["knowledge"]))
        self.ui.marksmanship_rating_text.setPlainText(str(self.character_stats["marksmanship"]))
        self.ui.persuasion_rating_text.setPlainText(str(self.character_stats["persuasion"]))
        self.ui.status_rating_text.setPlainText(str(self.character_stats["status"]))
        self.ui.stealth_rating_text.setPlainText(str(self.character_stats["stealth"]))
        self.ui.survival_rating_text.setPlainText(str(self.character_stats["survival"]))
        self.ui.thievery_rating_text.setPlainText(str(self.character_stats["thievery"]))
        self.ui.warfare_rating_text.setPlainText(str(self.character_stats["warfare"]))
        self.ui.will_rating_text.setPlainText(str(self.character_stats["will"]))

    def save_stats_to_file(self):
        self.update_stats_from_ui();

        character_name = self.ui.name_text.toPlainText() + ".txt";

        with open(character_name, "w") as text_file:
            for stat_name, stat_value in self.character_stats.items():
                text_file.write(f"{stat_name}, {stat_value}\n");

    def load_stats_from_file(self):
        character_name = self.ui.name_text.toPlainText() + ".txt";

        loaded_stats = {}

        with open(character_name, "r") as text_file:
            for line in text_file:
                stat_name, stat_value = line.strip().split(",")
                loaded_stats[stat_name.strip()] = int(stat_value.strip())
        self.character_stats = loaded_stats
        self.update_ui_from_stats()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


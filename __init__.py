from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class UnitConverterSkill(MycroftSkill):

    def __init__(self):
        super(UnitConverterSkill, self).__init__(name="UnitConverterSkill")

    @intent_handler(IntentBuilder("LaunchIntent").require("launch"))
    def handle_launch_intent(self, message):
        print(message)
        self.speak("Hi welcome to unit converter skill")

def create_skill():
    return UnitConverterSkill()

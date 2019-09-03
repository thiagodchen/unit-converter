from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class UnitConverterSkill(MycroftSkill):

    def __init__(self):
        super(UnitConverterSkill, self).__init__(name="UnitConverterSkill")

    def initialize(self):
        self.register_intent_file('convert.intent', self.handle_convert_intent)

    @intent_handler(IntentBuilder("LaunchIntent").require("launch"))
    def handle_launch_intent(self, message):
        print(message)
        self.speak("Hi welcome to unit converter skill")

    def handle_convert_intent(self, message):
        type = message.data.get("type")

        self.speak("The type spoken is " + type)

def create_skill():
    return UnitConverterSkill()

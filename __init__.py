# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class UnitConverterSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(UnitConverterSkill, self).__init__(name="UnitConverterSkill")

    # def initialize(self):
    #     self.register_intent_file()


    # @intent_handler(IntentBuilder("").require("launch"))
    # def handle_launch_intent(self, message):
    #     print(message)
    #     self.speak_dialog("Hi welcome to unit converter skill")

    @intent_file_handler('convert.intent')
    def handle_convert(self, message):
        # value = message.data.get("Value")
        # initUnit = message.data["InitUnit"]
        # finalUnit = message.data["FinalUnit"]

        # print(initUnit)

        self.speak_dialog("the conversion is " + str(value))


    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return UnitConverterSkill()

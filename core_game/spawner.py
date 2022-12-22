import json as json
import logging
import utils.Errors as Errors


class Spawner:
    def __init__(self, path):
        with open(path) as pw:
            entity_data = pw.read()
            self.entity_data = json.loads(entity_data)

            try:
                if self.entity_data["type"] != "entity":
                    logging.error("given object is not a spawn able entity")
                    raise Errors.ObjectTypeError()
            except KeyError:
                logging.error("the given entity does not have a 'type' property")
                return
